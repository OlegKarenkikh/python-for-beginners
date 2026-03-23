# Глава 06 — Первые функции

def greet_client(name):
    """Приветствие клиента страховой компании."""
    return f"Добро пожаловать, {name}! Мы рады видеть вас в ПолисПлюс."

def get_policy_number(client_id, year=2024):
    """Генерирует номер полиса."""
    return f"POL-{year}-{client_id:05d}"

def calculate_basic_premium(car_value, rate=0.04):
    """Базовая премия КАСКО: 4% от стоимости авто."""
    return round(car_value * rate, 2)

# Демонстрация
clients = [("Иванов", 1), ("Петрова", 2), ("Сидоров", 3)]

for name, cid in clients:
    print(greet_client(name))
    print(f"  Полис: {get_policy_number(cid)}")
    car_val = 1_500_000
    print(f"  Базовая КАСКО ({car_val:,} руб.): {calculate_basic_premium(car_val):,} руб.")
    print()
