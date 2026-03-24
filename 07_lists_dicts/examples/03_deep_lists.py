"""
Глава 07-ext: списки, срезы, comprehension — рабочий пример
Задача: обработать базу клиентов ПолисПлюс
"""

clients = [
    {"name": "Иванов А.П.",  "age": 35, "accidents": 0, "city": "Москва"},
    {"name": "Петрова М.С.", "age": 22, "accidents": 1, "city": "СПб"},
    {"name": "Сидоров К.Д.", "age": 47, "accidents": 0, "city": "Москва"},
    {"name": "Орлова Е.В.",  "age": 19, "accidents": 0, "city": "Казань"},
    {"name": "Козлов В.И.",  "age": 60, "accidents": 2, "city": "Москва"},
]

BASE_RATE = 12_000

def calculate_premium(age: int, accidents: int) -> float:
    premium = BASE_RATE
    if age < 25:
        premium *= 1.5
    elif age > 55:
        premium *= 1.3
    if accidents > 0:
        premium *= 1 + accidents * 0.2
    return round(premium, 2)


# --- 1. Добавляем премию каждому клиенту (comprehension) ---
clients_with_premium = [
    {**c, "premium": calculate_premium(c["age"], c["accidents"])}
    for c in clients
]

# --- 2. Фильтрация: только молодые (< 25) ---
young = [c for c in clients_with_premium if c["age"] < 25]
print("Молодые клиенты:")
for c in young:
    print(f"  {c['name']}, {c['age']} лет, {c['premium']:,.0f} руб.")

# --- 3. Сортировка по премии (от высокой к низкой) ---
by_premium = sorted(clients_with_premium, key=lambda c: c["premium"], reverse=True)
print("\nТоп по премии:")
for i, c in enumerate(by_premium, 1):
    print(f"  {i}. {c['name']}: {c['premium']:,.0f} руб.")

# --- 4. Группировка по городу ---
cities = {}
for c in clients_with_premium:
    city = c["city"]
    if city not in cities:
        cities[city] = []
    cities[city].append(c["name"])

print("\nКлиенты по городам:")
for city, names in cities.items():
    print(f"  {city}: {', '.join(names)}")

# --- 5. Сводная статистика ---
premiums = [c["premium"] for c in clients_with_premium]
print(f"\nСтатистика:")
print(f"  Всего клиентов: {len(premiums)}")
print(f"  Мин. премия:    {min(premiums):,.0f} руб.")
print(f"  Макс. премия:   {max(premiums):,.0f} руб.")
print(f"  Средняя:        {sum(premiums)/len(premiums):,.0f} руб.")
print(f"  Итого сборов:   {sum(premiums):,.0f} руб.")
