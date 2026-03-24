# Глава 17: Мониторинг

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/prometheus_grafana.jpg" width="95%"/></div>

> **Аналогия**: Prometheus — это спидометр и датчики в машине. Grafana — приборная панель, которую видит водитель. Python-приложение — двигатель.

---

## Зачем нужен мониторинг?

Без мониторинга вы узнаёте о проблеме от пользователя.
С мониторингом — видите аномалию раньше, чем её заметит кто-то другой.

**Что мониторим в страховой системе:**
- Сколько заявок обрабатывается в минуту
- Время расчёта премии (медиана, 95-й перцентиль)
- Количество ошибок
- Сколько заявок в очереди

---

## Три типа метрик Prometheus

| Тип | Что делает | Пример |
|---|---|---|
| **Counter** | Только растёт | Количество запросов |
| **Gauge** | Растёт и уменьшается | Заявок в очереди |
| **Histogram** | Распределение | Время ответа API |

---

## Установка

```bash
pip install prometheus-client
```

---

## Метрики в чистом Python

```python
from prometheus_client import Counter, Gauge, Histogram, start_http_server
import time, random

# Объявляем метрики
CLAIMS_TOTAL = Counter(
    "insurance_claims_total",
    "Всего обработано заявлений",
    ["status"]         # labels: approved / rejected / error
)

CLAIMS_IN_QUEUE = Gauge(
    "insurance_claims_in_queue",
    "Заявлений в очереди на обработку"
)

PROCESSING_TIME = Histogram(
    "insurance_processing_seconds",
    "Время обработки заявления",
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
)

# Запускаем HTTP-эндпоинт /metrics на порту 8000
start_http_server(8000)
print("Metrics available at http://localhost:8000/metrics")

# Имитируем работу
while True:
    # Заявление пришло
    CLAIMS_IN_QUEUE.inc()
    
    start = time.time()
    time.sleep(random.uniform(0.1, 0.8))   # обработка
    
    # Заявление обработано
    duration = time.time() - start
    PROCESSING_TIME.observe(duration)
    CLAIMS_IN_QUEUE.dec()
    
    status = random.choice(["approved", "rejected", "approved", "approved"])
    CLAIMS_TOTAL.labels(status=status).inc()
    
    print(f"Заявление {status} за {duration:.2f}с")
```

---

## Метрики в FastAPI

```python
from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
import time
from fastapi.responses import Response

app = FastAPI()

# Метрики
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Количество HTTP запросов",
    ["method", "endpoint", "status_code"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Время обработки запроса",
    ["endpoint"]
)

PREMIUM_CALCULATED = Counter(
    "premium_calculations_total",
    "Расчётов премии выполнено"
)

# Middleware для автоматического сбора метрик
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status_code=response.status_code
    ).inc()
    
    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(duration)
    return response

# Эндпоинт для Prometheus
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Бизнес-эндпоинт
@app.post("/calculate-premium")
def calculate_premium(age: int, accidents: int = 0):
    base = 12_000
    if age < 25:
        base *= 1.5
    if accidents > 0:
        base *= 1 + accidents * 0.2
    
    PREMIUM_CALCULATED.inc()
    return {"premium": round(base, 2)}
```

---

## Что происходит на /metrics

```
# HELP insurance_claims_total Всего обработано заявлений
# TYPE insurance_claims_total counter
insurance_claims_total{status="approved"} 847.0
insurance_claims_total{status="rejected"} 153.0

# HELP http_request_duration_seconds Время обработки
# TYPE http_request_duration_seconds histogram
http_request_duration_seconds_bucket{endpoint="/calculate-premium",le="0.1"} 632
http_request_duration_seconds_bucket{endpoint="/calculate-premium",le="0.5"} 941
http_request_duration_seconds_sum{endpoint="/calculate-premium"} 187.4
http_request_duration_seconds_count{endpoint="/calculate-premium"} 1000
```

---

## Настройка Prometheus

`prometheus.yml`:
```yaml
global:
  scrape_interval: 15s   # опрашивать каждые 15 секунд

scrape_configs:
  - job_name: insurance-api
    static_configs:
      - targets: ['localhost:8000']   # адрес нашего приложения
```

```bash
# Запуск Prometheus
docker run -d \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

---

## Grafana — настройка дашборда

```bash
# Запуск Grafana
docker run -d -p 3000:3000 grafana/grafana
# Открыть: http://localhost:3000  (admin/admin)
```

**Полезные PromQL-запросы для дашборда:**

```promql
# RPS (requests per second)
rate(http_requests_total[5m])

# Процент ошибок
rate(http_requests_total{status_code=~"5.."}[5m])
  / rate(http_requests_total[5m]) * 100

# 95-й перцентиль времени ответа
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# Заявлений в очереди
insurance_claims_in_queue

# Алерт: более 10 ошибок за 5 минут
rate(http_requests_total{status_code=~"5.."}[5m]) > 10
```

---

## Анализ логов: loki + promtail

```bash
# Добавить к docker-compose
loki:
  image: grafana/loki
  ports: ["3100:3100"]

promtail:
  image: grafana/promtail
  volumes:
    - ./logs:/logs
    - ./promtail.yml:/etc/promtail/config.yml
```

```yaml
# promtail.yml
scrape_configs:
  - job_name: insurance-logs
    static_configs:
      - targets: [localhost]
        labels:
          job: insurance
          __path__: /logs/*.log
```

Теперь в Grafana видны и метрики, и логи в одном дашборде.

---

## Упражнения

1. Добавьте `prometheus-client` в FastAPI из главы 11.
2. Создайте Counter `policies_issued_total` и Gauge `active_policies`.
3. Запустите Prometheus + Grafana через Docker.
4. Добавьте дашборд: RPS, время ответа, количество ошибок.
5. Настройте алерт: если `active_policies < 10` — предупреждение.
