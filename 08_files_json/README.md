# 💾 Глава 08: Файлы и JSON

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/dict_as_form.jpg" alt="JSON = электронная анкета" width="90%"/>
</div>

> **Цель:** читать и сохранять данные в файлы  
> **Время:** ~1.5 часа

---

## Аналогия: папка с документами

Программа без файлов — как менеджер без документов.  
Закрыли программу — все данные пропали.

Файлы — это постоянное хранилище.

---

## Читать и писать текстовый файл

```python
# Запись
with open("clients.txt", "w", encoding="utf-8") as f:
    f.write("Иванов А.П.\n")
    f.write("Петрова М.С.\n")

# Чтение
with open("clients.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

## JSON — универсальный формат данных

JSON — это способ хранить словари и списки в файле.  
Используется везде: API, базы данных, конфигурации.

```python
import json

# Словарь → JSON файл
client = {
    "name": "Иванов А.П.",
    "age": 35,
    "premium": 14_400,
    "is_vip": False
}

with open("client.json", "w", encoding="utf-8") as f:
    json.dump(client, f, ensure_ascii=False, indent=2)

# JSON файл → словарь
with open("client.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"])   # Иванов А.П.
```

---

## CSV — таблица в текстовом файле

```python
import csv

rows = [
    ["Иванов", 35, 14400],
    ["Петрова", 22, 21600],
]

with open("premiums.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ФИО", "Возраст", "Премия"])
    writer.writerows(rows)
```

---

## Практика

```bash
python examples/01_read_write.py
python examples/02_json_operations.py
python examples/03_process_json_database.py
```

➡️ [Глава 09: Модули и pip](../09_modules_pip/README.md)
