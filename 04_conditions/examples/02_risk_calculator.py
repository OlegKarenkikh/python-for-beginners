# Глава 04 — Расчёт коэффициента риска

name = "Петрова М.С."
age = 22
experience = 2
accidents = 1
base_rate = 12_000

# Коэффициент по возрасту
if age < 25:
    age_factor = 1.5
elif age > 60:
    age_factor = 1.3
else:
    age_factor = 1.0

# Коэффициент по авариям
if accidents == 0:
    acc_factor = 0.9
elif accidents <= 2:
    acc_factor = 1.0 + accidents * 0.15
else:
    acc_factor = 1.5

# Итог
premium = base_rate * age_factor * acc_factor
print(f"Клиент: {name}")
print(f"Коэф. возраст: {age_factor}")
print(f"Коэф. аварии:  {acc_factor}")
print(f"Премия: {premium:,.0f} руб./год")
