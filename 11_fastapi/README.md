# ⚡ Глава 11: FastAPI — первый API

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/fastapi_flow.jpg" width="95%"/>
</div>

> **API** — программа, которую вызывают другие программы.
> Напишем API расчёта страховой премии.

---

## Установка

```bash
pip install fastapi uvicorn[standard]
```

---

## Минимальный сервер

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ПолисПлюс API работает!"}
```

**Запуск:** `uvicorn main:app --reload`
Документация: `http://localhost:8000/docs`

---

## GET: расчёт премии через URL

```python
from fastapi import FastAPI

app = FastAPI()
BASE_RATE = 12_000

@app.get("/premium")
def calculate_premium(age: int, accidents: int = 0):
    premium = BASE_RATE
    if age < 25:
        premium *= 1.5
    elif age > 65:
        premium *= 1.3
    if accidents > 0:
        premium *= 1 + accidents * 0.2
    return {
        "age": age,
        "premium": round(premium, 2),
        "currency": "RUB",
    }
```

Вызов: `http://localhost:8000/premium?age=22&accidents=1`

```json
{
  "age": 22,
  "premium": 21600.0,
  "currency": "RUB"
}
```

---

## POST: запрос с телом JSON (Pydantic)

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
BASE_RATE = 12_000

class ClientRequest(BaseModel):
    name:      str
    age:       int = Field(ge=18, le=90)
    accidents: int = Field(default=0, ge=0)

class PremiumResponse(BaseModel):
    name:    str
    premium: float
    risk:    str

@app.post("/premium", response_model=PremiumResponse)
def calc(client: ClientRequest):
    premium = BASE_RATE
    risk = "low"
    if client.age < 25:
        premium *= 1.5
        risk = "high"
    if client.accidents > 0:
        premium *= 1 + client.accidents * 0.2
        risk = "high"
    return PremiumResponse(
        name=client.name,
        premium=round(premium, 2),
        risk=risk,
    )
```

**Вызов (curl):**
```bash
curl -X POST "http://localhost:8000/premium" \
     -H "Content-Type: application/json" \
     -d '{"name": "Иванов", "age": 22, "accidents": 1}'
```

```json
{
  "name": "Иванов",
  "premium": 21600.0,
  "risk": "high"
}
```

---

## CRUD: работа со списком клиентов

```python
from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

# "База" в памяти
db: List[dict] = [
    {"id": 1, "name": "Иванов А.П.",  "age": 35},
    {"id": 2, "name": "Петрова М.С.", "age": 22},
]

@app.get("/clients")
def get_all():
    return {"clients": db, "total": len(db)}

@app.get("/clients/{client_id}")
def get_one(client_id: int):
    for c in db:
        if c["id"] == client_id:
            return c
    raise HTTPException(status_code=404, detail="Клиент не найден")

@app.post("/clients")
def add_client(name: str, age: int):
    new_id = max(c["id"] for c in db) + 1
    client = {"id": new_id, "name": name, "age": age}
    db.append(client)
    return {"message": "Добавлен", "client": client}
```

---

## Что делает FastAPI автоматически

| Функция | Как использовать |
|---|---|
| Документация Swagger | `/docs` — интерактивное тестирование |
| Документация ReDoc | `/redoc` — красивое чтение |
| Валидация типов | Pydantic — ошибка 422 если данные неверны |
| Схема API (OpenAPI) | `/openapi.json` — машиночитаемое описание |

---

## Структура проекта

```
polisplus_api/
├── main.py
├── routers/
│   ├── clients.py
│   └── premium.py
├── models/
│   └── schemas.py
├── services/
│   └── calculator.py
└── requirements.txt
```

---

## Упражнения

1. Добавьте `GET /clients/city/{city}` — клиенты из конкретного города
2. Сделайте `POST /batch-premium` — принимает список клиентов, возвращает список премий
3. Добавьте middleware для логирования каждого запроса


---

## ❓ Вопросы которые возникают при изучении

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/qa_fastapi.png" alt="Вопросы о FastAPI" width="95%"/>
</div>

---

### 🙋 Что такое `@app.get("/")`? Зачем `@`?

`@` — это **декоратор**. Он модифицирует функцию которая идёт сразу после него.
`@app.get("/")` означает: «зарегистрируй следующую функцию как обработчик GET-запроса на `/`».

```python
@app.get("/premium")
def calculate(age: int):
    return {"premium": age * 500}

# Технически это сокращение для:
def calculate(age: int):
    return {"premium": age * 500}
calculate = app.get("/premium")(calculate)
```

Когда приходит GET-запрос на `/premium` — FastAPI находит функцию и вызывает её.

---

### 🙋 `uvicorn main:app --reload` — как расшифровать?

- `uvicorn` — ASGI-сервер (программа которая запускает ваш FastAPI)
- `main` — файл `main.py` (без расширения `.py`)
- `app` — переменная `app = FastAPI()` внутри этого файла
- `--reload` — перезапускать автоматически при изменении файлов

> ⚠️ `--reload` только для разработки! В продакшне уберите этот флаг.

---

### 🙋 `class ClientRequest(BaseModel)` — что это за класс?

`BaseModel` из библиотеки Pydantic — класс для валидации данных.
Когда вы пишете `class ClientRequest(BaseModel)` — создаёте **схему запроса**:

```python
class ClientRequest(BaseModel):
    name:      str
    age:       int = Field(ge=18, le=90)
    accidents: int = Field(default=0, ge=0)

# FastAPI автоматически:
# 1. Прочитает JSON из тела запроса
# 2. Проверит типы (age должен быть int)
# 3. Проверит диапазон (18 ≤ age ≤ 90)
# 4. При ошибке — вернёт HTTP 422 с описанием проблемы
```

---

### 🙋 `ge=18, le=90` — что значат эти параметры?

- `ge` — **g**reater or **e**qual (≥ 18)
- `le` — **l**ess or **e**qual (≤ 90)
- `gt` — **g**reater **t**han (> строго)
- `lt` — **l**ess **t**han (< строго)

```python
age: int = Field(ge=18, le=90)    # 18 ≤ age ≤ 90
amount: float = Field(gt=0)       # amount > 0
```

---

### 🙋 `raise HTTPException` — что делает `raise`?

`raise` — намеренно поднять исключение (прервать выполнение с сообщением об ошибке).

```python
@app.get("/clients/{client_id}")
def get_client(client_id: int):
    for c in db:
        if c["id"] == client_id:
            return c   # нашли — возвращаем
    
    raise HTTPException(status_code=404, detail="Клиент не найден")
    # ↑ прерывает выполнение, FastAPI вернёт клиенту:
    # HTTP 404
    # {"detail": "Клиент не найден"}
```

`raise` используется когда что-то пошло не так и продолжать выполнение нельзя.

---

### 🙋 Зачем `response_model=PremiumResponse`?

Три пользы:
1. **Документация** — Swagger UI (`/docs`) покажет правильную схему ответа
2. **Фильтрация** — лишние поля не попадут в ответ (например внутренние флаги)
3. **Валидация** — если вернёте данные неправильного типа — ошибка на этапе разработки

```python
@app.post("/premium", response_model=PremiumResponse)
def calc(client: ClientRequest):
    # Если вернуть dict с лишними полями — они будут отфильтрованы
    # Если забыть обязательное поле — ошибка при разработке, не в продакшне
    return PremiumResponse(name=client.name, premium=12000, risk="low")
```
