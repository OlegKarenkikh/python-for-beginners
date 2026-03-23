# 🚨 Как читать сообщения об ошибках

---

## Структура сообщения об ошибке

```
Traceback (most recent call last):        ← след ошибки
  File "script.py", line 12, in <module>  ← где произошло
    premium = base_rate * age_str          ← строка кода
TypeError: can't multiply sequence by non-int of type 'str'
│          │
│          └── Объяснение что случилось
└── Тип ошибки — самое важное
```

**Читайте снизу вверх:** последняя строка — тип и причина ошибки.

---

## Частые ошибки и решения

### SyntaxError — опечатка в синтаксисе

```
SyntaxError: invalid syntax
```

```python
# Причина: забыли двоеточие
if age < 25      # ← нет ":"
    print("...")

# Исправление
if age < 25:
    print("...")
```

---

### IndentationError — неправильный отступ

```
IndentationError: expected an indented block
```

```python
# Причина: нет отступа после if/def/for
def calc(age):
return age * 1.5    # ← нет отступа

# Исправление
def calc(age):
    return age * 1.5
```

---

### NameError — переменная не определена

```
NameError: name 'premium' is not defined
```

```python
# Причина: опечатка в имени или не создали переменную
print(primeum)   # ← опечатка: primeum вместо premium

# Исправление
premium = 15_000
print(premium)
```

---

### TypeError — неправильный тип

```
TypeError: unsupported operand type(s) for *: 'int' and 'str'
```

```python
# Причина: пытаемся перемножить число и строку
age_input = input("Возраст: ")   # возвращает str!
result = 12_000 * age_input       # ошибка

# Исправление: преобразовать тип
age = int(input("Возраст: "))
result = 12_000 * age
```

---

### KeyError — нет такого ключа в словаре

```
KeyError: 'city'
```

```python
# Причина: обращаемся к несуществующему ключу
client = {"name": "Иванов", "age": 35}
print(client["city"])   # ← ключа "city" нет

# Исправление: использовать .get() с умолчанием
print(client.get("city", "не указан"))   # не указан
```

---

### IndexError — выход за пределы списка

```
IndexError: list index out of range
```

```python
# Причина: индекс больше длины списка
items = [1, 2, 3]
print(items[5])    # ← только 3 элемента (индексы 0,1,2)

# Исправление
if len(items) > 5:
    print(items[5])
```

---

### ZeroDivisionError — деление на ноль

```
ZeroDivisionError: division by zero
```

```python
# Исправление: проверять перед делением
count = 0
average = total / count if count > 0 else 0
```

---

### ValueError — неправильное значение

```
ValueError: invalid literal for int() with base 10: 'abc'
```

```python
# Причина: пытаемся преобразовать нечисловую строку в int
age = int("abc")   # ← "abc" — не число

# Исправление: обработать исключение
try:
    age = int(input("Возраст: "))
except ValueError:
    print("Пожалуйста, введите число")
    age = 0
```

---

## Алгоритм отладки

1. **Прочитайте последнюю строку** — тип ошибки
2. **Найдите строку кода** — `File "...", line N`
3. **Посмотрите на эту строку** в своём файле
4. **Проверьте типы** — `print(type(variable))`
5. **Добавьте print** перед проблемной строкой чтобы увидеть значения

```python
# Отладочный print
print(f"DEBUG: age={age}, type={type(age)}")
premium = base_rate * age    # ← где ошибка?
```
