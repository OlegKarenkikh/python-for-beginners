# Глава 15: Ошибки, отладка, логирование

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/traceback_anatomy.jpg" width="95%"/></div>

> **Главное правило:** читай traceback **снизу вверх**.
> Последняя строка — тип и причина ошибки. Выше — где это произошло.

---

## Как читать traceback Python

```
Traceback (most recent call last):            <- 1. Заголовок
  File "main.py", line 12, in process_claim  <- 2. Где произошло
    result = amount / days                   <- 3. Строка кода
  File "main.py", line 5, in calculate       <- 4. Вложенный вызов
    return a / b                             <- 5. Строка кода
ZeroDivisionError: division by zero          <- 6. ЧИТАЙ ЗДЕСЬ ПЕРВЫМ
```

**Алгоритм:**
1. Смотри на **последнюю строку** — тип ошибки и причина
2. Смотри на **строку над ней** — код который упал
3. Смотри **выше** — цепочка вызовов, как дошли до ошибки

---

## ТОП-10 ошибок новичка

### 1. NameError — переменная не объявлена

```python
# ОШИБКА
print(premiym)          # опечатка в имени
# NameError: name 'premiym' is not defined

# КАК ИЗБЕЖАТЬ
# Используй Tab (автодополнение) в Jupyter/VS Code
print(premium)
```

### 2. TypeError — неправильный тип

```python
# ОШИБКА
age = input("Возраст: ")   # input возвращает строку!
premium = 12000 * 1.5 if age < 25 else 12000
# TypeError: '<' not supported between instances of 'str' and 'int'

# ИСПРАВЛЕНИЕ
age = int(input("Возраст: "))   # явное преобразование
```

### 3. KeyError — нет ключа в словаре

```python
client = {"name": "Иванов", "age": 35}

# ОШИБКА
print(client["city"])
# KeyError: 'city'

# БЕЗОПАСНО
print(client.get("city", "не указан"))   # "не указан"
# или
if "city" in client:
    print(client["city"])
```

### 4. IndexError — выход за пределы списка

```python
claims = ["claim_1", "claim_2", "claim_3"]

# ОШИБКА
print(claims[5])
# IndexError: list index out of range

# ИСПРАВЛЕНИЕ
if len(claims) > 5:
    print(claims[5])
# или
print(claims[-1])    # последний элемент — всегда безопасно
```

### 5. AttributeError — нет такого атрибута/метода

```python
# ОШИБКА
name = "иванов"
print(name.upper)    # забыли скобки!
# Вернёт: <built-in method upper of str object>  (не ошибка, но не то)

name.capitalize()    # правильно — метод с ()
print(name.upper())  # ИВАНОВ
```

### 6. ValueError — неправильное значение

```python
# ОШИБКА
age = int("тридцать пять")
# ValueError: invalid literal for int() with base 10: 'тридцать пять'

# ИСПРАВЛЕНИЕ
try:
    age = int(input("Возраст: "))
except ValueError:
    print("Введите число!")
    age = 0
```

### 7. FileNotFoundError

```python
# ОШИБКА
with open("clients.json") as f:
    data = f.read()
# FileNotFoundError: [Errno 2] No such file or directory: 'clients.json'

# ИСПРАВЛЕНИЕ
import os
if os.path.exists("clients.json"):
    with open("clients.json") as f:
        data = f.read()
else:
    print("Файл не найден, создаём пустую базу")
    data = "[]"
```

### 8. ZeroDivisionError

```python
# ОШИБКА
avg = total_premium / client_count   # если client_count == 0
# ZeroDivisionError: division by zero

# ИСПРАВЛЕНИЕ
avg = total_premium / client_count if client_count > 0 else 0
```

### 9. IndentationError — проблема с отступами

```python
# ОШИБКА
def calculate(age):
    if age < 25:
    return 18000       # ← нет отступа после if!
# IndentationError: expected an indented block

# ИСПРАВЛЕНИЕ
def calculate(age):
    if age < 25:
        return 18000   # 4 пробела
    return 12000
```

### 10. ImportError / ModuleNotFoundError

```python
# ОШИБКА
import fastapi
# ModuleNotFoundError: No module named 'fastapi'

# ИСПРАВЛЕНИЕ
# В терминале:
# pip install fastapi
```

---

## try / except / finally

```python
def safe_calculate(age_str, amount_str):
    try:
        # Код который может упасть
        age    = int(age_str)
        amount = float(amount_str)
        
        if amount <= 0:
            raise ValueError(f"Сумма должна быть > 0, получили: {amount}")
        
        premium = 12000 * 1.5 if age < 25 else 12000
        return premium
    
    except ValueError as e:
        # Обрабатываем конкретную ошибку
        print(f"Ошибка ввода: {e}")
        return None
    
    except Exception as e:
        # Все остальные ошибки
        print(f"Неожиданная ошибка: {e}")
        return None
    
    finally:
        # Выполняется ВСЕГДА — для очистки ресурсов
        print("Расчёт завершён")


print(safe_calculate("22", "5000"))    # 18000.0  Расчёт завершён
print(safe_calculate("abc", "5000"))   # Ошибка ввода  Расчёт завершён  None
print(safe_calculate("22", "-100"))    # Ошибка  Расчёт завершён  None
```

---

## Логирование: замена print

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/logging_levels.jpg" width="95%"/></div>

**Почему logging лучше print:**
- Можно включить/выключить уровень одной строкой
- Автоматически пишет время, модуль, строку
- Пишет в файл и в консоль одновременно
- В продакшн-системах `print` не видно в логах

```python
import logging

# Настройка — делается один раз при старте приложения
logging.basicConfig(
    level=logging.DEBUG,      # минимальный уровень
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),                     # вывод в консоль
        logging.FileHandler("insurance.log"),        # и в файл
    ]
)

logger = logging.getLogger("insurance.calculator")

# Использование
def calculate_premium(client_name, age, accidents=0):
    logger.debug(f"Расчёт для {client_name}: age={age}, accidents={accidents}")
    
    if age < 0 or age > 120:
        logger.error(f"Некорректный возраст: {age}")
        raise ValueError(f"Возраст {age} невозможен")
    
    base = 12_000
    if age < 25:
        base *= 1.5
        logger.info(f"Применён молодёжный коэффициент x1.5 для {client_name}")
    
    if accidents > 0:
        base *= 1 + accidents * 0.2
        logger.warning(f"{client_name} имеет {accidents} аварий — коэффициент повышен")
    
    logger.info(f"Итоговая премия {client_name}: {base:.0f} руб.")
    return round(base, 2)

calculate_premium("Иванов", 35)
calculate_premium("Петрова", 22)
calculate_premium("Козлов",  58, accidents=2)
```

**Вывод:**
```
2026-03-24 07:00:01  DEBUG     insurance.calculator  Расчёт для Иванов: age=35, accidents=0
2026-03-24 07:00:01  INFO      insurance.calculator  Итоговая премия Иванов: 12000 руб.
2026-03-24 07:00:01  DEBUG     insurance.calculator  Расчёт для Петрова: age=22, accidents=0
2026-03-24 07:00:01  INFO      insurance.calculator  Применён молодёжный коэффициент x1.5
2026-03-24 07:00:01  WARNING   insurance.calculator  Козлов имеет 2 аварий — коэффициент повышен
```

---

## Анализ логов из командной строки

```bash
# Все ошибки за сегодня
grep "ERROR" insurance.log

# Только WARNING и выше
grep -E "WARNING|ERROR|CRITICAL" insurance.log

# Последние 50 строк лога
tail -50 insurance.log

# Живой мониторинг
tail -f insurance.log

# Сколько ошибок за день
grep "ERROR" insurance.log | wc -l

# Найти клиента в логах
grep "Козлов" insurance.log

# Ошибки за конкретный час
grep "2026-03-24 07:" insurance.log | grep "ERROR"
```

---

## Структурированные логи (JSON)

В продакшн-системах логи пишут в JSON — их легче парсить:

```python
import logging, json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({
            "time":    datetime.utcnow().isoformat(),
            "level":   record.levelname,
            "logger":  record.name,
            "message": record.getMessage(),
            "module":  record.module,
            "line":    record.lineno,
        }, ensure_ascii=False)

handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logging.getLogger().addHandler(handler)
```

```bash
# Анализ JSON-логов
cat insurance.log | python3 -c "
import sys, json
for line in sys.stdin:
    try:
        d = json.loads(line)
        if d['level'] == 'ERROR':
            print(d['time'], d['message'])
    except: pass
"
```

---

## Упражнения

1. Напишите функцию `parse_age(s)` которая возвращает `int` или `None` при ошибке — используйте `try/except ValueError`.

2. Добавьте логирование в `calculate_premium` из предыдущей главы: DEBUG при входе, INFO при выходе, WARNING при авариях.

3. Запустите скрипт и откройте `insurance.log` в редакторе.

4. Используйте `grep` чтобы найти все WARNING в логе.

5. Напишите функцию `load_clients(path)` которая ловит `FileNotFoundError` и `json.JSONDecodeError`.
