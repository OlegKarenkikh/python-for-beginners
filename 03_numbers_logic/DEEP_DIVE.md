# 🔢 Глава 03: Второй взгляд — Числа и ловушки

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/numbers_traps.jpg" width="95%"/></div>

---

## Другая аналогия: числа как стаканы разного размера

`int` — стакан для воды (целые числа). `float` — термос (дробные).
Если смешать — Python иногда удивит.

```python
# Делите? Думайте о типе результата!
13 / 5    # → 2.6  (всегда float!)
13 // 5   # → 2    (только целая часть)
13 % 5    # → 3    (остаток от деления)

# В страховании важно:
total_claims = 47
per_agent    = total_claims // 5   # 9 дел на агента
remainder    = total_claims % 5    # 2 дела остались
print(f"По {per_agent} дел, ещё {remainder} в очереди")
```

---

## Страшная сторона: деньги и float

```python
# НИКОГДА не используйте float для денег!
premium = 0.1 + 0.2
print(premium)   # 0.30000000000000004  ← ЭТО НЕ 0.3!

# Почему? float хранится в двоичном виде — некоторые числа
# не представимы точно, как 1/3 в десятичной дроби

# ПРАВИЛЬНО — для денег используйте Decimal
from decimal import Decimal
p1 = Decimal("0.1")
p2 = Decimal("0.2")
print(p1 + p2)   # 0.3 — точно!

# В страховой системе:
base    = Decimal("12000.00")
coeff   = Decimal("1.50")
premium = base * coeff
print(f"Премия: {premium} руб.")  # 18000.00 — точно
```

---

## Страшная сторона: деление на ноль

```python
# Это вызовет ошибку!
claims_count = 0
avg_amount = total_amount / claims_count
# ZeroDivisionError: division by zero

# Защита
avg_amount = total_amount / claims_count if claims_count > 0 else 0
print(f"Средняя сумма: {avg_amount:,.0f} руб.")
```

---

## Страшная сторона: большие числа и читаемость

```python
# Плохо — число невозможно прочитать
max_coverage = 1000000000

# Хорошо — Python игнорирует _ как разделитель
max_coverage = 1_000_000_000
annual_premium = 14_400.50

# Форматирование вывода
print(f"Покрытие: {max_coverage:,} руб.")   # 1,000,000,000 руб.
print(f"Премия:   {annual_premium:.2f} руб.")  # 14400.50 руб.
```

---

## Полезные функции для страхования

```python
import math

# Округление — три способа
premium = 14567.333

round(premium, 0)      # 14567.0 — математическое
math.floor(premium)    # 14567   — вниз (в пользу клиента)
math.ceil(premium)     # 14568   — вверх (в пользу СК)

# abs — для разниц
delta = abs(actual_loss - estimated_loss)

# Мин/макс в списках
premiums = [12000, 18000, 9500, 24000]
print(f"Мин: {min(premiums):,}")   # 9,500
print(f"Макс: {max(premiums):,}")  # 24,000
print(f"Сумма: {sum(premiums):,}") # 63,500

# Процентное изменение
old_premium = 12_000
new_premium = 14_400
change_pct  = (new_premium - old_premium) / old_premium * 100
print(f"Рост: {change_pct:.1f}%")  # Рост: 20.0%
```
