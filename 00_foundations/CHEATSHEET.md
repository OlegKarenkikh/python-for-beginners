# 🗂️ Python — шпаргалка одним листом

> Распечатайте и держите рядом с компьютером.

---

## Переменные и типы

```python
name   = "Ivanov A.P."     # str
age    = 35                 # int
rate   = 1.15               # float
active = True               # bool
empty  = None               # None

type(age)      # <class 'int'>
int("35")      # str -> int
str(35)        # int -> str
float("1.5")   # str -> float
```

---

## f-строки

```python
print(f"{name}")
print(f"{premium:.2f}")
print(f"{premium:,.0f}")
print(f"{rate:.1%}")
print(f"{n:05d}")
```

---

## Условия

```python
if age < 25:
    factor = 1.5
elif age > 60:
    factor = 1.3
else:
    factor = 1.0

# Тернарный
factor = 1.5 if age < 25 else 1.0
```

---

## Циклы

```python
for item in my_list:
    print(item)

for i, item in enumerate(my_list):
    print(i, item)

for i in range(10):        # 0..9
for i in range(1, 11):     # 1..10
for i in range(0, 10, 2):  # 0,2,4,6,8

while count > 0:
    count -= 1
```

---

## Функции

```python
def calculate(age, base=12_000):
    # docstring: Описание функции
    return base * 1.5 if age < 25 else base

result = calculate(22)
result = calculate(22, 15_000)
```

---

## Списки (list)

```python
items = [1, 2, 3]
items[0]           # 0-й элемент
items[-1]          # последний
items.append(4)    # добавить
items.remove(2)    # удалить значение 2
len(items)         # длина
sum(items)         # сумма
sorted(items)      # новый отсортированный
big = [x for x in items if x > 2]
```

---

## Словари (dict)

```python
d = {"name": "Ivanov", "age": 35}
d["name"]                  # получить
d.get("city", "—")         # с умолчанием
d["city"] = "Moscow"       # добавить/изменить
"name" in d                 # проверить ключ

for key, val in d.items():
    print(key, val)
```

---

## Файлы и JSON

```python
import json

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

---

## Операторы

| Арифметика | Сравнение | Логика |
|---|---|---|
| `+` `-` `*` `/` | `==` `!=` | `and` |
| `//` (целое) | `>` `<` | `or` |
| `%` (остаток) | `>=` `<=` | `not` |
| `**` (степень) | `in` `not in` | |

---

## Правила именования

```
переменные:  snake_case         client_name
константы:   UPPER_SNAKE_CASE   BASE_RATE
функции:     snake_case         calculate()
классы:      PascalCase         InsuranceClient
```

---

## Стиль (PEP 8)

- Отступ: **4 пробела** (не Tab)
- Пробел вокруг `=` и операторов
- 2 пустые строки между функциями
- Строки не длиннее **79 символов**

---

## Частые ошибки

| Ошибка | Причина |
|---|---|
| `SyntaxError` | Нет `:` или опечатка |
| `IndentationError` | Нет отступа |
| `NameError` | Переменная не создана |
| `TypeError` | Неверный тип, преобразуй `int(...)` |
| `KeyError` | Нет ключа, используй `.get()` |
| `IndexError` | Индекс вне списка |
