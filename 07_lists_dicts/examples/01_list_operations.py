# Глава 07 — Операции со списками
premiums = [15_200, 34_800, 8_500, 22_100, 19_600]

print("Список премий:", premiums)
print(f"Первая: {premiums[0]:,}")
print(f"Последняя: {premiums[-1]:,}")
print(f"Сумма: {sum(premiums):,}")
print(f"Среднее: {sum(premiums)/len(premiums):,.0f}")

# Добавим новую
premiums.append(31_000)

# Отсортируем
premiums.sort(reverse=True)
print("\nПо убыванию:", [f"{p:,}" for p in premiums])

# List comprehension — короткий способ фильтрации
big = [p for p in premiums if p > 20_000]
print(f"\nПремий > 20 000: {len(big)}")
