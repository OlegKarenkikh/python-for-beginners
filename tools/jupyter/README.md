# Jupyter Notebook — рабочий стол для экспериментов

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/jupyter_interface.jpg" width="95%"/>
</div>

> **Jupyter** — среда, где код, результат и объяснение живут в одном документе.
> Идеально для обучения, отладки и экспериментов.

---

## Установка и запуск

```bash
pip install jupyterlab
jupyter lab          # откроет браузер на http://localhost:8888
```

Или в **VS Code**: расширение `Jupyter` (Microsoft) — notebooks прямо в редакторе.

---

## Два типа ячеек

| Тип | Что пишем | Переключить |
|---|---|---|
| **Code** | Python-код, результат под ячейкой | `Y` |
| **Markdown** | Текст, заголовки, объяснения | `M` |

```python
# Code cell — пишем код и жмём Shift+Enter
clients = ['Иванов', 'Петрова', 'Сидоров']
print(f'Клиентов: {len(clients)}')
# Клиентов: 3   <- вывод появляется сразу здесь
```

---

## Горячие клавиши

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/jupyter_shortcuts.jpg" width="95%"/>
</div>

### Запуск ячеек

| Комбинация | Действие |
|---|---|
| `Shift+Enter` | Запустить и перейти вниз |
| `Ctrl+Enter` | Запустить, остаться на месте |
| `Alt+Enter` | Запустить и добавить ячейку |

### Командный режим (`Esc`)

| Клавиша | Действие |
|---|---|
| `A` | Ячейка выше |
| `B` | Ячейка ниже |
| `D D` | Удалить ячейку |
| `Z` | Отменить |
| `M` | Markdown |
| `Y` | Code |

### Режим редактирования (`Enter`)

| Комбинация | Действие |
|---|---|
| `Tab` | Автодополнение |
| `Shift+Tab` | Документация по функции |
| `Ctrl+/` | Комментарий |

---

## Magic-команды

```python
# Замер времени одной строки
%timeit sum(range(1_000_000))

# Время всей ячейки
%%time
data = [i**2 for i in range(1_000_000)]

# Список переменных с типами
%whos

# Запустить .py файл
%run 01_variables/examples/01_first_variables.py

# Справка по функции
?sorted

# Команды терминала
!pip install requests
!ls -la

# Сохранить ячейку как файл
%%writefile my_script.py
print('Сохранено!')

# Автоперезагрузка модулей
%load_ext autoreload
%autoreload 2
```

---

## Отладка

### 1. print-отладка

```python
clients = [
    {'название': 'Иванов', 'возраст': 35},
    {'название': 'Петрова', 'возраст': 22},
]
for c in clients:
    print(f'DEBUG: {c}')
    premium = 12_000 * 1.5 if c['возраст'] < 25 else 12_000
    print(f'DEBUG: premium={premium}')
```

### 2. Маленькие ячейки

```python
# Ячейка 1
data = {'название': 'Иванов', 'возраст': 35}
```

```python
# Ячейка 2
print(type(data['возраст']))   # <class 'int'>
```

```python
# Ячейка 3
result = data['возраст'] * 1.5
print(result)  # 52.5
```

### 3. Встроенный дебаггер

```python
# После ошибки:
%debug
# Команды: p x (смотреть x), n (следующий), q (выход)
```

---

## Страховой пример

```python
# Ячейка 1: данные
import json
clients = [
    {'name': 'Иванов', 'age': 35, 'accidents': 0},
    {'name': 'Петрова', 'age': 22, 'accidents': 1},
]
print(f'Загружено: {len(clients)} клиентов')
```

```python
# Ячейка 2: функция
def calc(age, accidents=0):
    p = 12_000 * 1.5 if age < 25 else 12_000
    return round(p * (1 + accidents * 0.2) if accidents else p, 2)
print(calc(22, 1))   # 21600.0
print(calc(35))      # 12000.0
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
print(f'Средняя: {sum(p)/len(p):,.0f} руб.')
print(f'Итого:   {sum(p):,.0f} руб.')
```

---

## Jupyter vs .py

| Задача | Jupyter | .py файл |
|---|---|---|
| Учёба, эксперименты | ✅ | — |
| Отладка непонятного кода | ✅ | — |
| FastAPI-сервер | — | ✅ |
| Агент в продакшн | — | ✅ |

---

## Упражнения

1. Установите JupyterLab и создайте первый notebook
2. Напишите расчёт премии и запустите `Shift+Enter`
3. Добавьте Markdown-ячейку с объяснением формулы
4. Используйте `%timeit` — сравните list comprehension и цикл `for`
5. Запустите `%run 01_variables/examples/01_first_variables.py` из notebook
