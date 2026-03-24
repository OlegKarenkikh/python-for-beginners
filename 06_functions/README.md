# 🔧 Глава 06: Функции — def

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/function_vs_copypaste.jpg" alt="Функция vs копипаст" width="90%"/>
</div>

> **Цель:** перестать копипастить код — писать функции
> **Время:** ~1.5 часа

---

## Аналогия: рецепт борща

Вы варите борщ каждую неделю. Каждый раз писать рецепт заново? Нет — вы записываете его один раз, потом используете когда нужно.

**Функция = рецепт.** Написал один раз — используй сколько угодно раз, с разными ингредиентами.

```python
# Записываем "рецепт" — функцию
def calculate_premium(age, base_rate, accidents):
    """Рассчитывает страховую премию."""
    premium = base_rate

    if age < 25:
        premium *= 1.5      # молодой водитель — дороже
    elif age > 60:
        premium *= 1.3      # водитель 60+ — дороже

    if accidents > 0:
        premium *= (1 + accidents * 0.2)   # каждая авария +20%

    return round(premium, 2)   # возвращаем РЕЗУЛЬТАТ наружу

# "Используем рецепт" — вызываем функцию с разными данными
print(calculate_premium(35, 12_000, 0))   # 12000.0
print(calculate_premium(22, 12_000, 1))   # 21600.0
print(calculate_premium(65, 12_000, 0))   # 15600.0
```

---

## Что такое return

> `return` — это **ответ** функции. Как ответ на вопрос.

```python
# Вы спрашиваете: "Сколько платит клиент 35 лет?"
# Функция отвечает: return 12000.0

result = calculate_premium(35, 12_000, 0)
#   ↑ В result попадает то, что функция вернула через return

# Без return функция "немая" — работает, но ничего не сообщает
def just_print(name):
    print(f"Клиент: {name}")   # печатает на экран
    # нет return — возвращает None

x = just_print("Иванов")   # напечатает "Клиент: Иванов"
print(x)                   # None — функция ничего не вернула!
```

> 💡 **Правило:** если планируете использовать результат функции — всегда пишите `return`.
> Если функция только что-то делает (пишет в файл, отправляет запрос) — `return` необязателен.

---

## Анатомия функции

```
def  имя_функции  (  параметры  ):
     ┌──────────────────────────┐
     │    тело функции          │  ← отступ 4 пробела
     │    (что делает)          │
     └──────────────────────────┘
     return  результат
```

| Часть | Что делает | Пример |
|---|---|---|
| `def` | Говорит Python: «сейчас я опишу функцию» | `def calc(...)` |
| имя | Как будем вызывать | `calculate_premium` |
| параметры | Что функция получает на входе | `age, base_rate` |
| тело | Что функция делает | `premium *= 1.5` |
| `return` | Что функция возвращает | `return round(premium, 2)` |

---


<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/function_anatomy.jpg" alt="Анатомия функции" width="90%"/></div>
## Параметры по умолчанию

```python
# Если accidents не указан — считаем что аварий не было (0)
def get_policy_number(client_id, year=2024, prefix="POL"):
    return f"{prefix}-{year}-{client_id:05d}"
    #                                    ↑ 5 цифр с ведущими нулями

print(get_policy_number(42))                  # POL-2024-00042
print(get_policy_number(7, prefix="КАСКО"))   # КАСКО-2024-00007
print(get_policy_number(7, 2025, "ОСАГО"))    # ОСАГО-2025-00007
```

---

## Практика

```bash
python examples/01_first_function.py
python examples/02_premium_calculator.py
python examples/03_validation_functions.py
```

---

## 📌 После этой главы вы умеете:
- Написать функцию с параметрами и `return`
- Объяснить разницу между `print` внутри функции и `return`
- Использовать параметры по умолчанию
- Распознать когда код «просит» вынести его в функцию

➡️ [Глава 07: Списки и словари](../07_lists_dicts/README.md)
