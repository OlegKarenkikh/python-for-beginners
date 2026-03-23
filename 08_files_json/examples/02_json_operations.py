# Глава 08 — Работа с JSON
import json

# Страховая база данных в JSON
database = {
    "company": "ПолисПлюс",
    "year": 2024,
    "clients": [
        {"id": 1, "name": "Иванов А.П.", "age": 35, "premium": 14_400, "active": True},
        {"id": 2, "name": "Петрова М.С.", "age": 22, "premium": 21_600, "active": True},
        {"id": 3, "name": "Сидоров В.Н.", "age": 68, "premium": 18_000, "active": False},
    ]
}

# Сохраняем
with open("insurance_db.json", "w", encoding="utf-8") as f:
    json.dump(database, f, ensure_ascii=False, indent=2)

print("Сохранено в insurance_db.json")

# Загружаем и используем
with open("insurance_db.json", "r", encoding="utf-8") as f:
    db = json.load(f)

print(f"\nКомпания: {db['company']}, год: {db['year']}")
print(f"Всего клиентов: {len(db['clients'])}")

active_clients = [c for c in db["clients"] if c["active"]]
total = sum(c["premium"] for c in active_clients)
print(f"Активных: {len(active_clients)}, сборы: {total:,} руб.")

import os; os.remove("insurance_db.json")
