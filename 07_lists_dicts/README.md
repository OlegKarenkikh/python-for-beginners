# 📋 Глава 07: Списки и словари

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/dict_as_form.jpg" alt="dict — электронная анкета" width="90%"/>
</div>

> **Цель:** хранить наборы данных, не по одному
> **Время:** ~2 часа

---

## list — список (папка с пронумерованными документами)

Представьте папку с документами. На каждом — номер **начиная с 0** (не с 1!).
Это называется «индекс».

```
Папка:  [ "POL-001",  "POL-002",  "POL-003" ]
Индекс:      0            1            2
```

> 💡 **Почему с 0?** Это наследие из языка C — компьютеры считают адреса памяти с нуля.
> Привыкнуть легко: первый элемент = `[0]`, второй = `[1]`, последний = `[-1]`.

```python
policies = ["POL-001", "POL-002", "POL-003"]

# Доступ по индексу
print(policies[0])    # POL-001 — первый
print(policies[1])    # POL-002 — второй
print(policies[2])    # POL-003 — третий (последний)
print(policies[-1])   # POL-003 — последний (удобный способ!)
print(policies[-2])   # POL-002 — предпоследний

# Добавить / удалить
policies.append("POL-004")      # добавить в конец
policies.remove("POL-002")      # удалить по значению
popped = policies.pop()         # вытащить и удалить последний
policies.insert(0, "POL-000")   # вставить на позицию 0

# Длина
print(len(policies))   # количество элементов
```

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/list_slicing.jpg" alt="Срезы списков" width="90%"/>
</div>

---


<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/list_indexing.jpg" alt="Индексы списка" width="90%"/></div>
## Срезы — взять кусок списка

```python
premiums = [15_200, 34_800, 8_500, 22_100, 19_600]
#   индекс:    0       1       2      3       4

# [начало : конец]  — конец НЕ включается!
print(premiums[1:3])    # [34800, 8500]  — с 1 по 2 включительно
print(premiums[:2])     # [15200, 34800] — первые два
print(premiums[2:])     # [8500, 22100, 19600] — с третьего до конца
print(premiums[::2])    # [15200, 8500, 19600] — каждый второй
print(premiums[::-1])   # обратный порядок
```

---

## dict — словарь (анкета с именованными полями)

Список хранит данные под номерами (0, 1, 2...).
Словарь — под **именами** (ключами). Как анкета с подписанными полями.

```python
client = {
    "name":    "Иванов А.П.",   # строковый ключ → строковое значение
    "age":     35,              # строковый ключ → числовое значение
    "car":     "Toyota Camry",
    "premium": 14_400,
    "is_vip":  False
}

# Получить значение по ключу
print(client["name"])              # Иванов А.П.
print(client.get("city", "—"))     # — (поля нет — вернёт "—", не ошибку)

# Изменить / добавить
client["premium"] = 15_000         # изменить существующее
client["city"]    = "Москва"       # добавить новое

# Проверить существование ключа
if "email" in client:
    print(client["email"])
else:
    print("Email не указан")

# Перебрать все поля
for key, value in client.items():
    print(f"  {key}: {value}")
```

---

## Список словарей — мини-база данных клиентов

Самая частая конструкция в реальных проектах:

```python
database = [
    {"id": 1, "name": "Иванов",  "premium": 14_400, "city": "Москва"},
    {"id": 2, "name": "Петрова", "premium": 21_600, "city": "СПб"},
    {"id": 3, "name": "Сидоров", "premium":  9_800, "city": "Москва"},
]

# Найти клиента по имени
def find_client(db, name):
    for client in db:
        if client["name"] == name:
            return client
    return None   # если не нашли

# Найти всех из Москвы
moscow_clients = [c for c in database if c["city"] == "Москва"]

# Посчитать суммарные сборы
total = sum(c["premium"] for c in database)
print(f"Итого сборов: {total:,} руб.")   # 45,800 руб.
```

---

## Практика

```bash
python examples/01_list_operations.py
python examples/02_client_database.py
python examples/03_data_analysis.py
```

---

## 📌 После этой главы вы умеете:
- Создать список и обращаться к элементам по индексу (в т.ч. `[-1]`)
- Брать срезы списка `[1:3]`
- Создать словарь и безопасно получать значения через `.get()`
- Строить «базу данных» как список словарей и искать в ней

➡️ [Глава 08: Файлы и JSON](../08_files_json/README.md)
