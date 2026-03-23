# 🗂️ Типы данных Python

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/data_types_overview.jpg" alt="4 основных типа данных" width="95%"/>
</div>

---

## Четыре основных типа

### str — строка (текст)

Любой текст, заключённый в кавычки.

```python
name     = "Иванов Алексей Петрович"   # двойные кавычки
city     = 'Москва'                     # одинарные — тоже можно
phone    = "+7 (495) 123-45-67"
policy   = "POL-2024-00042"
empty    = ""                           # пустая строка
```

**Когда использовать:** имена, адреса, номера, коды, любой текст.

---

### int — целое число

Число без дробной части.

```python
age         = 35
accidents   = 0
clients     = 1_248        # _ можно использовать как разделитель
year        = 2024
negative    = -5            # отрицательные тоже int
```

**Когда использовать:** возраст, количество, год, индексы.

---

### float — дробное число

Число с десятичной точкой (не запятой!).

```python
rate        = 0.038         # 3.8% годовых
premium     = 45_000.50     # рубли с копейками
coefficient = 1.15
pi          = 3.14159
```

**Когда использовать:** деньги, коэффициенты, проценты, ставки.  
⚠️ Разделитель — точка, не запятая: `1.5`, не `1,5`

---

### bool — логическое значение

Только два значения: `True` (истина) или `False` (ложь).

```python
is_vip          = True
has_accidents   = False
policy_active   = True
documents_ok    = False
```

**Когда использовать:** флаги, статусы, результаты проверок.  
⚠️ Первая буква заглавная: `True`, не `true`

---

## Как узнать тип переменной

```python
name = "Иванов"
age = 35
rate = 1.5
active = True

print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(rate))    # <class 'float'>
print(type(active))  # <class 'bool'>
```

---

## Преобразование типов

```python
# Пользователь вводит текст — нужно превратить в число
age_input = input("Введите возраст: ")   # "35" — это str!
age = int(age_input)                     # 35 — теперь int

# Число → строка
policy_number = "POL-" + str(42)         # "POL-42"

# Целое → дробное
discount = float(10) / 100              # 0.1
```

---

## Частые ошибки с типами

```python
# ❌ Нельзя складывать строку и число
age = "35"
result = age + 5     # TypeError!

# ✅ Нужно сначала преобразовать
age = int("35")
result = age + 5     # 40 ✓

# ❌ Запятая в числе — это не float!
rate = 1,15          # создаст кортеж (1, 15), не число!

# ✅ Точка — разделитель дробной части
rate = 1.15          # ✓
```

---

## Специальное значение None

`None` означает «ничего», «не задано», «пусто».

```python
result = None           # ещё нет значения

def find_client(name):
    # если не нашли — вернуть None
    return None

client = find_client("Иванов")
if client is None:
    print("Клиент не найден")
```
