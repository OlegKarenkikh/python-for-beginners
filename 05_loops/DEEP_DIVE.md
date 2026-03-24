# 🔄 Глава 05: Второй взгляд — Циклы и их ловушки

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/loops_comparison.jpg" width="95%"/></div>

---

## Другая аналогия: музыкальный плеер

`for` — плейлист с конкретными песнями. Проиграл все — стоп.
`while` — кнопка "повтор". Играет пока не нажмёшь стоп.

---

## Страшная сторона: бесконечный цикл

```python
# ОПАСНО — программа зависнет!
while True:
    print("Работаем...")
    # забыли break — будет работать вечно

# ПРАВИЛЬНО — всегда есть условие выхода
attempts = 0
while attempts < 3:
    code = input("Код подтверждения: ")
    if code == "1234":
        print("Верно!")
        break
    attempts += 1
    print(f"Осталось попыток: {3 - attempts}")
else:
    print("Превышено количество попыток")
```

---

## Страшная сторона: изменение списка во время итерации

```python
claims = [
    {"id": 1, "amount": 5_000,   "status": "pending"},
    {"id": 2, "amount": 150_000, "status": "pending"},
    {"id": 3, "amount": 8_000,   "status": "pending"},
]

# ОПАСНО — изменяем список пока перебираем
for claim in claims:
    if claim["amount"] > 100_000:
        claims.remove(claim)   # ЭТО ПРОПУСТИТ ЭЛЕМЕНТЫ!

# ПРАВИЛЬНО — создаём новый список
small_claims = [c for c in claims if c["amount"] <= 100_000]

# ИЛИ итерируемся по копии
for claim in claims[:]:   # claims[:] — копия списка
    if claim["amount"] > 100_000:
        claims.remove(claim)
```

---

## Страшная сторона: range и индексы

```python
clients = ["Иванов", "Петрова", "Сидоров"]

# НЕПРАВИЛЬНО
for i in range(4):         # range(4) = 0,1,2,3 — но список длиной 3!
    print(clients[i])      # IndexError на i=3!

# ПРАВИЛЬНО — используйте len()
for i in range(len(clients)):   # range(3) = 0,1,2
    print(clients[i])

# ЛУЧШЕ — enumerate
for i, name in enumerate(clients):
    print(f"{i+1}. {name}")

# ИДЕАЛЬНО — прямой перебор
for name in clients:
    print(name)
```

---

## Полезные паттерны в страховании

```python
claims = [
    {"id": 1, "amount": 5_000,   "approved": True},
    {"id": 2, "amount": 150_000, "approved": False},
    {"id": 3, "amount": 8_000,   "approved": True},
    {"id": 4, "amount": 45_000,  "approved": True},
]

# Паттерн 1: фильтрация
approved = [c for c in claims if c["approved"]]

# Паттерн 2: сумма с условием
total_approved = sum(c["amount"] for c in claims if c["approved"])

# Паттерн 3: поиск первого подходящего
big_claim = next(
    (c for c in claims if c["amount"] > 100_000),
    None   # если не нашли
)

# Паттерн 4: группировка
from collections import defaultdict
by_status = defaultdict(list)
for c in claims:
    key = "approved" if c["approved"] else "rejected"
    by_status[key].append(c)

print(f"Одобрено:  {len(by_status['approved'])}")
print(f"Отклонено: {len(by_status['rejected'])}")
```
