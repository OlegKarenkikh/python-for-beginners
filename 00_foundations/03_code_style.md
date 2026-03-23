# 🎨 Стиль кода Python (PEP 8 — просто)

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/code_style_pep8.jpg" alt="Правила оформления кода PEP 8" width="95%"/>
</div>

> **PEP 8** — официальное руководство по стилю Python.
> Здесь только то, что нужно знать новичку.

---

## 1. Отступы: 4 пробела

Отступы обязательны после `if`, `for`, `while`, `def`, `class`.
**Всегда 4 пробела. Никаких табуляций.**

```python
# ✅ Правильно — 4 пробела
if age < 25:
    premium = base * 1.5
    print(premium)

# ❌ Неправильно — нет отступа
if age < 25:
premium = base * 1.5    # IndentationError!
```

---

## 2. Пробелы вокруг операторов

```python
# ✅ Правильно
age = 35
premium = base_rate * 1.5
is_valid = age >= 18 and age <= 80

# ❌ Неправильно
age=35
premium=base_rate*1.5
```

**Исключение:** параметры функций со значением по умолчанию — без пробелов:

```python
def calculate(age, rate=1.0):    # ✅ без пробелов у =
    ...
```

---

## 3. Пустые строки

```python
# ✅ 2 пустые строки между функциями верхнего уровня
def calculate_premium(age, base):
    return base * 1.5 if age < 25 else base


def validate_claim(amount, days):
    return amount > 0 and days <= 30


# ✅ 1 пустая строка внутри функции — между смысловыми блоками
def process_client(data):
    name = data["name"]
    age = data["age"]

    premium = calculate_premium(age, 12_000)

    return {"premium": premium}
```

---

## 4. Длина строки: максимум 79 символов

```python
# ❌ Слишком длинная строка
result = some_long_function(first_arg, second_arg, third_arg, fourth_arg)

# ✅ Разбить на несколько строк
result = some_long_function(
    first_arg,
    second_arg,
    third_arg,
    fourth_arg,
)
```

---

## 5. Комментарии

```python
# Однострочный комментарий — начинается с #

# ✅ Хороший — объясняет ПОЧЕМУ
# Молодые водители статистически аварийнее
if age < 25:
    factor = 1.5

# ❌ Плохой — объясняет ЧТО (и так видно)
age = 35   # присваиваем переменной age значение 35
```

---

## 6. Документация функции (docstring)

```python
def calculate_premium(age: int, base_rate: float) -> float:
    """
    Рассчитывает страховую премию.

    Args:
        age: возраст водителя в годах
        base_rate: базовая ставка в рублях

    Returns:
        Годовая страховая премия в рублях
    """
    factor = 1.5 if age < 25 else 1.0
    return round(base_rate * factor, 2)
```

---

## 7. Импорты — всегда вверху файла

```python
# Порядок: стандартная библиотека → сторонние → свои
import json
import os
from datetime import date

import requests          # сторонняя библиотека

from utils import calc   # свой модуль
```

---

## Автоформатирование (рекомендуется)

```bash
pip install black
black my_script.py    # исправит стиль автоматически
```
