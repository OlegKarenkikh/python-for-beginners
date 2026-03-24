# ✂️ Глава 02: Строки — неизменяемость, форматирование и ловушки

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/string_immutable.jpg" width="95%"/></div>

---

## Главный закон строк: они НЕИЗМЕНЯЕМЫ

Строка в Python — как высеченная в камне надпись.
Нельзя исправить букву — можно только создать новую надпись.

```python
name = "Иванов А.П."

# Все методы возвращают НОВУЮ строку
name.upper()     # "ИВАНОВ А.П." — создана новая, но НЕ сохранена
name.strip()     # "Иванов А.П." — тоже просто создана и выброшена

print(name)      # "Иванов А.П." — СТАРАЯ строка не изменилась!

# ПРАВИЛЬНО: сохраняем результат
name = name.strip().title()   # перезаписываем в ту же переменную
```

Почему Python сделал строки неизменяемыми?
- Безопасность: несколько переменных могут ссылаться на одну строку — никто не испортит данные другому
- Производительность: одинаковые строки кэшируются в памяти
- Ключи словаря: строки подходят как ключи dict именно потому, что не меняются

---

## Что ещё неизменяемо в Python?

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/mutable_immutable.jpg" width="95%"/></div>

| Тип | Изменяемый? | Создание | Пример |
|---|---|---|---|
| `str` | Нет | `"текст"` | `"Иванов"` |
| `int` | Нет | `42` | возраст, счётчик |
| `float` | Нет | `1.5` | коэффициент |
| `bool` | Нет | `True/False` | флаг |
| `tuple` | Нет | `(a, b)` | координаты ДТП |
| `frozenset` | Нет | `frozenset({1,2})` | набор городов |
| `list` | Да | `[a, b]` | список заявлений |
| `dict` | Да | `{"k": v}` | данные клиента |
| `set` | Да | `{1, 2, 3}` | уникальные ID |

---

## Tuple — неизменяемый список

```python
# Tuple создаётся скобками (или просто запятыми)
coords = (55.75, 37.62)   # широта, долгота места ДТП

# Нельзя изменить элемент
# coords[0] = 56.0   # TypeError: 'tuple' object does not support item assignment

# Зачем нужен tuple?

# 1. Защита данных от случайного изменения
RISK_THRESHOLDS = (0, 1, 3, 5)   # границы коэффициентов — не менять!

# 2. Ключ словаря — список нельзя, tuple можно
accident_locations = {
    (55.75, 37.62): "ДТП у Кремля",
    (59.93, 30.31): "ДТП в Петербурге",
}

# 3. Возврат нескольких значений из функции
def get_risk_range(age):
    if age < 25:
        return 1.3, 2.0   # Python упаковывает в tuple автоматически
    return 0.8, 1.2

low, high = get_risk_range(22)   # распаковка
print(f"Коэффициент от {low} до {high}")

# ВНИМАНИЕ: один элемент требует запятую!
single    = (42,)   # tuple с одним числом
not_tuple = (42)    # просто число в скобках — НЕ tuple!
print(type(single))    # <class 'tuple'>
print(type(not_tuple)) # <class 'int'>
```

---

## frozenset — неизменяемое множество

```python
# frozenset — уникальные значения, но нельзя изменить
HIGH_RISK_CITIES = frozenset({"Москва", "СПб", "Казань"})
FORBIDDEN_BRANDS = frozenset({"Lada Kalina 2004", "ВАЗ-2101"})

city = "Москва"
if city in HIGH_RISK_CITIES:   # O(1) — мгновенная проверка
    risk_coeff *= 1.15

car = "BMW X5"
if car not in FORBIDDEN_BRANDS:
    print("Автомобиль принят на страхование")

# Нельзя изменить — защита от ошибок
# HIGH_RISK_CITIES.add("Новосибирск")  # AttributeError!

# Обычный set можно менять
allowed_cities = {"Москва", "СПб"}
allowed_cities.add("Казань")    # OK
```

---

## Форматирование кода: PEP 8

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/pep8_rules.jpg" width="95%"/></div>

PEP 8 — официальный стандарт оформления Python-кода. Это не просто красота — читаемость и меньше ошибок.

```python
# ПЛОХО — не по PEP 8
def calculatePremium(age,base,accidents=0):
    p=base
    if age<25:p*=1.5
    elif age>60:p*=1.3
    return round(p,2)

# ХОРОШО — PEP 8
def calculate_premium(age: int, base: float, accidents: int = 0) -> float:
    premium = base

    if age < 25:
        premium *= 1.5
    elif age > 60:
        premium *= 1.3

    return round(premium, 2)
```

Ключевые правила:
- Имена переменных и функций: `snake_case` (через нижнее подчёркивание)
- Отступы: строго 4 пробела — никогда табы!
- Пробелы вокруг операторов: `x = a * b + c`, не `x=a*b+c`
- Пустые строки: 2 строки между функциями верхнего уровня
- Длина строки: не более 88 символов

---

## Отступы — скелет кода

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/indentation_visual.jpg" width="95%"/></div>

```python
def process_claim(claim):       # уровень 0
    if claim["amount"] > 0:     # уровень 1 (4 пробела)
        if claim["approved"]:   # уровень 2 (8 пробелов)
            return "выплата"    # уровень 3 (12 пробелов)
        else:
            return "отказ"
    return "нет данных"

# Типичные ошибки:
# IndentationError: unexpected indent     — лишний отступ
# IndentationError: expected an indented block — забыли тело if/def
# TabError: inconsistent use of tabs and spaces — смешали таб и пробелы
```

Настройте редактор:
- VS Code: Ctrl+Shift+P → "Convert Indentation to Spaces" → размер 4
- PyCharm: Settings → Editor → Code Style → Python → Indent size = 4

---

## f-строки: полная шпаргалка

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/fstring_cheatsheet.jpg" width="95%"/></div>

```python
premium  = 14567.333
discount = 0.157
policy_n = 42
city     = "Москва"

# Числа
print(f"{premium:.2f}")        # 14567.33
print(f"{premium:,.0f}")       # 14,567          — тысячи, без дробной части
print(f"{premium:,.2f}")       # 14,567.33

# Проценты
print(f"{discount:.0%}")       # 16%
print(f"{discount:.1%}")       # 15.7%

# Заполнение нулями
print(f"POL-{policy_n:05d}")   # POL-00042

# Выравнивание
print(f"{city:<15}|")          # "Москва         |"  левое
print(f"{city:>15}|")          # "         Москва|"  правое
print(f"{city:^15}|")          # "    Москва     |"  по центру

# Выражения внутри f-строки
name = "иванов"
print(f"{name.title()} — 22 лет")
print(f"Надбавка: {0.2 * premium:,.0f}")

# Словарь внутри f-строки (одинарные кавычки внутри!)
client = {"name": "Иванов", "city": "Москва"}
print(f"{client['name']} из {client['city']}")
```

---

## Полезные методы строк

```python
s = "  Иванов Алексей Петрович  "

# Очистка и регистр
s.strip()              # "Иванов Алексей Петрович"
s.lower()              # "  иванов алексей петрович  "
s.upper()              # "  ИВАНОВ АЛЕКСЕЙ ПЕТРОВИЧ  "
s.title()              # "  Иванов Алексей Петрович  "
s.replace("А", "а")   # заменить всё

# Разбиение и сборка
"BMW;X5;2022".split(";")          # ["BMW", "X5", "2022"]
" ".join(["Иванов", "Алексей"])   # "Иванов Алексей"

# Проверки
"POL-2024-001".startswith("POL")  # True
"clients.json".endswith(".json")  # True
"2024" in "POL-2024-001"          # True
"POL-2024-001".count("-")         # 2
"POL-2024-001".find("2024")       # 4  (позиция или -1 если нет)

"12345".isdigit()                 # True
"Иванов".isalpha()                # True
```

---

## Практические упражнения

1. Очистите и нормализуйте список имён:
   `["  иванов  ", "ПЕТРОВА", " сидоров К.Д."]` → `["Иванов", "Петрова", "Сидоров К.Д."]`

2. Разберите строку автомобиля в словарь:
   `"BMW;X5;2022;Черный;55000"` → `{"brand": "BMW", "model": "X5", ...}`

3. Напишите функцию `format_policy(n: int) -> str` → `"POL-2026-00042"`

4. Создайте f-строку отчёта: имя клиента, возраст, премия с разделителем тысяч

5. Создайте frozenset городов повышенного риска и проверьте по нему 5 городов


---

## ❓ Вопросы которые возникают при изучении

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/qa_strings.png" alt="Вопросы о строках" width="95%"/>
</div>

---

### 🙋 Что если внутри строки нужна двойная кавычка?

Три способа — выбирайте самый читаемый:

```python
# 1. Одинарные кавычки снаружи
text = 'Клиент сказал "Одобрено"'            # ✅ самый простой

# 2. Экранирование обратным слешем
text = "Клиент сказал \"Одобрено\""          # ✅ работает

# 3. Тройные кавычки — для длинных текстов
text = \"\"\"Клиент сказал "Одобрено" и ушёл\"\"\""""      # ✅ удобно для многострочного
```

---

### 🙋 Что будет если несколько пробелов подряд при `split()`?

`split()` без аргументов — умный: игнорирует любое количество пробелов.
`split(" ")` с явным пробелом — тупой: оставляет пустые строки.

```python
name = "  Иванов   Алексей  "

name.split()       # ✅ ['Иванов', 'Алексей']  — правильно
name.split(" ")    # ❌ ['', '', 'Иванов', '', '', 'Алексей', '', '']  — мусор!
```

**Правило:** используйте `split()` без аргументов для текста с пробелами.

---

### 🙋 Можно ли цепочкой: `name.split()[0]`?

Да! Это «цепочка методов» — очень распространённый паттерн.

```python
name = "  иванов алексей петрович  "

# Каждый метод берёт результат предыдущего:
result = name.strip().title().split()[0]
#   strip()  → "иванов алексей петрович"
#   title()  → "Иванов Алексей Петрович"
#   split()  → ["Иванов", "Алексей", "Петрович"]
#   [0]      → "Иванов"

print(result)   # Иванов
```

---

### 🙋 Почему `name.upper()` не сохраняется само?

Строки **неизменяемы** — методы возвращают новую строку, но не меняют старую.
Результат нужно явно сохранить:

```python
name = "иванов"
name.upper()           # ⚠️ создаёт новую строку, но никуда не кладёт
print(name)            # иванов — ничего не изменилось!

name = name.upper()    # ✅ сохраняем результат
print(name)            # ИВАНОВ
```

> 💡 **Правило:** у строк нет методов которые меняют строку «на месте». Всегда сохраняйте результат.

---

### 🙋 `name = name.strip()` — это изменение строки или новая?

Новая строка! Правая часть `name.strip()` создаёт новую строку.
Потом `name =` делает так, что имя `name` указывает на новую строку.
Старая строка удаляется автоматически (сборщик мусора Python).

Технически переменная — это «ярлык». Вы переклеиваете ярлык на новый объект.
