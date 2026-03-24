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
