# 🔢 Глава 03: Числа и логика

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/numbers_traps.jpg" alt="Числа и ловушки" width="90%"/></div>

> **Цель:** уверенно считать и сравнивать значения
> **Время:** ~1 час

---

## Типы чисел

```python
age = 35                 # int — целое
rate = 1.15              # float — дробное
big = 1_500_000          # _ как разделитель тысяч
```

## Арифметика страхового калькулятора

```python
base = 12_000
age_coeff = 1.5
accident_coeff = 1.2

premium = base * age_coeff * accident_coeff
print(f"Премия: {premium:,.2f} руб.")   # 21,600.00 руб.

# Полезные операции
print(round(21600.678, 0))   # 21601.0
print(abs(-5_000))           # 5000
print(max(1.2, 0.9, 1.5))   # 1.5
print(min(1.2, 0.9, 1.5))   # 0.9
```

## Операторы сравнения и логика

```python
age = 22
experience = 3
accidents = 0

# Сравнение
young = age < 25          # True
experienced = experience > 5  # False

# and, or, not
needs_surcharge = young and not experienced
print(needs_surcharge)    # True

# in — проверить вхождение в список
risk_cities = ["Москва", "СПб", "Казань"]
city = "Москва"
city_risk = city in risk_cities  # True
```

---

## Практика

```bash
python examples/01_arithmetic.py
python examples/02_comparisons.py
```

➡️ [Глава 04: Условия](../04_conditions/README.md)
