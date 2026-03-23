# 📋 Глава 07: Списки и словари

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/dict_as_form.jpg" alt="dict — электронная анкета" width="90%"/>
</div>

> **Цель:** хранить наборы данных, не по одному  
> **Время:** ~2 часа

---

## list — список (папка с документами)

```python
# list — упорядоченный набор элементов
policies = ["POL-001", "POL-002", "POL-003"]
premiums = [15_200, 34_800, 8_500]

# Доступ по индексу (счёт с 0!)
print(policies[0])      # POL-001
print(policies[-1])     # POL-003 (последний)

# Добавить / удалить
policies.append("POL-004")
policies.remove("POL-002")

# Длина
print(len(policies))    # 3
```

---

## dict — словарь (анкета с полями)

```python
client = {
    "name": "Иванов А.П.",
    "age": 35,
    "car": "Toyota Camry",
    "premium": 14_400,
    "is_vip": False
}

# Получить значение
print(client["name"])           # Иванов А.П.
print(client.get("city", "—"))  # — (нет такого поля)

# Изменить
client["premium"] = 15_000
client["city"] = "Москва"       # добавить новое поле

# Перебрать
for key, value in client.items():
    print(f"  {key}: {value}")
```

---

## Список словарей — база данных клиентов

```python
database = [
    {"id": 1, "name": "Иванов", "premium": 14_400},
    {"id": 2, "name": "Петрова", "premium": 21_600},
    {"id": 3, "name": "Сидоров", "premium": 9_800},
]

# Найти клиента
def find_client(db, name):
    for client in db:
        if client["name"] == name:
            return client
    return None

result = find_client(database, "Петрова")
print(result)
```

---

## Практика

```bash
python examples/01_list_operations.py
python examples/02_client_database.py
python examples/03_data_analysis.py
```

➡️ [Глава 08: Файлы и JSON](../08_files_json/README.md)
