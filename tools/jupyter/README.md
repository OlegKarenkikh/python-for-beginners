# Jupyter Notebook

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/jupyter_interface.jpg" width="95%"/></div>

> Jupyter — среда, где код, результат и объяснение живут в одном документе.

---

## Установка

```bash
pip install jupyterlab
jupyter lab
```

VS Code: расширение Jupyter (Microsoft).

---

## Два типа ячеек

| Тип | Что | Переключить |
|---|---|---|
| Code | Python-код | Y |
| Markdown | Текст | M |

---

## Горячие клавиши

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/jupyter_shortcuts.jpg" width="95%"/></div>

| Комбинация | Действие |
|---|---|
| Shift+Enter | Запустить и перейти вниз |
| Ctrl+Enter | Запустить, остаться |
| Alt+Enter | Запустить + новая ячейка |
| Esc | Командный режим |
| A | Ячейка выше |
| B | Ячейка ниже |
| D D | Удалить |
| Z | Отменить |
| Tab | Автодополнение |

---

## Magic-команды

```python
%timeit sum(range(1_000_000))
%whos
%run script.py
?sorted
!pip install requests
%debug
```

---

## Страховой пример

```python
# Ячейка 1
import json
clients = [
    {'name':'Ivanov','age':35,'accidents':0},
    {'name':'Petrova','age':22,'accidents':1},
]
print('loaded:', len(clients))
```

```python
# Ячейка 2
def calc(age, accidents=0):
    p = 12000 * 1.5 if age < 25 else 12000
    return round(p*(1+accidents*0.2) if accidents else p, 2)
print(calc(22,1))  # 21600.0
```

```python
# Ячейка 3
for c in clients:
    c['premium'] = calc(c['age'], c['accidents'])
print(json.dumps(clients, ensure_ascii=False, indent=2))
```

```python
# Ячейка 4
p = [c['premium'] for c in clients]
print(f'Total: {sum(p):,.0f} rub')
```

---

## Когда Jupyter, когда .py

| Задача | Jupyter | .py |
|---|---|---|
| Учёба | OK | — |
| FastAPI | — | OK |

---

## Упражнения

1. Установите JupyterLab
2. Напишите расчёт премии, запустите Shift+Enter
3. Добавьте Markdown-ячейку
4. %timeit: list comprehension vs for
5. %run script.py
