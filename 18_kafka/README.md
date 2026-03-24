# Глава 18: Apache Kafka

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/kafka_flow.jpg" width="95%"/></div>

> **Аналогия**: Kafka — это стойка регистрации в страховой компании. Клиенты сдают заявления (продьюсеры), сотрудники их обрабатывают (консьюмеры). Если все сотрудники заняты — заявления ждут в стопке, не теряются.

---

## Зачем нужна Kafka?

**Проблема без Kafka:**
```
Сайт → FastAPI → обработчик → БД
        ↑
     Если 1000 запросов в секунду — API ложится
```

**С Kafka:**
```
Сайт ─┐
Моб.  ├→ Kafka (очередь) → Агент 1 → БД
КЦ   ─┘                 → Агент 2 → Уведомления
                         → Агент 3 → Расчёт премии
```

---

## Ключевые понятия

| Понятие | Аналогия | Пример |
|---|---|---|
| **Topic** | Стопка бумаг | `insurance.claims` |
| **Producer** | Клиент, сдающий заявление | FastAPI-сервер |
| **Consumer** | Сотрудник, обрабатывающий | Агент расчёта |
| **Broker** | Стойка регистрации | Kafka-сервер |
| **Partition** | Несколько стоек | Параллельность |
| **Offset** | Номер в очереди | Где мы остановились |

---

## Установка и запуск

```bash
pip install kafka-python
```

```bash
# Запуск через Docker (самый простой способ)
docker run -d --name kafka \
  -p 9092:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  confluentinc/cp-kafka:latest
```

---

## Продьюсер — отправляем заявления

```python
from kafka import KafkaProducer
import json

# Создаём продьюсера
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8"),
    key_serializer=lambda k: k.encode("utf-8") if k else None
)

def submit_claim(claim_id: int, client_name: str, amount: float, car: str):
    """Отправить заявление в Kafka."""
    message = {
        "claim_id":    claim_id,
        "client_name": client_name,
        "amount":      amount,
        "car":         car,
        "timestamp":   "2026-03-24T07:00:00Z"
    }
    
    # Отправляем в топик insurance.claims
    # key = client_name обеспечивает порядок для одного клиента
    future = producer.send(
        topic="insurance.claims",
        key=client_name,
        value=message
    )
    
    # Ждём подтверждения
    metadata = future.get(timeout=10)
    print(f"Отправлено в partition={metadata.partition}, offset={metadata.offset}")

# Отправляем несколько заявлений
submit_claim(1, "Иванов А.П.",  95000.0, "BMW X5")
submit_claim(2, "Петрова М.С.", 34000.0, "Toyota Vios")
submit_claim(3, "Сидоров К.Д.", 150000.0, "BMW X7")

producer.flush()   # сбрасываем буфер
producer.close()
```

---

## Консьюмер — обрабатываем заявления

```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "insurance.claims",
    bootstrap_servers=["localhost:9092"],
    group_id="claim-processors",         # группа потребителей
    auto_offset_reset="earliest",         # читать с начала если новый
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

def process_claim(claim: dict) -> dict:
    """Обрабатываем заявление."""
    amount = claim["amount"]
    
    # Автоматическое одобрение до 50k
    if amount <= 50_000:
        status = "auto_approved"
    # Ручная проверка 50k-300k
    elif amount <= 300_000:
        status = "manual_review"
    # Крупные суммы — в СБ
    else:
        status = "security_check"
    
    return {**claim, "status": status}

print("Ожидаем заявления...")
for message in consumer:
    claim = message.value
    print(f"\nПолучено: partition={message.partition}, offset={message.offset}")
    print(f"  Клиент: {claim['client_name']}, сумма: {claim['amount']:,.0f} руб.")
    
    result = process_claim(claim)
    print(f"  Статус: {result['status']}")
    
    # Здесь можно сохранить в БД
    # db.update_claim(result["claim_id"], result["status"])
```

---

## Интеграция FastAPI + Kafka

```python
from fastapi import FastAPI
from kafka import KafkaProducer
import json, asyncio

app = FastAPI()
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8")
)

@app.post("/claims")
async def create_claim(
    client_name: str,
    car: str,
    amount: float
):
    """Принимаем заявление и отправляем в очередь."""
    claim = {
        "client_name": client_name,
        "car": car,
        "amount": amount
    }
    
    # Отправляем в Kafka — не ждём обработки
    producer.send("insurance.claims", value=claim)
    producer.flush()
    
    # Сразу отвечаем клиенту
    return {
        "message": "Заявление принято в обработку",
        "status":  "queued"
    }

# Отдельный процесс — consumer-агент
# python consumer_agent.py
```

---

## Надёжная обработка: Dead Letter Queue

```python
from kafka import KafkaConsumer, KafkaProducer
import json, logging

logger = logging.getLogger("consumer")

consumer = KafkaConsumer("insurance.claims", ...)
dlq_producer = KafkaProducer(...)   # Dead Letter Queue

for message in consumer:
    claim = message.value
    try:
        result = process_claim(claim)
        logger.info(f"Обработано: {claim['claim_id']} -> {result['status']}")
        
    except Exception as e:
        # Не смогли обработать — отправляем в DLQ
        logger.error(f"Ошибка обработки {claim.get('claim_id')}: {e}")
        dlq_producer.send(
            "insurance.claims.dlq",
            value={**claim, "error": str(e)}
        )
```

---

## Мониторинг Kafka-лагов

```bash
# Сколько сообщений не обработано (lag)
kafka-consumer-groups.sh \
  --bootstrap-server localhost:9092 \
  --group claim-processors \
  --describe

# Вывод:
# GROUP            TOPIC            PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
# claim-processors insurance.claims 0          847             850             3
```

---

## Упражнения

1. Запустите Kafka через Docker.
2. Напишите продьюсер — отправляйте 10 заявлений.
3. Напишите консьюмер — печатайте каждое заявление.
4. Добавьте логику: суммы до 50k → `auto`, выше → `manual`.
5. Интегрируйте с FastAPI: `/claims POST` → Kafka → консьюмер → SQLite.
