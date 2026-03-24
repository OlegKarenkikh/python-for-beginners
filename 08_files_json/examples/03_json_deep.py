"""
Глава 08-ext: работа с JSON — чтение, запись, обработка
"""
import json
import os

CLIENTS = [
    {"id": 1, "name": "Иванов А.П.",  "age": 35, "accidents": 0},
    {"id": 2, "name": "Петрова М.С.", "age": 22, "accidents": 1},
    {"id": 3, "name": "Сидоров К.Д.", "age": 47, "accidents": 0},
]

# --- 1. Запись в файл ---
filename = "clients.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(CLIENTS, f, ensure_ascii=False, indent=2)
print(f"Записано {len(CLIENTS)} клиентов в {filename}")

# --- 2. Чтение из файла ---
with open(filename, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"Прочитано: {len(loaded)} клиентов")

# --- 3. Добавление поля и перезапись ---
BASE_RATE = 12_000
for c in loaded:
    premium = BASE_RATE
    if c["age"] < 25:
        premium *= 1.5
    if c["accidents"] > 0:
        premium *= 1 + c["accidents"] * 0.2
    c["premium"] = round(premium, 2)

with open("clients_with_premium.json", "w", encoding="utf-8") as f:
    json.dump(loaded, f, ensure_ascii=False, indent=2)

# --- 4. Вывод финального JSON ---
print("\nФинальный JSON:")
print(json.dumps(loaded, ensure_ascii=False, indent=2))

# --- 5. Вложенная структура ---
policy = {
    "number": "POL-2024-00042",
    "client": {
        "name": "Иванов А.П.",
        "age": 35,
        "contacts": {
            "phone": "+7 (495) 123-45-67",
            "email": "ivanov@mail.ru",
        },
    },
    "coverage": {
        "type": "КАСКО",
        "amount": 1_500_000,
    },
    "premium": 12_000,
}

print("\nПолис:")
print(f"  Номер:    {policy['number']}")
print(f"  Клиент:   {policy['client']['name']}")
print(f"  Покрытие: {policy['coverage']['amount']:,} руб.")
print(f"  Телефон:  {policy['client']['contacts']['phone']}")

# Очистка
os.remove(filename)
os.remove("clients_with_premium.json")
