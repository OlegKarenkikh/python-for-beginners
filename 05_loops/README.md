# 🔄 Глава 05: Циклы — for и while

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/for_loop_claims.jpg" alt="for loop — перебираем заявления" width="90%"/>
</div>

> **Цель:** обрабатывать много данных автоматически  
> **Время:** ~1.5 часа

---

## Аналогия: конвейер

Представьте конвейерную ленту со страховыми заявлениями.  
Каждое заявление — один элемент.  
Цикл `for` — это конвейер: берём по одному, обрабатываем, едем дальше.

```python
claims = ["Иванов", "Петрова", "Сидоров"]

for name in claims:
    print(f"Обрабатываем: {name}")
```

```
Обрабатываем: Иванов
Обрабатываем: Петрова
Обрабатываем: Сидоров
```

---

## for: перебрать список

```python
premiums = [15_200, 34_800, 8_500, 22_100, 19_600]

total = 0
for p in premiums:
    total += p

print(f"Сборов: {len(premiums)} полисов")
print(f"Итого:  {total:,} руб.")
```

---

## range(): цикл заданное число раз

```python
# Напечатать номера полисов
for i in range(1, 6):
    policy = f"POL-2024-{i:04d}"
    print(policy)
```
```
POL-2024-0001
POL-2024-0002
...
POL-2024-0005
```

---

## while: пока условие выполняется

```python
# Ждём пока пользователь введёт корректный возраст
while True:
    age = int(input("Введите возраст (18-100): "))
    if 18 <= age <= 100:
        break
    print("Некорректный возраст, попробуйте снова")

print(f"Принято: {age} лет")
```

---

## enumerate: индекс + значение

```python
clients = ["Козлов", "Зайцева", "Морозов"]

for i, name in enumerate(clients, start=1):
    print(f"{i}. {name}")
```
```
1. Козлов
2. Зайцева
3. Морозов
```

---

## Практика

```bash
python examples/01_for_basics.py
python examples/02_process_claims.py
python examples/03_statistics.py
```

➡️ [Глава 06: Функции](../06_functions/README.md)
