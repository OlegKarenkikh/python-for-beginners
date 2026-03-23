# 🔧 Глава 06: Функции — def

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/function_vs_copypaste.jpg" alt="Функция vs копипаст" width="90%"/>
</div>

> **Цель:** перестать копипастить код — писать функции  
> **Время:** ~1.5 часа

---

## Аналогия: рецепт борща

Вы варите борщ каждую неделю. Каждый раз писать рецепт заново?

Нет — вы записываете рецепт один раз, потом используете когда нужно.

**Функция = рецепт.** Написал один раз — использовал сколько угодно раз.

```python
def calculate_premium(age, base_rate, accidents):
    """Рассчитывает страховую премию."""
    premium = base_rate

    if age < 25:
        premium *= 1.5
    elif age > 60:
        premium *= 1.3

    if accidents > 0:
        premium *= (1 + accidents * 0.2)

    return round(premium, 2)

# Используем функцию много раз
print(calculate_premium(35, 12_000, 0))   # 12000.0
print(calculate_premium(22, 12_000, 1))   # 21600.0
print(calculate_premium(65, 12_000, 0))   # 15600.0
```

---

## Анатомия функции

```
def  имя_функции  (  параметры  ):
     ┌──────────────────────────┐
     │    тело функции          │  ← отступ 4 пробела
     │    (что делает)          │
     └──────────────────────────┘
     return  результат
```

---

## Параметры по умолчанию

```python
def get_policy_number(client_id, year=2024, prefix="POL"):
    return f"{prefix}-{year}-{client_id:05d}"

print(get_policy_number(42))              # POL-2024-00042
print(get_policy_number(7, prefix="КАСКО"))  # КАСКО-2024-00007
```

---

## Практика

```bash
python examples/01_first_function.py
python examples/02_premium_calculator.py
python examples/03_validation_functions.py
```

➡️ [Глава 07: Списки и словари](../07_lists_dicts/README.md)
