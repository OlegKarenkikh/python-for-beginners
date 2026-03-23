# Глава 01 — Пример 3: Расчёт страховой премии
# Запустите: python examples/03_calculations.py

# Исходные данные
client_name = "Сидоров Виктор Николаевич"
age = 35
base_rate = 12_000     # базовая годовая ставка (руб.)
risk_factor = 1.2      # коэффициент риска
discount = 0.9         # скидка за безаварийность

# Расчёт
gross_premium = base_rate * risk_factor
net_premium = gross_premium * discount

# Вывод
print(f"Клиент: {client_name}")
print(f"Базовая ставка: {base_rate:,} руб.")
print(f"Коэффициент риска: {risk_factor}")
print(f"Скидка: {(1 - discount) * 100:.0f}%")
print(f"──────────────────────────")
print(f"Страховая премия: {net_premium:,.0f} руб./год")

# type() — узнать тип переменной
print(f"\nТип base_rate: {type(base_rate)}")
print(f"Тип net_premium: {type(net_premium)}")
print(f"Тип client_name: {type(client_name)}")
