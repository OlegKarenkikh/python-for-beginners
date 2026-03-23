# Глава 01 — Ответ к упражнению 2

# Клиент 1
name1 = "Козлов"
age1 = 45
base = 10_000
premium1 = base * (1 + age1 / 100)

# Клиент 2
name2 = "Зайцева"
age2 = 19
premium2 = base * (1 + age2 / 100)

print(f"{name1}: {premium1:,.0f} руб./год")
print(f"{name2}: {premium2:,.0f} руб./год")
