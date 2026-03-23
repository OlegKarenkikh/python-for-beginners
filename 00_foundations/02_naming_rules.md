# ✏️ Правила именования в Python

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/naming_rules.jpg" alt="Правила именования переменных" width="95%"/>
</div>

---

## Золотые правила

1. **Только латинские** буквы, цифры и знак `_`
2. **Не начинается с цифры**
3. **Нет пробелов** — используйте `_`
4. **Нельзя** использовать зарезервированные слова (`if`, `for`, `return`…)
5. **Регистр важен:** `Name` ≠ `name` ≠ `NAME`

---

## snake_case — стандарт Python

Python использует **snake_case**: слова строчными буквами через `_`.

```python
# ✅ Правильный стиль (snake_case)
client_name     = "Иванов"
base_rate       = 12_000
total_premium   = 15_600
is_vip_client   = False
policy_number   = "POL-001"

# ❌ Другие стили (не для Python)
clientName      = "Иванов"    # camelCase — для Java/JS
ClientName      = "Иванов"    # PascalCase — для классов
```

---

## Константы — UPPER_SNAKE_CASE

Если значение **никогда не меняется** — пишите заглавными.

```python
# Константы (не меняются в ходе программы)
BASE_RATE           = 12_000
MAX_POLICY_AMOUNT   = 5_000_000
MIN_DRIVER_AGE      = 18
TAX_RATE            = 0.13
COMPANY_NAME        = "ПолисПлюс"
```

---

## Функции и методы — snake_case

```python
def calculate_premium(age, experience):
    ...

def validate_claim_documents(claim):
    ...

def get_risk_factor(client):
    ...
```

---

## Классы — PascalCase

```python
class InsuranceClient:
    ...

class PolicyCalculator:
    ...
```

---

## Примеры: хорошо и плохо

| ❌ Плохо | ✅ Хорошо | Почему |
|---|---|---|
| `x` | `client_age` | непонятное имя |
| `d` | `discount_rate` | однобуквенное |
| `2rate` | `rate_2` | начинается с цифры |
| `my rate` | `my_rate` | пробел |
| `клиент` | `client` | кириллица |
| `for` | `for_count` | зарезервированное слово |
| `prem` | `premium` | сокращение |
| `data` | `clients_list` | слишком общее |

---

## Одиночное подчёркивание `_`

```python
# Временная переменная (не важна)
_ = some_function()

# В цикле когда индекс не нужен
for _ in range(5):
    print("Привет")
```

---

## Зарезервированные слова (нельзя использовать как имена)

```
False   None    True    and     as      assert
async   await   break   class   continue def
del     elif    else    except  finally  for
from    global  if      import  in       is
lambda  nonlocal not    or      pass     raise
return  try     while   with    yield
```

Итого: **35 слов**. Редактор подсветит их цветом — сразу видно.
