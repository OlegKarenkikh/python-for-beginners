# Глава 07 — База данных клиентов
clients = [
    {"id": 1, "name": "Иванов А.П.", "age": 35, "premium": 14_400, "active": True},
    {"id": 2, "name": "Петрова М.С.", "age": 22, "premium": 21_600, "active": True},
    {"id": 3, "name": "Сидоров В.Н.", "age": 68, "premium": 18_000, "active": False},
    {"id": 4, "name": "Козлова Е.В.", "age": 31, "premium": 12_800, "active": True},
    {"id": 5, "name": "Волков Д.А.", "age": 44, "premium": 9_900, "active": True},
]

# Только активные
active = [c for c in clients if c["active"]]
print(f"Активных полисов: {len(active)}")

# Сборы по активным
total = sum(c["premium"] for c in active)
print(f"Сборы (активные): {total:,} руб.")

# Найти самый дорогой полис
most_expensive = max(clients, key=lambda c: c["premium"])
print(f"Самый дорогой: {most_expensive['name']} — {most_expensive['premium']:,} руб.")

# Сортировка по премии
sorted_clients = sorted(clients, key=lambda c: c["premium"], reverse=True)
print("\nТоп-3 по премии:")
for c in sorted_clients[:3]:
    print(f"  {c['name']:25} {c['premium']:,} руб.")
