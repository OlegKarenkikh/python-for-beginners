# 🪐 Jupyter Notebook — рабочий стол для экспериментов

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/jupyter_interface.jpg" alt="Jupyter Notebook интерфейс" width="95%"/>
</div>

> **Jupyter Notebook** — интерактивная среда, где код, результаты и объяснения
> живут в одном документе. Идеально для обучения и экспериментов.

---

## Установка

```bash
pip install jupyter notebook
# Или более современный JupyterLab (рекомендуется)
pip install jupyterlab
```

**Запуск:**
```bash
jupyter lab        # современный интерфейс (рекомендуется)
jupyter notebook   # классический интерфейс
```
Откроется браузер на `http://localhost:8888`

---

## Ячейки — главная концепция

Notebook состоит из **ячеек** двух типов:

| Тип | Содержимое | Переключить |
|---|---|---|
| **Code** | Python-код, результат появляется снизу | `Y` в командном режиме |
| **Markdown** | Текст, заголовки, формулы | `M` в командном режиме |

```python
# Code cell — пишем код и запускаем Shift+Enter
clients = ['Иванов', 'Петрова', 'Сидоров']
print(f'Клиентов: {len(clients)}')
# Вывод появляется прямо здесь ↓
# Клиентов: 3
```

---

## Горячие клавиши (самые важные)

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/jupyter_shortcuts.jpg" alt="Горячие клавиши Jupyter" width="95%"/>
</div>

### Запуск ячеек

| Комбинация | Действие |
|---|---|
| `Shift + Enter` | Запустить ячейку и перейти к следующей |
| `Ctrl + Enter` | Запустить ячейку, остаться на месте |
| `Alt + Enter` | Запустить и создать новую ячейку ниже |

### Командный режим (нажмите `Esc`)

| Клавиша | Действие |
|---|---|
| `A` | Новая ячейка **выше** (Above) |
| `B` | Новая ячейка **ниже** (Below) |
| `D D` | Удалить ячейку (два нажатия D) |
| `Z` | Отменить удаление |
| `M` | Сменить на Markdown |
| `Y` | Сменить на Code |
| `L` | Показать/скрыть номера строк |

### Режим редактирования (нажмите `Enter`)

| Комбинация | Действие |
|---|---|
| `Tab` | Автодополнение (после `.`) |
| `Shift + Tab` | Документация по функции |
| `Ctrl + /` | Закомментировать строку |
| `Ctrl + Z` | Отменить в ячейке |

---

## Magic-команды — суперсила Jupyter

Magic-команды начинаются с `%` (одна строка) или `%%` (вся ячейка).

```python
# ⏱️ Замер времени выполнения
%timeit sum(range(1_000_000))
# 13.4 ms ± 124 µs per loop

# ⏱️ Время всей ячейки
%%time
data = [i**2 for i in range(1_000_000)]
# Wall time: 87.3 ms

# 📋 Список всех переменных
%who

# 🔍 Подробный список с типами и размерами
%whos

# 🚀 Запустить .py файл
%run 01_variables/examples/01_first_variables.py

# 💾 Записать содержимое ячейки в файл
%%writefile my_script.py
print('Привет!')

# 📖 Справка по функции (можно также: help(len))
?len
??sorted  # с исходным кодом

# 🖥️ Команды терминала (без выхода из Jupyter)
!pip install requests
!ls -la
!python --version

# 📊 Встроенные графики (matplotlib)
%matplotlib inline

# 🔁 Автоперезагрузка модулей (удобно при разработке)
%load_ext autoreload
%autoreload 2
```

---

## Отладка — как найти ошибку

### Способ 1: print-отладка (самый простой)
```python
clients = [
    {'name': 'Иванов', 'age': 35},
    {'name': 'Петрова', 'age': 22},
]

for c in clients:
    print(f'DEBUG: обрабатываем {c}')  # ← смотрим что внутри
    premium = 12_000 * 1.5 if c['age'] < 25 else 12_000
    print(f'DEBUG: premium={premium}')
    c['premium'] = premium
```

### Способ 2: отдельная ячейка для проверки
```python
# Ячейка 1: создаём данные
data = {'name': 'Иванов', 'age': 35}

# Ячейка 2: проверяем тип
print(type(data['age']))   # <class 'int'>

# Ячейка 3: пробуем операцию
result = data['age'] * 1.5
print(result)  # 52.5
```

### Способ 3: встроенный дебаггер
```python
%debug  # запускает после ошибки — появляется интерактивная консоль
```

```python
# Или так — точка останова внутри функции
def calculate(age):
    import pdb; pdb.set_trace()  # ← остановится здесь
    return 12_000 * 1.5 if age < 25 else 12_000
```

---

## Удобные расширения (установка)

```bash
# Для JupyterLab — уже встроено большинство
pip install jupyterlab

# nbformat — конвертация .ipynb в .py
pip install nbconvert
jupyter nbconvert --to script notebook.ipynb

# Виджеты — интерактивные слайдеры и кнопки
pip install ipywidgets
```

---

## Структура папки для работы

```
my_notebooks/
├── 01_variables.ipynb      ← урок 1
├── 02_strings.ipynb        ← урок 2
├── sandbox.ipynb           ← черновик для экспериментов
├── premium_calc.ipynb      ← рабочий проект
└── data/
    └── clients.json
```

---

## Jupyter vs .py файл: когда что использовать

| Ситуация | Jupyter Notebook | .py файл |
|---|---|---|
| Изучение и эксперименты | ✅ Идеально | — |
| Пошаговый разбор данных | ✅ | — |
| Отладка непонятного кода | ✅ | — |
| Финальный скрипт/API | — | ✅ |
| FastAPI-сервер | — | ✅ |
| Агент в продакшн | — | ✅ |
| Презентация результатов | ✅ | — |

---

## VS Code + Jupyter (альтернатива)

Если уже используете VS Code — notebooks работают прямо в редакторе:

1. Установите расширение **Jupyter** (Microsoft)
2. Создайте файл `notebook.ipynb`
3. Выберите ядро Python
4. Все те же ячейки, горячие клавиши и magic-команды работают

---

## Упражнения

1. Установите JupyterLab и создайте первый notebook
2. Напишите ячейку с расчётом премии — запустите `Shift+Enter`
3. Добавьте Markdown-ячейку с объяснением
4. Используйте `%timeit` чтобы сравнить скорость list comprehension vs цикла for
5. Запустите `%run 01_variables/examples/01_first_variables.py` из notebook