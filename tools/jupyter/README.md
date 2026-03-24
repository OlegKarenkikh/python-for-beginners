# Jupyter Notebook

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/jupyter_interface.jpg" width="95%"/></div>

> Jupyter — среда, где код, результат и объяснение живут в одном документе.
> Идеально для обучения, отладки и экспериментов.

---

## Установка

```bash
pip install jupyterlab
jupyter lab
```

Или в **VS Code**: расширение `Jupyter` (Microsoft).

---

## Два типа ячеек

| Тип | Что | Переключить |
|---|---|---|
| **Code** | Python-код | `Y` |
| **Markdown** | Текст | `M` |

```python
# Code cell
clients = ['Иванов', 'Петрова']
print(len(clients))  # 2
```

---

## Горячие клавиши

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/jupyter_shortcuts.jpg" width="95%"/></div>

| Комбинация | Действие |
|---|---|
| `Shift+Enter` | Запустить и перейти вниз |
| `Ctrl+Enter` | Запустить, остаться |
| `Alt+Enter` | Запустить + новая ячейка |
| `Esc` | Командный режим |
| `A` | Ячейка выше |
| `B` | Ячейка ниже |
| `D D` | Удалить |
| `Z` | Отменить |
| `M` | Markdown |
| `Y` | Code |
| `Tab` | Автодополнение |
| `Shift+Tab` | Документация |

---

## Magic-команды

```python
%timeit sum(range(1_000_000))   # замер времени
%%time                          # время ячейки
%whos                           # список переменных
%run script.py                  # запустить .py
?sorted                         # справка
!pip install requests           # терминал
%%writefile my.py               # сохранить ячейку
%load_ext autoreload            # автоперезагрузка
%autoreload 2
%debug                          # дебаггер
```

---

## Отладка

**1. print-отладка:**
```python
for c in clients:
    print('DEBUG:', c)
    premium = 12000 * 1.5 if c['age'] < 25 else 12000
    print('DEBUG premium:', premium)
```

**2. Маленькие ячейки** — проверяем каждый шаг отдельно.

**3. `%debug`** — после ошибки открывает интерактивную консоль.

---

## Страховой пример (четыре ячейки)

```python
# Ячейка 1: данные
import json
clients = [
    {'name': 'Ivanov', 'age': 35, 'accidents': 0},
    {'name': 'Petrova', 'age': 22, 'accidents': 1},
]
print('loaded:', len(clients))
```

```python
# Ячейка 2: функция
def calc(age, accidents=0):
    p = 12000 * 1.5 if age < 25 else 12000
    return round(p * (1 + accidents * 0.2) if accidents else p, 2)
print(calc(22, 1))  # 21600.0
```

```python
# Ячейка 3: применяем
for c in clients:
    c['premium'] = calc(c['age'], c['accidents'])
print(json.dumps(clients, ensure_ascii=False, indent=2))
```

```python
# Ячейка 4: статистика
p = [c['premium'] for c in clients]
print(f'Total: {sum(p):,.0f} rub')
```

---

## Jupyter vs .py

| Задача | Jupyter | .py |
|---|---|---|
| Учёба, эксперименты | OK | — |
| Отладка | OK | — |
| FastAPI, агент | — | OK |

---

## Упражнения

1. Установите JupyterLab и создайте первый notebook
2. Напишите расчёт премии и запустите `Shift+Enter`
3. Markdown-ячейка с объяснением
4. `%timeit` — list comprehension vs цикл for
5. `%run 01_variables/examples/01_first_variables.py`
