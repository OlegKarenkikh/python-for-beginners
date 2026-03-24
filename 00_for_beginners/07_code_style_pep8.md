# ✍️ Оформление кода Python — PEP 8 и отступы

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/pep8_rules.jpg" width="95%"/></div>

> Код без PEP 8 работает — но команда не сможет его читать. А через месяц — и вы сами.

---

## Почему оформление важно

```python
# ПЛОХО — никто не поймёт
def c(a,b,ac=0):
    p=b
    if a<25:p*=1.5
    elif a>60:p*=1.3
    if ac>0:p*=(1+ac*0.2)
    return round(p,2)

# ХОРОШО — PEP 8
def calculate_premium(age: int, base: float, accidents: int = 0) -> float:
    premium = base

    if age < 25:
        premium *= 1.5
    elif age > 60:
        premium *= 1.3

    if accidents > 0:
        premium *= (1 + accidents * 0.2)

    return round(premium, 2)
```

---

## Отступы — скелет Python-кода

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/indentation_visual.jpg" width="95%"/></div>

В Python нет фигурных скобок. Структуру задают **отступы** — ровно 4 пробела на каждый уровень.

```python
def process_claim(claim):         # уровень 0
    status = "unknown"            # уровень 1

    if claim["amount"] > 0:       # уровень 1
        if claim["approved"]:     # уровень 2
            status = "выплата"    # уровень 3
        else:
            status = "отказ"      # уровень 3

    return status                 # уровень 1
```

Типичные ошибки:

```python
# IndentationError: unexpected indent — лишний отступ
x = 5
    y = 10     # ошибка: откуда этот отступ?

# IndentationError: expected an indented block — пустое тело
if True:
pass           # тело if не может быть совсем пустым

# Правильно — используйте pass как заглушку
if True:
    pass

# TabError — нельзя смешивать табы и пробелы!
def foo():
	x = 1     # таб (→)
    y = 2     # пробелы — Python не поймёт
```

---

## Именование: snake_case

```python
# Python — snake_case (через подчёркивание)
client_name   = "Иванов"
base_rate     = 12_000
is_vip_client = True

# Классы — CamelCase
class InsuranceClient:
    pass

# Константы — UPPER_CASE
MAX_COVERAGE   = 5_000_000
MIN_CLIENT_AGE = 18
```

---

## Пробелы вокруг операторов

```python
# ПЛОХО
x=a*b+c
if age<25 and accidents>0:

# ХОРОШО
x = a * b + c
if age < 25 and accidents > 0:

# Исключение: аргументы функций — без пробелов при =
def calc(age, base=12000):    # OK
    pass

calc(age=35, base=15000)      # OK
```

---

## Длинные строки — как переносить

```python
# ПЛОХО — одна длинная строка
result = calculate_premium(age=client_age, base=base_rate, accidents=total_accidents_count)

# ХОРОШО — переносим внутри скобок
result = calculate_premium(
    age=client_age,
    base=base_rate,
    accidents=total_accidents_count
)

# Длинное условие
is_valid = (
    age >= 18
    and age <= 75
    and experience >= 1
)

# Длинный словарь
client = {
    "name":    "Иванов А.П.",
    "age":     35,
    "premium": 12_000,
}
```

---

## Инструменты автоформатирования

Не нужно помнить все правила — инструменты сделают это за вас:

| Инструмент | Что делает | Команда |
|---|---|---|
| `black` | Форматирует код автоматически | `black my_file.py` |
| `ruff` | Проверяет стиль и ошибки | `ruff check .` |
| `isort` | Сортирует импорты | `isort my_file.py` |

```bash
pip install black ruff
black 04_conditions/examples/risk_calculator.py
ruff check .
```

VS Code: расширение **Python** от Microsoft → форматирование по Ctrl+S автоматически.

---

## Docstring — документация функции

```python
def calculate_premium(age: int, base: float, accidents: int = 0) -> float:
    """Рассчитывает страховую премию по базовым правилам.

    Args:
        age:       Возраст водителя (лет)
        base:      Базовая ставка (руб.)
        accidents: Количество аварий за 3 года

    Returns:
        Итоговая премия в рублях
    """
    premium = base
    if age < 25:
        premium *= 1.5
    if accidents > 0:
        premium *= (1 + accidents * 0.2)
    return round(premium, 2)
```

---

## Правило одного: хороший код читается как текст

```python
# Плохо: непонятные имена
def f(a, b, c):
    return a * b * (1 + c * 0.2)

# Хорошо: код говорит сам за себя
def apply_accident_surcharge(base_premium, risk_factor, accidents_count):
    surcharge_per_accident = 0.2
    total_surcharge = accidents_count * surcharge_per_accident
    return base_premium * risk_factor * (1 + total_surcharge)
```
