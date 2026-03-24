# 📋 Списки, массивы и JSON — подробный разбор

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/list_slicing.jpg" alt="Список: индексация и срезы" width="95%"/>
</div>

---

## Часть 1: Списки (list) — элементарные операции

### Создание

```python
# Пустой список
clients = []

# Список сразу с данными
names = ["Иванов", "Петрова", "Сидоров", "Орлова", "Козлов"]
ages  = [35, 22, 47, 31, 60]
premiums = [12_000, 18_000, 12_000, 14_400, 15_600]
```

---

### Обращение к элементам (индексация)

```python
names = ["Иванов", "Петрова", "Сидоров", "Орлова", "Козлов"]

# Положительные индексы — с начала (с 0)
print(names[0])   # Иванов   ← первый
print(names[1])   # Петрова
print(names[4])   # Козлов   ← последний через прямой индекс

# Отрицательные индексы — с конца
print(names[-1])  # Козлов   ← последний
print(names[-2])  # Орлова
print(names[-5])  # Иванов   ← первый через отрицательный
```

---

### Срезы (slicing)

```python
names = ["Иванов", "Петрова", "Сидоров", "Орлова", "Козлов"]
#         0          1          2          3          4

# names[от:до]  — элементы от (включительно) до (не включая)
print(names[1:3])   # ["Петрова", "Сидоров"]   — индексы 1 и 2
print(names[:2])    # ["Иванов", "Петрова"]     — первые два
print(names[2:])    # ["Сидоров", "Орлова", "Козлов"] — с 3-го
print(names[:])     # все элементы (копия)
print(names[::2])   # ["Иванов", "Сидоров", "Козлов"] — каждый второй
print(names[::-1])  # ["Козлов", "Орлова", "Сидоров", "Петрова", "Иванов"] — в обратном порядке
```

---

### Изменение и добавление

```python
clients = ["Иванов", "Петрова", "Сидоров"]

clients.append("Козлов")          # добавить в конец
clients.insert(1, "Алексеев")     # вставить на позицию 1
clients[0] = "Иванов А.П."        # изменить элемент

print(clients)
# ["Иванов А.П.", "Алексеев", "Петрова", "Сидоров", "Козлов"]
```

---

### Удаление

```python
clients = ["Иванов", "Петрова", "Сидоров", "Орлова"]

clients.remove("Петрова")   # удалить по значению (первое вхождение)
del clients[0]              # удалить по индексу
last = clients.pop()        # удалить и вернуть последний
first = clients.pop(0)      # удалить и вернуть первый

print(clients)   # ["Сидоров"]
```

---

### Поиск и проверка

```python
names = ["Иванов", "Петрова", "Сидоров"]

print("Иванов" in names)       # True
print("Козлов" in names)       # False
print("Козлов" not in names)   # True

print(names.index("Петрова"))  # 1  — позиция (ошибка если нет!)
print(names.count("Иванов"))   # 1  — сколько раз встречается
```

---

### Полезные функции

```python
premiums = [18_000, 12_000, 45_000, 14_400, 15_600]

print(len(premiums))      # 5      — количество элементов
print(sum(premiums))      # 105000 — сумма
print(min(premiums))      # 12000  — минимум
print(max(premiums))      # 45000  — максимум
print(sorted(premiums))   # [12000, 14400, 15600, 18000, 45000] — новый сортированный
premiums.sort()           # сортировка на месте (изменяет исходный список)
premiums.sort(reverse=True) # по убыванию
```

---

### List comprehension — мощный инструмент

```python
ages = [35, 22, 47, 19, 31, 24, 60]

# Получить всех молодых (< 25)
young = [age for age in ages if age < 25]
# [22, 19, 24]

# Применить формулу ко всем
premiums = [12_000 * 1.5 if a < 25 else 12_000 for a in ages]
# [12000, 18000, 12000, 18000, 12000, 18000, 12000]

# Работа со списком словарей
clients = [
    {"name": "Иванов", "age": 35},
    {"name": "Петрова", "age": 22},
    {"name": "Сидоров", "age": 47},
]
young_clients = [c["name"] for c in clients if c["age"] < 30]
# ["Петрова"]
```

---

## Часть 2: Словари (dict) — продвинутые операции

### Создание и основы

```python
# Способ 1: фигурные скобки
client = {
    "name":       "Иванов Алексей Петрович",
    "age":        35,
    "is_vip":     False,
    "city":       "Москва",
    "accidents":  0,
    "premium":    12_000.0,
}

# Способ 2: из двух списков (zip)
keys   = ["name", "age", "city"]
values = ["Иванов", 35, "Москва"]
client = dict(zip(keys, values))
```

---

### Чтение значений

```python
client = {"name": "Иванов", "age": 35, "city": "Москва"}

# Напрямую — KeyError если ключа нет
print(client["name"])        # Иванов

# Через .get() — безопасно, возвращает None или умолчание
print(client.get("city"))            # Москва
print(client.get("phone"))           # None
print(client.get("phone", "—"))      # — (умолчание)
```

---

### Перебор словаря

```python
client = {"name": "Иванов", "age": 35, "city": "Москва"}

# Только ключи
for key in client:
    print(key)              # name, age, city

# Ключи и значения
for key, value in client.items():
    print(f"{key}: {value}")

# Только значения
for value in client.values():
    print(value)
```

---

### Список словарей — база данных клиентов

```python
clients = [
    {"id": 1, "name": "Иванов А.П.",  "age": 35, "accidents": 0},
    {"id": 2, "name": "Петрова М.С.", "age": 22, "accidents": 1},
    {"id": 3, "name": "Сидоров К.Д.", "age": 47, "accidents": 0},
]

# Найти клиента по id
def find_client(clients, client_id):
    for c in clients:
        if c["id"] == client_id:
            return c
    return None

found = find_client(clients, 2)
print(found["name"])   # Петрова М.С.

# Фильтрация
vip_age = [c for c in clients if c["age"] < 25 or c["accidents"] == 0]

# Сортировка по возрасту
sorted_clients = sorted(clients, key=lambda c: c["age"])

# Сортировка по имени
sorted_clients = sorted(clients, key=lambda c: c["name"])
```

---

### Вложенные словари

```python
policy = {
    "number":   "POL-2024-00042",
    "client": {
        "name":   "Иванов А.П.",
        "age":    35,
        "docs": {
            "passport": "4521 987654",
            "driver_license": "77АА 123456",
        }
    },
    "coverage": {
        "type":      "КАСКО",
        "amount":    1_500_000,
        "franchise": 30_000,
    },
    "premium": 45_000,
}

# Доступ к вложенным данным
name     = policy["client"]["name"]           # Иванов А.П.
passport = policy["client"]["docs"]["passport"] # 4521 987654
coverage = policy["coverage"]["amount"]       # 1500000

# Безопасный доступ через .get()
phone = policy.get("client", {}).get("phone", "не указан")
```

---

## Часть 3: JSON — полный разбор

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/json_vs_dict.jpg" alt="JSON vs Python dict" width="95%"/>
</div>

### Что такое JSON

JSON (JavaScript Object Notation) — формат хранения и передачи данных.  
В Python JSON ↔ dict (словарь). Работа через модуль `json`.

```python
# JSON в тексте выглядит так:
json_text = '''
{
  "name": "Иванов А.П.",
  "age": 35,
  "is_vip": false,
  "premium": 12000.0,
  "documents": ["паспорт", "права"],
  "address": {
    "city": "Москва",
    "street": "Ленина 42"
  }
}
'''
```

**Отличия JSON от Python:**
| Python | JSON |
|---|---|
| `True` / `False` | `true` / `false` |
| `None` | `null` |
| одинарные кавычки `'` | только двойные `"` |
| кортеж `(1,2)` | массив `[1,2]` |

---

### Чтение JSON (строка → dict)

```python
import json

json_text = '{"name": "Иванов", "age": 35, "active": true}'

client = json.loads(json_text)   # loads = load from String
print(client["name"])            # Иванов
print(type(client))              # <class 'dict'>
```

---

### Запись JSON (dict → строка)

```python
import json

client = {"name": "Иванов", "age": 35, "active": True}

# Компактно
compact = json.dumps(client)
# '{"name": "Иванов", "age": 35, "active": true}'

# Красиво с отступами
pretty = json.dumps(client, ensure_ascii=False, indent=2)
print(pretty)
# {
#   "name": "Иванов",
#   "age": 35,
#   "active": true
# }
```

---

### Чтение из файла

```python
import json

with open("clients.json", "r", encoding="utf-8") as f:
    clients = json.load(f)    # load = load from File

# Теперь clients — это список словарей
for client in clients:
    print(client["name"], client["age"])
```

---

### Запись в файл

```python
import json

clients = [
    {"name": "Иванов А.П.", "age": 35, "premium": 12_000},
    {"name": "Петрова М.С.", "age": 22, "premium": 18_000},
]

with open("clients.json", "w", encoding="utf-8") as f:
    json.dump(clients, f, ensure_ascii=False, indent=2)
```

Результат `clients.json`:
```json
[
  {
    "name": "Иванов А.П.",
    "age": 35,
    "premium": 12000
  },
  {
    "name": "Петрова М.С.",
    "age": 22,
    "premium": 18000
  }
]
```

---

### Практика: обработка JSON-ответа от API

```python
import json, requests

# Допустим, наш FastAPI вернул такой ответ:
response_text = '''
{
  "status": "ok",
  "client_id": 42,
  "result": {
    "premium": 18000.0,
    "risk_level": "medium",
    "notes": ["молодой водитель", "опыт < 3 лет"]
  }
}
'''

data = json.loads(response_text)

# Извлекаем данные
status    = data["status"]
premium   = data["result"]["premium"]
notes     = data["result"]["notes"]
risk      = data["result"]["risk_level"]

print(f"Статус: {status}")
print(f"Премия: {premium:,.0f} руб.")
print(f"Риск: {risk}")
print("Примечания:")
for note in notes:
    print(f"  — {note}")
```

---

### Упражнения

**Задание 1:** Дан список клиентов — выведите только тех, у кого премия > 15 000 руб.
```python
clients = [
    {"name": "Иванов", "age": 35, "premium": 12_000},
    {"name": "Петрова", "age": 22, "premium": 18_000},
    {"name": "Сидоров", "age": 47, "premium": 14_400},
    {"name": "Орлова",  "age": 31, "premium": 45_000},
]
# Ваш код здесь
```

**Задание 2:** Прочитайте `clients.json` и посчитайте среднюю премию по всем клиентам.

**Задание 3:** Создайте словарь из двух списков `names` и `ages` и запишите его в файл `output.json`.
