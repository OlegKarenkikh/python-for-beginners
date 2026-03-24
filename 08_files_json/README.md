# 💾 Глава 08: Файлы и JSON

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/json_vs_dict.jpg" alt="JSON vs словарь Python" width="90%"/>
</div>

> **Цель:** читать и сохранять данные в файлы
> **Время:** ~1.5 часа

---

## Аналогия: блокнот для постоянных записей

Программа без файлов — как менеджер без блокнота.
Всё что запомнил — исчезнет когда он уйдёт домой.

Файл — это **постоянное хранилище**: закрыли программу, перезапустили, данные остались.

---

## with open — как открыть файл (и не забыть закрыть)

`with open(...)` — это как **взять ключ, открыть сейф, положить документ, закрыть сейф, вернуть ключ**.
Python делает закрытие автоматически — вы не забудете.

```python
# Запись — "w" = write (перезаписать файл)
with open("clients.txt", "w", encoding="utf-8") as f:
    f.write("Иванов А.П.\n")    # \n = перенос строки
    f.write("Петрова М.С.\n")
# ← файл АВТОМАТИЧЕСКИ закрыт когда вышли из блока with

# Чтение — "r" = read
with open("clients.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())   # strip() убирает \n в конце строки
```

> ⚠️ **Всегда указывайте `encoding="utf-8"`** если в файле есть кириллица!
> Без этого на Windows можно получить «кракозябры».

---


<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/with_open_files.jpg" alt="with open — ключ к файлу" width="90%"/></div>
## JSON — универсальный формат данных

JSON — это способ сохранить словарь или список Python **в файл**, а потом прочитать обратно.
Используется везде: API, базы данных, конфигурации, ответы от LLM.

```python
import json

# Словарь Python → JSON файл
client = {
    "name":    "Иванов А.П.",
    "age":     35,
    "premium": 14_400,
    "is_vip":  False
}

# json.dump — записать в файл
with open("client.json", "w", encoding="utf-8") as f:
    json.dump(client, f, ensure_ascii=False, indent=2)
    #                    ↑ чтобы кириллица не превратилась в \u041c...
    #                                        ↑ отступ 2 пробела — красиво

# json.load — прочитать из файла
with open("client.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)   # возвращает обычный словарь Python

print(loaded["name"])   # Иванов А.П.
print(type(loaded))     # <class 'dict'>
```

Что получится в файле `client.json`:
```json
{
  "name": "Иванов А.П.",
  "age": 35,
  "premium": 14400,
  "is_vip": false
}
```

> 💡 **Отличие JSON от dict:** в JSON строки — только двойные кавычки,
> `True/False` пишется как `true/false`, нет trailing comma.
> Python переводит автоматически.

---

## json.loads / json.dumps — для строк (не файлов)

```python
import json

# dumps — словарь → строка (например для отправки по API)
data = {"status": "approved", "amount": 14_400}
text = json.dumps(data, ensure_ascii=False)
print(text)    # '{"status": "approved", "amount": 14400}'
print(type(text))  # <class 'str'>

# loads — строка → словарь (например ответ от API)
response_text = '{"status": "ok", "claim_id": 42}'
result = json.loads(response_text)
print(result["claim_id"])   # 42
print(type(result))         # <class 'dict'>
```

---

## CSV — таблица в текстовом файле

```python
import csv

rows = [
    ["Иванов",  35, 14400],
    ["Петрова", 22, 21600],
]

# Запись
with open("premiums.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ФИО", "Возраст", "Премия"])  # заголовок
    writer.writerows(rows)                           # данные

# Чтение
with open("premiums.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)   # каждая строка — словарь
    for row in reader:
        print(f"{row['ФИО']}: {row['Премия']} руб.")
```

---

## Практика

```bash
python examples/01_read_write.py
python examples/02_json_operations.py
python examples/03_process_json_database.py
```

---

## 📌 После этой главы вы умеете:
- Читать и писать текстовые файлы через `with open`
- Сохранять словарь в JSON и загружать обратно (`dump`/`load`)
- Конвертировать строку ↔ словарь через `dumps`/`loads`
- Читать и писать CSV-таблицы

➡️ [Глава 09: Модули и pip](../09_modules_pip/README.md)
