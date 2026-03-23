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
