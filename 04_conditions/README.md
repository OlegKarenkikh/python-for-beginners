# 🔀 Глава 04: Условия — if, elif, else

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/conditions_flow.jpg" alt="Условия if/elif/else" width="90%"/>
</div>

> **Цель:** научить программу «принимать решения»  
> **Время:** ~1.5 часа

---

## Аналогия: дорожная развилка

Если возраст водителя < 25 лет — дорого.  
Иначе если стаж > 10 лет — скидка.  
Иначе — стандартная ставка.

```python
age = 23

if age < 25:
    print("Молодой водитель — коэффициент 1.5")
elif age > 60:
    print("Водитель 60+ — коэффициент 1.3")
else:
    print("Стандартный коэффициент 1.0")
```

**Важно:** отступы (4 пробела) — обязательны!

---

## Страховой пример: расчёт коэффициента риска

```python
def get_risk_factor(age, experience, accidents):
    risk = 1.0

    # По возрасту
    if age < 25:
        risk *= 1.5
    elif age > 70:
        risk *= 1.3

    # По стажу
    if experience < 2:
        risk *= 1.4
    elif experience > 10:
        risk *= 0.85

    # По авариям
    if accidents == 0:
        risk *= 0.9       # бонус за безаварийность
    elif accidents == 1:
        risk *= 1.2
    else:
        risk *= (1 + accidents * 0.25)

    return round(risk, 2)

print(get_risk_factor(35, 8, 0))   # 0.85
print(get_risk_factor(22, 1, 1))   # 2.52
```

---

## Операторы сравнения

| Оператор | Смысл | Пример |
|---|---|---|
| `==` | равно | `age == 25` |
| `!=` | не равно | `city != "Москва"` |
| `>` | больше | `premium > 50000` |
| `<` | меньше | `accidents < 3` |
| `>=` | больше или равно | `experience >= 5` |
| `and` | и то и другое | `age > 18 and age < 65` |
| `or` | хотя бы одно | `city == "Москва" or city == "СПб"` |
| `not` | отрицание | `not is_vip` |

---

## Практика

```bash
python examples/01_simple_if.py
python examples/02_risk_calculator.py
python examples/03_claim_checker.py
```

---

## 📌 После этой главы вы умеете:
- Написать `if / elif / else` для принятия решений
- Строить условия с `and`, `or`, `not`
- Объяснить почему порядок `elif` важен
- Реализовать расчёт коэффициента риска с несколькими условиями

➡️ [Глава 05: Циклы](../05_loops/README.md)
