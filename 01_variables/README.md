# 📦 Глава 01: Переменные и типы данных

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/variables_explained.jpg" alt="Переменные — ящики с именами" width="90%"/>
</div>

> **Цель:** научиться хранить и использовать данные  
> **Время:** ~1 час  
> **Файлы:** `examples/`, `exercises/`

---

## Аналогия: ящики с подписями

Представьте шкаф с ящиками. На каждом ящике — наклейка с именем.

В ящик `name` вы кладёте «Иванов А.П.»  
В ящик `age` кладёте число 35  
В ящик `premium` кладёте 45000.50

**Переменная = ящик с именем.** В Python это выглядит так:

```python
name = "Иванов А.П."   # текстовая строка (str)
age = 35                # целое число (int)
premium = 45000.50      # дробное число (float)
is_vip = True           # да/нет (bool)
```

Знак `=` — это не «равно», это «положить в ящик».

---

## Четыре основных типа

| Тип | Python | Пример | Когда использовать |
|---|---|---|---|
| Строка | `str` | `"Иванов А.П."` | Имена, адреса, тексты |
| Целое число | `int` | `35` | Возраст, количество аварий |
| Дробное число | `float` | `45000.50` | Суммы, коэффициенты |
| Логическое | `bool` | `True` / `False` | Да/Нет, флаги |

---

## Как работать с переменными

```python
# Создаём переменные клиента
client_name = "Петрова М.С."
client_age = 22
base_rate = 12000
risk_factor = 1.5

# Вычисляем
premium = base_rate * risk_factor
print(f"Клиент: {client_name}")
print(f"Возраст: {client_age} лет")
print(f"Премия: {premium:.0f} руб.")
```

**Вывод:**
```
Клиент: Петрова М.С.
Возраст: 22 лет
Премия: 18000 руб.
```

---

## Важные правила именования

```python
# ✅ Хорошо
client_name = "Иванов"
base_rate = 12000
total_premium = 15600

# ❌ Плохо — Python не поймёт
2name = "Иванов"      # нельзя начинать с цифры
client name = "Иванов" # нельзя пробелы
```

**Правило:** используйте `_` вместо пробелов, пишите на латинице, называйте понятно.

---

## Проверка типа

```python
age = 35
print(type(age))        # <class 'int'>

name = "Иванов"
print(type(name))       # <class 'str'>

coeff = 1.5
print(type(coeff))      # <class 'float'>
```

---

## Практика

Откройте файлы в папке `examples/` и запустите их:
```bash
python examples/01_first_variables.py
python examples/02_insurance_client.py
python examples/03_calculations.py
```

Затем выполните упражнения в `exercises/`.

---

## Шпаргалка главы

```python
name = "текст"          # строка
age = 35                # целое число
rate = 1.5              # дробное
active = True           # булево
print(type(name))       # узнать тип
print(f"Текст {name}") # f-строка для вывода
```

➡️ [Глава 02: Строки](../02_strings/README.md)
