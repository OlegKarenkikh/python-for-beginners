# 🔑 Ключевые слова Python

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/python_keywords.jpg" alt="Ключевые слова Python" width="95%"/>
</div>

---

> Ключевые слова — **зарезервированные** слова Python.
> **Нельзя** использовать их как имена переменных, функций или файлов.

---

## Управление потоком

| Слово | Что делает | Пример |
|---|---|---|
| `if` | Условие | `if age < 25:` |
| `elif` | Иначе если | `elif age > 60:` |
| `else` | Иначе | `else:` |
| `for` | Цикл перебора | `for item in list:` |
| `while` | Цикл пока | `while count > 0:` |
| `break` | Выйти из цикла | `break` |
| `continue` | Перейти к следующей итерации | `continue` |
| `pass` | Ничего не делать (заглушка) | `pass` |

---

## Функции и классы

| Слово | Что делает | Пример |
|---|---|---|
| `def` | Определить функцию | `def calculate():` |
| `return` | Вернуть значение из функции | `return premium` |
| `class` | Определить класс | `class Client:` |
| `lambda` | Анонимная функция | `f = lambda x: x * 2` |

---

## Значения и логика

| Слово | Что делает | Пример |
|---|---|---|
| `True` | Истина | `is_vip = True` |
| `False` | Ложь | `active = False` |
| `None` | Ничего / не задано | `result = None` |
| `and` | Логическое И | `a and b` |
| `or` | Логическое ИЛИ | `a or b` |
| `not` | Логическое НЕ | `not active` |
| `in` | Принадлежность | `x in list` |
| `is` | Тождественность | `x is None` |

---

## Импорт

| Слово | Пример |
|---|---|
| `import` | `import json` |
| `from` | `from datetime import date` |
| `as` | `import numpy as np` |

---

## Исключения

| Слово | Что делает |
|---|---|
| `try` | Попробовать выполнить |
| `except` | Обработать ошибку |
| `finally` | Выполнить в любом случае |
| `raise` | Вызвать ошибку |
| `with` | Контекстный менеджер (напр. для файлов) |

```python
try:
    age = int(input("Введите возраст: "))
except ValueError:
    print("Нужно ввести число!")
```

---

## Полный список (35 слов)

```
False    None     True     and      as       assert
async    await    break    class    continue def
del      elif     else     except   finally  for
from     global   if       import   in       is
lambda   nonlocal not      or       pass     raise
return   try      while    with     yield
```

Редактор подсветит их **жирным или цветом** — вы сразу увидите что это зарезервированное слово.
