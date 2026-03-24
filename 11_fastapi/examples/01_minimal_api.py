"""
Глава 11: FastAPI — минимальный рабочий сервер
Запуск: uvicorn 01_minimal_api:app --reload
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(
    title="ПолисПлюс API",
    description="Страховые расчёты через REST API",
    version="1.0.0",
)

BASE_RATE = 12_000

# База в памяти
clients_db: List[dict] = [
    {"id": 1, "name": "Иванов А.П.",  "age": 35, "accidents": 0},
    {"id": 2, "name": "Петрова М.С.", "age": 22, "accidents": 1},
]


class ClientIn(BaseModel):
    name:      str
    age:       int = Field(ge=18, le=90, description="Возраст от 18 до 90")
    accidents: int = Field(default=0, ge=0)


class PremiumOut(BaseModel):
    name:    str
    age:     int
    premium: float
    risk:    str


@app.get("/")
def root():
    return {"service": "ПолисПлюс API", "status": "ok"}


@app.get("/clients")
def list_clients():
    return {"clients": clients_db, "total": len(clients_db)}


@app.get("/clients/{client_id}")
def get_client(client_id: int):
    for c in clients_db:
        if c["id"] == client_id:
            return c
    raise HTTPException(status_code=404, detail=f"Клиент {client_id} не найден")


@app.post("/clients", status_code=201)
def add_client(client: ClientIn):
    new_id = max((c["id"] for c in clients_db), default=0) + 1
    new_client = {"id": new_id, **client.model_dump()}
    clients_db.append(new_client)
    return {"message": "Клиент добавлен", "id": new_id}


@app.post("/premium", response_model=PremiumOut)
def calculate(client: ClientIn):
    premium = BASE_RATE
    risk = "low"
    if client.age < 25:
        premium *= 1.5
        risk = "high"
    elif client.age > 65:
        premium *= 1.3
        risk = "medium"
    if client.accidents > 0:
        premium *= 1 + client.accidents * 0.2
        risk = "high"
    return PremiumOut(
        name=client.name,
        age=client.age,
        premium=round(premium, 2),
        risk=risk,
    )


@app.get("/stats")
def stats():
    if not clients_db:
        return {"error": "Нет клиентов"}
    ages = [c["age"] for c in clients_db]
    return {
        "total_clients": len(clients_db),
        "avg_age": round(sum(ages) / len(ages), 1),
        "min_age": min(ages),
        "max_age": max(ages),
    }
