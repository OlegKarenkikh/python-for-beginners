# 🐍 Python для всех — от нуля до агентов

![CI](https://github.com/OlegKarenkikh/python-for-beginners/actions/workflows/ci.yml/badge.svg)
![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/course_roadmap.jpg" width="90%"/>
</div>

> Все примеры — из страхования и финансов.
> Финальная цель: **FastAPI-сервис + вызов LLM + агент**.

---

## 🗂️ Справочник основ

| Тема | Файл |
|---|---|
| 4 типа данных | [01_data_types.md](./00_foundations/01_data_types.md) |
| Именование переменных | [02_naming_rules.md](./00_foundations/02_naming_rules.md) |
| Стиль кода PEP 8 | [03_code_style.md](./00_foundations/03_code_style.md) |
| f-строки: все форматы | [04_fstrings.md](./00_foundations/04_fstrings.md) |
| Операторы | [05_operators.md](./00_foundations/05_operators.md) |
| Ключевые слова (35 шт.) | [06_keywords.md](./00_foundations/06_keywords.md) |
| Анатомия программы | [07_program_anatomy.md](./00_foundations/07_program_anatomy.md) |
| Встроенные функции | [08_builtins.md](./00_foundations/08_builtins.md) |
| Как читать ошибки | [09_errors.md](./00_foundations/09_errors.md) |
| ⭐ Шпаргалка одним листом | [CHEATSHEET.md](./00_foundations/CHEATSHEET.md) |

---

## 🗺️ Маршрут курса

### Фундамент Python (главы 00–10)

| Глава | Тема | Время |
|---|---|---|
| [00](./00_why_python/) | Зачем Python? | 20 мин |
| [01](./01_variables/) | Переменные и типы | 1 ч |
| [02](./02_strings/) | Строки | 1 ч |
| [03](./03_numbers_logic/) | Числа и логика | 1 ч |
| [04](./04_conditions/) | Условия if/elif/else | 1.5 ч |
| [05](./05_loops/) | Циклы for/while | 1.5 ч |
| [06](./06_functions/) | Функции def | 1.5 ч |
| [07](./07_lists_dicts/) | **Списки, словари** + срезы, comprehension | 2.5 ч |
| [08](./08_files_json/) | **Файлы и JSON** — полный разбор | 2 ч |
| [09](./09_modules_pip/) | Модули и pip | 1 ч |
| [10](./10_final_project/) | 🏆 Финальный проект | 3 ч |

### Прикладной Python (главы 11–13)

| Глава | Тема | Что получите |
|---|---|---|
| [11](./11_fastapi/) | **FastAPI** — REST API | Рабочий API-сервер |
| [12](./12_llm_inference/) | **LLM-инференс** (Ollama / vLLM) | Вызов LLM из кода |
| [13](./13_agents/) | **Агенты** — LLM + инструменты | Автономный агент |

---

## 🚀 Быстрый старт

### GitHub Codespaces (без установки)
1. **Code** → **Codespaces** → **Create codespace on main**
2. Подождите ~2 минуты
3. `python 01_variables/examples/01_first_variables.py`

### Локально
```bash
git clone https://github.com/OlegKarenkikh/python-for-beginners
cd python-for-beginners
pip install -r requirements.txt
python 01_variables/examples/01_first_variables.py
```

### Для глав 11-13 дополнительно:
```bash
pip install fastapi uvicorn pydantic requests
# Для LLM:
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
```

---

## 🧑‍💼 Персонаж: Ирина из «ПолисПлюс»

Каждый урок — реальная задача Ирины:
от расчёта первой премии вручную до полноценного агента,
который автоматически обрабатывает 40+ заявлений в день.

---

## 📚 Ресурсы

- [Глоссарий](./resources/glossary.md)
- [Частые ошибки](./resources/common_errors.md)
- [Книги и сайты](./resources/books.md)
