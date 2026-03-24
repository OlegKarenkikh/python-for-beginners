# ✂️ Глава 02: Второй взгляд — Строки как текстовый редактор

> Строки в Python — неизменяемые. Каждый метод возвращает НОВУЮ строку, не меняет старую.

---

## Главная ловушка строк

```python
name = "Иванов А.П."
name.upper()         # НЕ меняет name!
print(name)          # "Иванов А.П." — без изменений!

# ПРАВИЛЬНО — сохраняем результат
name_upper = name.upper()
# ИЛИ
name = name.upper()  # перезаписываем
```

---

## Строки из внешних источников — всегда очищайте

```python
# Данные из формы могут содержать лишние пробелы
raw_name = "  Иванов А.П.  "   # пробелы с обеих сторон
raw_name.strip()               # "Иванов А.П." — без пробелов

# Пример: пользователь ввёл ФИО с опечаткой в регистре
client_name = "  иванов а.п.  "
clean_name = client_name.strip().title()   # "Иванов А.П."

# Проверка перед сохранением в БД
def validate_name(name: str) -> str | None:
    clean = name.strip()
    if len(clean) < 2:
        return None   # слишком короткое
    return clean.title()

print(validate_name("  иван  "))  # "Иван"
print(validate_name("  "))        # None — пустое
```

---

## f-строки — единственный правильный способ форматирования

```python
name = "Иванов"
age  = 35
premium = 14_567.333

# Четыре способа — используйте только f-строки!
# 1. Конкатенация — плохо
msg = "Клиент " + name + ", возраст " + str(age)  # громоздко

# 2. % форматирование — устарело
msg = "Клиент %s, возраст %d" % (name, age)

# 3. .format() — многословно
msg = "Клиент {0}, возраст {1}".format(name, age)

# 4. f-строки — лучший способ ✓
msg = f"Клиент {name}, возраст {age} лет"

# Форматирование чисел в f-строках
print(f"Премия: {premium:,.2f} руб.")    # 14,567.33 руб.
print(f"Скидка: {0.15:.1%}")             # 15.0%
print(f"Номер: {42:05d}")                # 00042
```

---

## Разбор и сборка строк — split/join

```python
# Получили строку из формы: "BMW;X5;2022;Черный"
car_data = "BMW;X5;2022;Черный"
parts = car_data.split(";")   # ["BMW", "X5", "2022", "Черный"]

brand = parts[0]    # "BMW"
year  = int(parts[2])  # 2022

# Обратно
rebuilt = ";".join(parts)   # "BMW;X5;2022;Черный"

# Проверки
policy_number = "POL-2024-00042"
print(policy_number.startswith("POL"))  # True
print(policy_number.endswith("42"))     # True
print("2024" in policy_number)          # True
print(policy_number.count("-"))         # 2
```
