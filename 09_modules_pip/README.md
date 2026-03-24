# 📦 Глава 09: Модули и pip

> **Цель:** использовать готовые библиотеки, не писать всё с нуля
> **Время:** ~1 час

---

## Что такое модуль?

Модуль — это файл с готовым кодом, который кто-то написал за вас.

```python
import json        # работа с JSON
import os          # файловая система
import statistics  # статистика
import datetime    # даты и время
import csv         # CSV-файлы
```

---

## Стандартная библиотека Python

```python
from datetime import date

today = date.today()
print(f"Дата полиса: {today}")           # 2024-03-23
print(f"Год: {today.year}")

# Срок действия полиса (1 год)
from datetime import timedelta
expiry = today + timedelta(days=365)
print(f"Истекает: {expiry}")
```

---

## pip: установка внешних библиотек

```bash
pip install requests    # HTTP-запросы
pip install pandas      # анализ данных
pip install openpyxl    # Excel-файлы
```

После установки:

```python
import requests
response = requests.get("https://api.example.com/rates")
data = response.json()
print(data)
```

---

## requirements.txt

```txt
requests>=2.31.0
openpyxl>=3.1.0
```

Установка всех зависимостей:
```bash
pip install -r requirements.txt
```

---

## Практика

```bash
python examples/01_stdlib_modules.py
python examples/02_dates_and_policies.py
```

➡️ [Финальный проект →](../10_final_project/README.md)


---

## 🔗 Связь с FastAPI и агентами

Модули — это не изолированный инструмент. Каждая следующая глава строится на них:

| Модуль | Используется в |
|---|---|
| `json` | Гл. 08, 12, 13 — данные из файлов и от LLM |
| `datetime` | Гл. 08, 11 — даты полисов в API |
| `os` | Гл. 08, 20 — пути, переменные окружения |
| `re` | Гл. 13 — извлечение JSON из ответов LLM |
| `requests` | Гл. 12 — вызов LLM по HTTP |
| `typing` | Гл. 11, 13 — подсказки типов в FastAPI |

---

## ❓ Вопросы которые возникают

---

### 🙋 `import` vs `from X import Y` — в чём разница?

```python
import json                    # подключить весь модуль
json.loads(text)               # обращаться через имя модуля

from json import loads, dumps  # взять только нужные функции
loads(text)                    # вызывать напрямую

from datetime import date, timedelta   # берём конкретное из datetime
```

Правило: для стандартной библиотеки чаще используйте `import module` —
это явно показывает откуда пришла функция.

---

### 🙋 `pip` — это скачивает навсегда?

`pip install requests` скачивает библиотеку **в текущую среду Python**.
Если сменить компьютер или создать новое виртуальное окружение — надо установить снова.

Именно поэтому существует `requirements.txt`: список всего что нужно установить.

```bash
# Записать всё что установлено:
pip freeze > requirements.txt

# Установить из файла на другом компьютере:
pip install -r requirements.txt
```

---

### 🙋 Стандартная библиотека vs сторонние пакеты

| Стандартная (встроена, без pip) | Сторонние (нужен pip install) |
|---|---|
| `json`, `os`, `re`, `datetime` | `requests`, `fastapi`, `pydantic` |
| `math`, `statistics`, `csv` | `pandas`, `numpy`, `sqlalchemy` |
| `pathlib`, `logging`, `typing` | `openai`, `ollama`, `smolagents` |

```python
# Встроенная — просто import:
import statistics
print(statistics.mean([1, 2, 3]))  # 2.0

# Сторонняя — сначала pip install requests, потом:
import requests
r = requests.get("https://api.example.com")
```
