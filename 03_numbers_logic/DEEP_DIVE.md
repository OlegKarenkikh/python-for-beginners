# 🔢 Глава 03: Второй взгляд — Числа и ловушки

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/numbers_traps.jpg" width="95%"/></div>

---

## Другая аналогия: числа как стаканы разного размера

`int` — стакан для воды (целые числа). `float` — термос (дробные).
Если смешать — Python иногда удивит.

```python
# Делите? Думайте о типе результата!
13 / 5    # → 2.6  (всегда float!)
13 // 5   # → 2    (только целая часть)
13 % 5    # → 3    (остаток от деления)

# В страховании важно:
total_claims = 47
per_agent    = total_claims // 5   # 9 дел на агента
remainder    = total_claims % 5    # 2 дела остались
print(f"По {per_agent} дел, ещё {remainder} в очереди")
```

---

## Страшная сторона: деньги и float

```python
# НИКОГДА не используйте float для денег!
premium = 0.1 + 0.2
print(premium)   # 0.30000000000000004  ← ЭТО НЕ 0.3!

# Почему? float хранится в двоичном виде — некоторые числа
# не представимы точно, как 1/3 в десятичной дроби

# ПРАВИЛЬНО — для денег используйте Decimal
from decimal import Decimal
p1 = Decimal("0.1")
p2 = Decimal("0.2")
print(p1 + p2)   # 0.3 — точно!

# В страховой системе:
base    = Decimal("12000.00")
coeff   = Decimal("1.50")
premium = base * coeff
print(f"Премия: {premium} руб.")  # 18000.00 — точно
```

---

## Страшная сторона: деление на ноль

```python
# Это вызовет ошибку!
claims_count = 0
avg_amount = total_amount / claims_count
# ZeroDivisionError: division by zero

# Защита
avg_amount = total_amount / claims_count if claims_count > 0 else 0
print(f"Средняя сумма: {avg_amount:,.0f} руб.")
```

---

## Страшная сторона: большие числа и читаемость

```python
# Плохо — число невозможно прочитать
max_coverage = 1000000000

# Хорошо — Python игнорирует _ как разделитель
max_coverage = 1_000_000_000
annual_premium = 14_400.50

# Форматирование вывода
print(f"Покрытие: {max_coverage:,} руб.")   # 1,000,000,000 руб.
print(f"Премия:   {annual_premium:.2f} руб.")  # 14400.50 руб.
```

---

## Полезные функции для страхования

```python
import math

# Округление — три способа
premium = 14567.333

round(premium, 0)      # 14567.0 — математическое
math.floor(premium)    # 14567   — вниз (в пользу клиента)
math.ceil(premium)     # 14568   — вверх (в пользу СК)

# abs — для разниц
delta = abs(actual_loss - estimated_loss)

# Мин/макс в списках
premiums = [12000, 18000, 9500, 24000]
print(f"Мин: {min(premiums):,}")   # 9,500
print(f"Макс: {max(premiums):,}")  # 24,000
print(f"Сумма: {sum(premiums):,}") # 63,500

# Процентное изменение
old_premium = 12_000
new_premium = 14_400
change_pct  = (new_premium - old_premium) / old_premium * 100
print(f"Рост: {change_pct:.1f}%")  # Рост: 20.0%
```


---

## ❓ Вопросы которые возникают при изучении

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/qa_numbers.png" alt="Вопросы о числах и точности" width="95%"/>
</div>

---

### 🙋 Почему `0.1 + 0.2 = 0.30000000000000004`?

Компьютер хранит числа в двоичной (бинарной) системе.
Некоторые дроби невозможно представить точно в двоичном виде — как `1/3` в десятичной (0.333...).
`0.1` в двоичном — бесконечная дробь. Процессор её обрезает — появляется погрешность.

```python
print(0.1 + 0.2)     # 0.30000000000000004  — неожиданно!
print(0.1 + 0.2 == 0.3)  # False!

# Решения:
import math
print(math.isclose(0.1 + 0.2, 0.3))   # True — сравнение с допуском

from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))  # 0.3 — точно
```

**Это не баг Python** — так работают все современные процессоры (стандарт IEEE 754).

---

### 🙋 `4 / 2` — результат 2 или 2.0?

В Python 3 — всегда `2.0` (float). Всегда.

```python
print(4 / 2)        # 2.0  — float
print(type(4 / 2))  # <class 'float'>

print(4 // 2)       # 2    — int, целочисленное деление
print(type(4 // 2)) # <class 'int'>
```

---

### 🙋 Зачем `Decimal("0.1")` строкой, а не числом `0.1`?

Если передать число `Decimal(0.1)` — вы передаёте уже неточный float.
Строка `"0.1"` парсится точно, без промежуточного float.

```python
from decimal import Decimal
print(Decimal(0.1))    # 0.1000000000000000055511...  ← неточно!
print(Decimal("0.1"))  # 0.1  ← точно
```

**Правило:** для денег всегда `Decimal("строка")`, никогда `Decimal(число)`.

---

### 🙋 Подчёркивание в числе `1_500_000` — это работает?

Да, это абсолютно корректный Python (с версии 3.6). Только визуальный разделитель.

```python
million = 1_000_000
print(million)              # 1000000
print(1_500_000 == 1500000)  # True
```

---

### 🙋 `from decimal import Decimal` — нужно скачивать?

Нет. `decimal` — стандартная библиотека Python, встроена.
`import` не значит «скачать» — значит «подключить уже установленный модуль».
Скачивать (`pip install`) нужно только сторонние пакеты.
