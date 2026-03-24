# 🔧 Глава 06: Второй взгляд — Функции как контракт

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/function_vending.jpg" width="95%"/></div>

---

## Другая аналогия: торговый автомат

Кладёшь монеты (аргументы) → автомат делает своё дело → получаешь напиток (return).

Не важно что внутри. Главное — что кладёшь и что получаешь.

---

## Страшная сторона: return vs print

```python
# Эти функции выглядят похоже, но работают СОВСЕМ по-разному

def bad_premium(age, base):
    premium = base * (1.5 if age < 25 else 1.0)
    print(f"Премия: {premium}")  # только печатает на экран!

def good_premium(age, base):
    premium = base * (1.5 if age < 25 else 1.0)
    return premium  # возвращает значение

# bad_premium нельзя использовать в вычислениях
total = bad_premium(22, 12000) + 1000   # TypeError: None + 1000
#      ↑ вернула None, потому что нет return!

# good_premium — можно
total = good_premium(22, 12000) + 1000  # 19000 ✓
```

---

## Страшная сторона: изменяемые аргументы по умолчанию

```python
# КЛАССИЧЕСКАЯ ЛОВУШКА Python — не делайте так!
def add_accident(client, accidents=[]):   # список как дефолт — ПЛОХО!
    accidents.append(client)
    return accidents

r1 = add_accident("Иванов")    # ["Иванов"]
r2 = add_accident("Петрова")   # ["Иванов", "Петрова"] ← ожидали ["Петрова"]!

# Список создаётся ОДИН РАЗ при определении функции и переиспользуется!

# ПРАВИЛЬНО
def add_accident(client, accidents=None):
    if accidents is None:
        accidents = []   # новый список каждый раз
    accidents.append(client)
    return accidents
```

---

## Страшная сторона: область видимости (scope)

```python
base_rate = 12_000   # глобальная переменная

def calculate(age):
    # Функция ВИДИТ глобальные переменные
    premium = base_rate * (1.5 if age < 25 else 1.0)
    return premium

# Но не может их изменить без global
def update_rate(new_rate):
    base_rate = new_rate   # создаст ЛОКАЛЬНУЮ переменную!
    print(base_rate)       # покажет new_rate

update_rate(15_000)
print(base_rate)           # 12_000 — глобальная не изменилась!

# ПРАВИЛЬНО если нужно изменить
def update_rate(new_rate):
    global base_rate   # говорим: работаем с глобальной
    base_rate = new_rate

# На практике: лучше избегать global — передавайте через аргументы
```

---

## Type hints — подсказки типов

```python
# Без подсказок — непонятно что ожидает функция
def calculate_premium(age, base, accidents):
    ...

# С подсказками — сразу понятно
def calculate_premium(age: int, base: float, accidents: int = 0) -> float:
    premium = base
    if age < 25:
        premium *= 1.5
    if accidents > 0:
        premium *= (1 + accidents * 0.2)
    return round(premium, 2)

# IDE подскажет ошибку если передать строку вместо числа
calculate_premium("35", 12000, 0)   # IDE: ожидается int, получена str
```

---

## Документация функции

```python
def assess_claim(claim_id: int, amount: float, car_model: str) -> dict:
    """
    Оценивает страховое заявление и возвращает решение.
    
    Args:
        claim_id:  Уникальный ID заявления
        amount:    Запрошенная сумма выплаты в рублях
        car_model: Марка автомобиля
    
    Returns:
        dict с ключами: status, approved_amount, reason
    
    Examples:
        >>> assess_claim(42, 45000, "Toyota")
        {'status': 'auto_approved', 'approved_amount': 45000, 'reason': 'Сумма в норме'}
    """
    if amount <= 50_000:
        return {"status": "auto_approved", "approved_amount": amount, "reason": "Сумма в норме"}
    elif amount <= 300_000:
        return {"status": "manual_review", "approved_amount": None, "reason": "Требует проверки"}
    else:
        return {"status": "security_check", "approved_amount": None, "reason": "Крупная сумма"}
```


---

## ❓ Вопросы которые возникают при изучении

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/qa_functions.png" alt="Вопросы о функциях" width="95%"/>
</div>

---

### 🙋 `return` vs `print` — в чём разница?

**Ключевое отличие:** `print` только показывает на экране. `return` возвращает значение для дальнейшего использования.

```python
def bad_premium(age, base):
    premium = base * 1.5
    print(premium)       # ⚠️ только печатает, ничего не возвращает

def good_premium(age, base):
    premium = base * 1.5
    return premium       # ✅ возвращает значение

# Разница в использовании:
result = bad_premium(22, 12000)   # напечатает 18000, но result = None!
total = result + 1000             # ❌ TypeError: None + int

result = good_premium(22, 12000)  # result = 18000
total = result + 1000             # ✅ total = 19000
```

> 💡 **Правило:** если планируете использовать результат — всегда пишите `return`.

---

### 🙋 Тройные кавычки внутри функции — это комментарий?

Нет! Это **docstring** — документационная строка. Она хранится в `__doc__` и показывается IDE.

```python
def calculate_premium(age, base_rate):
    \"\"\"Рассчитывает страховую премию.
    
    Args:
        age: возраст клиента в годах
        base_rate: базовая ставка в рублях
    Returns:
        float: итоговая премия
    \"\"\"
    ...

# Посмотреть docstring:
help(calculate_premium)
print(calculate_premium.__doc__)
```

VS Code и PyCharm показывают docstring во всплывающей подсказке при наведении мыши.

---

### 🙋 `round()` откуда взялась без import?

Это **встроенная функция** (builtin). Python загружает ~70 таких функций автоматически.

Самые используемые builtins:
```python
print()   len()   type()   int()   str()   float()
bool()    list()  dict()   set()   range() enumerate()
zip()     sorted() sum()  min()   max()   abs()
round()   input()  open()  isinstance()
```

Всё что не в этом списке — нужно `import`.

---

### 🙋 Что значит `{client_id:05d}`?

- `05` — ширина поля 5 символов, заполнить **нулями** слева
- `d` — decimal (целое десятичное число)

```python
print(f"{42:05d}")     # 00042
print(f"{1:05d}")      # 00001
print(f"{12345:05d}")  # 12345   — ровно 5
print(f"{123456:05d}") # 123456  — шире 5, не обрезается!
```

---

### 🙋 «Функция — объект» — что это значит?

В Python функции можно: присваивать переменной, класть в список, передавать как аргумент.

```python
def greet(name):
    return f"Привет, {name}!"

# Функция как переменная
say_hi = greet
print(say_hi("Иванов"))   # "Привет, Иванов!"

# Функция в словаре — реестр обработчиков
handlers = {
    "fraud": check_fraud,
    "calc":  calculate_premium,
}
result = handlers["fraud"](claim)   # вызвали нужную функцию по ключу
```

Это фундамент декораторов, колбэков и агентских систем.
