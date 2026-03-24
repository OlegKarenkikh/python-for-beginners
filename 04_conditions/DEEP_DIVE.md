# 🔀 Глава 04: Второй взгляд — Условия как светофор

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/conditions_tree.jpg" width="95%"/></div>

---

## Другая аналогия: светофор и камера на дороге

Камера видит скорость → принимает решение:
- ≤ 60 км/ч → штрафа нет
- 61–80 → штраф 500 руб.
- > 80 → штраф 5000 руб.

```python
speed = 75

if speed <= 60:
    fine = 0
    message = "Нарушений нет"
elif speed <= 80:
    fine = 500
    message = "Незначительное превышение"
else:
    fine = 5000
    message = "Серьёзное нарушение"

print(f"{message}. Штраф: {fine} руб.")
```

---

## Страшная сторона: порядок elif ВАЖЕН

```python
age = 24

# НЕПРАВИЛЬНО — первое условие поглотит все случаи < 65
if age < 65:
    print("Стандарт")
elif age < 25:   # до этого НИКОГДА не доберёмся если age=24!
    print("Молодой")  # эта ветка мертва

# ПРАВИЛЬНО — от узкого к широкому
if age < 25:
    print("Молодой водитель")    # сначала самое строгое
elif age < 65:
    print("Стандарт")
else:
    print("Водитель 65+")
```

---

## Страшная сторона: == vs is

```python
status = None

# НЕПРАВИЛЬНО
if status == None:   # работает, но плохой стиль
    print("Не установлен")

# ПРАВИЛЬНО для None
if status is None:   # правильно!
    print("Не установлен")

# == сравнивает ЗНАЧЕНИЯ
# is  сравнивает ЛИЧНОСТЬ объекта (тот же объект?)
# Для None, True, False — всегда используйте is
```

---

## Страшная сторона: опасные условия с float

```python
ratio = 0.1 + 0.2   # = 0.30000000000000004!

# ОПАСНО
if ratio == 0.3:
    print("Коэффициент 30%")   # НЕ ВЫПОЛНИТСЯ!

# ПРАВИЛЬНО
if abs(ratio - 0.3) < 0.0001:   # почти равно
    print("Коэффициент 30%")

# Или используйте Decimal (см. главу 03)
```

---

## Тернарный оператор — условие в одну строку

```python
age = 22

# Длинно
if age < 25:
    label = "Молодой"
else:
    label = "Стандарт"

# Коротко (тернарный оператор)
label = "Молодой" if age < 25 else "Стандарт"

# В страховом контексте
discount = 0.15 if is_vip else 0.0
risk_tag  = "ВЫСОКИЙ" if accidents > 2 else "НИЗКИЙ"
```

---

## match/case — Python 3.10+ (альтернатива длинному if-elif)

```python
claim_status = "manual_review"

match claim_status:
    case "auto_approved":
        print("Одобрено автоматически, выплата сегодня")
    case "manual_review":
        print("Передано аналитику")
    case "security_check":
        print("Передано в СБ")
    case "rejected":
        print("Отказ. Уведомляем клиента")
    case _:   # как else
        print(f"Неизвестный статус: {claim_status}")
```


---

## ❓ Вопросы которые возникают при изучении

---

### 🙋 Двоеточие после `if` — обязательно?

Да, абсолютно обязательно. Двоеточие говорит Python: «дальше начинается блок».

```python
if age < 25        # ❌ SyntaxError: expected ':'
    premium *= 1.5

if age < 25:       # ✅ правильно
    premium *= 1.5
```

**После чего всегда нужно двоеточие:** `if`, `elif`, `else`, `for`, `while`, `def`, `class`.

---

### 🙋 `risk *= 1.5` — это сокращение?

Да. Операторы «присвоить и выполнить»:

```python
risk *= 1.5     # то же что risk = risk * 1.5
total += p      # то же что total = total + p
count -= 1      # то же что count = count - 1
text += " руб." # то же что text = text + " руб."
```

---

### 🙋 `not experienced` — чем отличается от `experienced == False`?

`not x` — истина если `x` «ложное» (`False`, `None`, `0`, `""`, `[]`, `{}`).
`x == False` — истина только если `x` именно `False`.

```python
x = []
not x          # True  — пустой список «ложный»
x == False     # False — [] не равен False

x = 0
not x          # True  — ноль «ложный»
x == False     # True  — 0 == False (нюанс Python)
```

Используйте `not x` — это питоновский стиль. Линтер будет доволен.

---

### 🙋 Тернарный оператор — когда использовать?

Когда значение зависит от одного простого условия:

```python
# ✅ Хорошо — коротко и ясно
label = "молодой" if age < 25 else "стандарт"

# ❌ Плохо — слишком длинно, лучше обычный if/else
result = calculate_complex_function(a, b) if some_long_condition else another_function(c, d)
```

**Правило:** если тернарный не умещается в одну строку — используйте обычный `if/else`.
