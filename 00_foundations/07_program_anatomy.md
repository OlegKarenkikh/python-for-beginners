# 🔬 Анатомия Python-программы

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/program_anatomy.jpg" alt="Анатомия Python-программы" width="95%"/>
</div>

---

## Полный пример с пояснениями

```python
# ① Импорты — всегда в начале файла
import json
from datetime import date

# ② Константы — ЗАГЛАВНЫМИ БУКВАМИ, не меняются
BASE_RATE = 12_000
MAX_PAYOUT = 500_000
COMPANY = "ПолисПлюс"

# ③ Функция — начинается с def, заканчивается return
def calculate_premium(age: int, accidents: int = 0) -> float:
    # ④ Docstring — документация функции
    """
    Рассчитывает годовую страховую премию.

    Args:
        age: возраст водителя
        accidents: количество аварий за 3 года

    Returns:
        Страховая премия в рублях
    """
    # ⑤ Тело функции — отступ 4 пробела
    premium = BASE_RATE

    if age < 25:                    # условие
        premium *= 1.5              # умножение с присваиванием
    elif age > 65:
        premium *= 1.3

    if accidents > 0:
        premium *= (1 + accidents * 0.2)

    return round(premium, 2)        # ⑥ возврат результата


# ⑦ Основная часть программы
def main():
    """Точка входа — запускается первой."""
    clients = [
        {"name": "Иванов А.П.", "age": 35, "accidents": 0},
        {"name": "Петрова М.С.", "age": 22, "accidents": 1},
    ]

    # ⑧ Цикл — перебираем каждого клиента
    for client in clients:
        premium = calculate_premium(
            age=client["age"],
            accidents=client["accidents"],
        )
        # ⑨ Вывод — f-строка с форматированием
        print(f"{client['name']}: {premium:,.0f} руб./год")


# ⑩ Точка входа — стандартный паттерн Python
if __name__ == "__main__":
    main()
```

---

## Что означает каждая часть

| Номер | Элемент | Правило |
|---|---|---|
| ① | `import` | В начале файла, до остального кода |
| ② | Константы | `CAPS_SNAKE_CASE`, вверху после импортов |
| ③ | `def` | Имя функции — `snake_case`, скобки обязательны |
| ④ | Docstring | Тройные кавычки, первая строка тела функции |
| ⑤ | Тело функции | Отступ 4 пробела от `def` |
| ⑥ | `return` | Что функция возвращает вызывающему |
| ⑦ | `main()` | Необязательно, но хорошая практика |
| ⑧ | `for` | Отступ 4 пробела, двоеточие в конце строки |
| ⑨ | `print()` | f-строка для форматированного вывода |
| ⑩ | `if __name__` | Позволяет импортировать файл без запуска |

---

## Минимальная программа

```python
# Это полная валидная программа Python
print("Привет, Ирина!")
```

---

## Типичная структура файла

```
my_script.py
├── Импорты (import)
├── Константы (BASE_RATE = ...)
├── Вспомогательные функции (def helper_func():)
├── Основная функция (def main():)
└── if __name__ == "__main__": main()
```
