# ✍️ Глава 02: Строки — работа с текстом

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/string_immutable.jpg" alt="Работа со строками" width="90%"/>
</div>

> **Цель:** научиться создавать и обрабатывать текстовые данные  
> **Время:** ~1 час

---

## Аналогия: текст в кавычках

Строка — это любой текст в кавычках. Python не считает его числом или командой — просто текст.

```python
name = "Иванов Алексей"         # двойные кавычки
city = 'Москва'                   # одинарные — тоже можно
address = "ул. Ленина, д. 5"     # кавычки внутри — без проблем
```

---

## Основные операции со строками

```python
name = "Иванов Алексей Петрович"

# Длина строки
print(len(name))              # 26

# Верхний / нижний регистр
print(name.upper())           # ИВАНОВ АЛЕКСЕЙ ПЕТРОВИЧ
print(name.lower())           # иванов алексей петрович

# Разбить по пробелам
parts = name.split()
print(parts)                  # ['Иванов', 'Алексей', 'Петрович']
print(parts[0])               # Иванов (фамилия)

# Проверить содержимое
print("Иванов" in name)       # True
print(name.startswith("Ив"))  # True

# Заменить
clean = name.replace("Алексей", "А.")
print(clean)                  # Иванов А. Петрович
```

---

## f-строки: форматирование результата

```python
client = "Петрова М.С."
premium = 18540.5
risk = "средний"

# Форматированный вывод
print(f"Клиент: {client}")
print(f"Премия: {premium:,.0f} руб.")      # 18,540 руб.
print(f"Уровень риска: {risk.upper()}")    # СРЕДНИЙ
```

---

## Практика

```bash
python examples/01_string_basics.py
python examples/02_format_output.py
python examples/03_process_names.py
```

---

## Шпаргалка

```python
s = "привет мир"
len(s)              # длина: 9
s.upper()           # ПРИВЕТ МИР
s.lower()           # привет мир
s.split()           # ['привет', 'мир']
s.replace("мир","Python")   # привет Python
"мир" in s          # True
s.strip()           # убрать пробелы по краям
f"{s} и Python"   # строка с переменной
```

➡️ [Глава 03: Числа и логика](../03_numbers_logic/README.md)
