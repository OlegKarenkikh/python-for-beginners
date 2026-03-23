# ⚠️ Частые ошибки начинающих

---

## 1. IndentationError — неправильный отступ

```python
# ❌ Ошибка
if age < 25:
print("Молодой")  # нет отступа

# ✅ Правильно
if age < 25:
    print("Молодой")  # 4 пробела
```

---

## 2. NameError — переменная не определена

```python
# ❌ Ошибка
print(name)  # NameError: name 'name' is not defined

# ✅ Правильно
name = "Иванов"
print(name)
```

---

## 3. TypeError — неправильный тип

```python
# ❌ Ошибка
age = "35"
premium = 12000 * age  # TypeError: can't multiply str and int

# ✅ Правильно
age = 35          # int, не str!
premium = 12000 * age
```

---

## 4. KeyError — нет такого ключа в словаре

```python
client = {"name": "Иванов", "age": 35}

# ❌ Ошибка
print(client["city"])  # KeyError: 'city'

# ✅ Правильно
print(client.get("city", "не указан"))  # не указан
```

---

## 5. IndexError — выход за пределы списка

```python
premiums = [15000, 34000, 8500]

# ❌ Ошибка
print(premiums[5])  # IndexError: list index out of range

# ✅ Правильно — проверить длину
if len(premiums) > 5:
    print(premiums[5])
```

---

## 6. SyntaxError — опечатка в коде

```python
# ❌ Ошибка — забыли ":"
if age < 25
    print("Молодой")

# ✅ Правильно
if age < 25:
    print("Молодой")
```

---

## 7. ZeroDivisionError — деление на ноль

```python
# ❌ Ошибка
total = 100
count = 0
average = total / count  # ZeroDivisionError

# ✅ Правильно
average = total / count if count > 0 else 0
```
