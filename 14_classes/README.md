# Глава 14: Классы и объекты

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/class_analogy.jpg" width="95%"/></div>

> **Аналогия**: класс — это бланк страхового полиса. Сам бланк ничего не значит.
> Когда вы заполняете его данными Иванова — получается **объект** (экземпляр).

---

## Зачем нужны классы?

**Без класса — 7 отдельных переменных на каждого клиента:**

```python
client1_name = "Иванов А.П."
client1_age = 35
client1_premium = 14_400
# и ещё для client2, client3... 😱
```

**С классом — один шаблон, сколько угодно объектов:**

```python
class Client:
    def __init__(self, name, age, premium):
        self.name = name
        self.age = age
        self.premium = premium

client1 = Client("Иванов А.П.", 35, 14_400)
client2 = Client("Петрова М.С.", 22, 21_600)
print(client1.name)  # Иванов А.П.
```

---

## Анатомия класса

```python
class InsurancePolicy:        # имя класса — с заглавной буквы
    
    def __init__(self, owner, car, premium):   # конструктор
        self.owner   = owner      # атрибуты объекта
        self.car     = car
        self.premium = premium
        self.active  = True       # значение по умолчанию
    
    def deactivate(self):         # метод
        self.active = False
    
    def info(self):               # метод вывода
        status = "активен" if self.active else "закрыт"
        return f"Полис: {self.owner} / {self.car} / {self.premium:,} руб. [{status}]"

# Создаём объекты
policy1 = InsurancePolicy("Иванов А.П.", "Toyota Camry", 14_400)
policy2 = InsurancePolicy("Петрова М.С.", "Kia Rio", 21_600)

print(policy1.info())   # Полис: Иванов А.П. / Toyota Camry / 14,400 руб. [активен]
policy1.deactivate()
print(policy1.info())   # Полис: Иванов А.П. / Toyota Camry / 14,400 руб. [закрыт]
```

---

## self — что это такое?

`self` — ссылка на **сам объект**. Python передаёт её автоматически при вызове метода.

```python
class Calc:
    def __init__(self, base):
        self.base = base
    
    def double(self):
        return self.base * 2     # self.base — атрибут этого объекта

c = Calc(10)
c.double()    # Python на самом деле вызывает: Calc.double(c)
              # self = c, поэтому self.base = 10
```

> 💡 `self` — соглашение, не ключевое слово. Можно написать `this`, но все пишут `self`.

---

## Наследование: от общего к частному

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year  = year
    
    def age(self):
        return 2025 - self.year

class Car(Vehicle):             # Car наследует Vehicle
    def __init__(self, brand, year, engine_cc):
        super().__init__(brand, year)   # вызов родительского __init__
        self.engine_cc = engine_cc
    
    def premium_rate(self):
        base = 0.04
        if self.engine_cc > 2000:
            base += 0.01        # доплата за мощный двигатель
        return base

car = Car("BMW X5", 2021, 2993)
print(f"{car.brand}, возраст {car.age()} лет, ставка {car.premium_rate():.1%}")
# BMW X5, возраст 4 лет, ставка 5.0%
```

---

## Dataclass — класс без лишнего кода

```python
from dataclasses import dataclass, field

@dataclass
class Claim:
    claim_id: str
    amount:   float
    approved: bool = False         # значение по умолчанию
    tags:     list = field(default_factory=list)
    
    def approve(self):
        self.approved = True

c = Claim("CLM-001", 45_000)
print(c)           # Claim(claim_id='CLM-001', amount=45000, approved=False, tags=[])
c.approve()
print(c.approved)  # True
```

Dataclass автоматически создаёт `__init__`, `__repr__`, `__eq__` — писать руками не надо.

---

## Частые ошибки с классами

```python
# ❌ Забыли self в методе
class Bad:
    def greet():          # нет self!
        print("Привет")

b = Bad()
b.greet()   # TypeError: greet() takes 0 positional arguments but 1 was given

# ✅ Правильно
class Good:
    def greet(self):
        print("Привет")

# ❌ Изменяемый объект как дефолтный аргумент
class Broken:
    def __init__(self, tags=[]):   # ⚠️ список делится между всеми объектами!
        self.tags = tags

# ✅ Правильно
class Fixed:
    def __init__(self, tags=None):
        self.tags = tags if tags is not None else []
```

---

## ❓ Вопросы которые возникают

---

### 🙋 `__init__` — зачем подчёркивания?

Двойные подчёркивания (`__`) называются **dunder** (double underscore).
`__init__` — «магический метод», Python вызывает его автоматически при создании объекта.

```python
policy = InsurancePolicy("Иванов", "BMW", 14_400)
# Python автоматически вызвал: InsurancePolicy.__init__(policy, "Иванов", "BMW", 14_400)
```

Другие dunder-методы:
- `__str__` — что вернуть при `print(obj)` и `str(obj)`
- `__repr__` — отладочное представление в консоли
- `__len__` — что вернуть при `len(obj)`
- `__eq__` — что значит `obj1 == obj2`

---

### 🙋 Класс vs функция — когда что?

**Функция** — когда выполняется одно действие, нет состояния:
```python
def calculate_premium(age, base): return base * 1.5 if age < 25 else base
```

**Класс** — когда нужно хранить состояние + поведение вместе:
```python
class Policy:
    def __init__(self, owner, premium): ...
    def activate(self): ...
    def pay(self, amount): ...
```

Правило: если у вас 3+ связанных переменных и 2+ функций работают с ними — пора в класс.

---

### 🙋 `super().__init__` — что это?

`super()` — ссылка на родительский класс. `super().__init__(...)` вызывает конструктор родителя:

```python
class Car(Vehicle):
    def __init__(self, brand, year, engine_cc):
        super().__init__(brand, year)   # инициализируем родительские атрибуты
        self.engine_cc = engine_cc      # добавляем свой
```

Без `super().__init__` атрибуты `brand` и `year` не будут созданы.

---

## Упражнения

```python
# 1. Создайте класс Claim (заявление на выплату):
#    поля: claim_id (str), amount (float), status (str = "pending")
#    метод approve() — меняет status на "approved"
#    метод reject() — меняет status на "rejected"

# 2. Создайте список из 5 заявлений, одобрите нечётные, отклоните чётные
#    Напечатайте только одобренные и их суммарный размер выплат

# 3. Напишите CargoPolicy(Policy) — страхование груза
#    Дополнительный атрибут: weight_kg (float)
#    Метод premium() учитывает весовой коэффициент: base * 0.001 * weight_kg

# 4. Используйте @dataclass для модели Vehicle(brand, year, mileage_km)
```
