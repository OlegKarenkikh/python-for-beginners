# 🐍 Python для всех — с нуля до первого скрипта

![CI](https://github.com/OlegKarenkikh/python-for-beginners/actions/workflows/ci.yml/badge.svg)
![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Уровень](https://img.shields.io/badge/уровень-абсолютный_новичок-green.svg)

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/course_roadmap.jpg" alt="Маршрут курса" width="90%"/>
</div>

> **Этот курс для вас, если:**
> - Вы никогда не писали код
> - Слова «переменная», «цикл», «функция» звучат страшно
> - Вы хотите автоматизировать рутину на работе
> - У вас есть 1–2 часа в день

Все примеры — из области **страхования и финансов** (расчёт премий, проверка заявлений, работа с документами).

---

## 🗺️ Маршрут (10 глав + финальный проект)

| Глава | Тема | Что умеете после | Время |
|---|---|---|---|
| [00](./00_why_python/) | Зачем Python? | Понять зачем учить | 20 мин |
| [01](./01_variables/) | Переменные и типы | Хранить данные | 1 ч |
| [02](./02_strings/) | Строки | Работать с текстом | 1 ч |
| [03](./03_numbers_logic/) | Числа и логика | Считать и сравнивать | 1 ч |
| [04](./04_conditions/) | Условия if/else | Принимать решения | 1.5 ч |
| [05](./05_loops/) | Циклы for/while | Обрабатывать много данных | 1.5 ч |
| [06](./06_functions/) | Функции | Не повторять код | 1.5 ч |
| [07](./07_lists_dicts/) | Списки и словари | Хранить наборы данных | 2 ч |
| [08](./08_files_json/) | Файлы и JSON | Читать/писать файлы | 1.5 ч |
| [09](./09_modules_pip/) | Модули и pip | Использовать библиотеки | 1 ч |
| [10](./10_final_project/) | 🏆 Финальный проект | Написать рабочий скрипт | 3 ч |

---

## 🚀 Быстрый старт (без установки)

### Вариант 1: GitHub Codespaces (рекомендуется)
1. Нажмите **`< > Code`** → **Codespaces** → **Create codespace on main**
2. Подождите ~2 минуты
3. Откройте терминал и введите: `python 01_variables/examples/01_first_variables.py`

### Вариант 2: На своём компьютере
```bash
git clone https://github.com/OlegKarenkikh/python-for-beginners
cd python-for-beginners
pip install -r requirements.txt
python 01_variables/examples/01_first_variables.py
```

---

## 📁 Структура каждой главы

```
NN_chapter/
  README.md          ← теория с аналогиями и иллюстрацией
  examples/          ← 3-5 рабочих примеров с комментариями
    01_example.py
    02_example.py
  exercises/         ← задания для практики
    exercise_01.py
    exercise_02.py
  answers/           ← решения (смотреть после попытки!)
    answer_01.py
  cheatsheet.md      ← шпаргалка главы
```

---

## 🧑‍💼 Сквозной персонаж: Ирина из «ПолисПлюс»

Ирина — менеджер страховой компании. Каждый день она:
- Считает страховые премии вручную (40+ клиентов)
- Проверяет заявления на выплату
- Заполняет таблицы Excel

К концу курса Ирина напишет скрипт, который делает всё это **автоматически**.

---

## 📚 Ресурсы

- [Глоссарий](./resources/glossary.md)
- [Шпаргалки по всем главам](./resources/cheatsheets/)
- [Частые ошибки](./resources/common_errors.md)
- [Рекомендованная литература](./resources/books.md)
