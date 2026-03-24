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
