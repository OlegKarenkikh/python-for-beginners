# 🧠 Глава 13: Строим агентов

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/agent_architecture.jpg" width="95%"/>
</div>

> **Агент** = LLM + набор инструментов + цикл: вызвать → проверить → повторить.
> Агент сам решает, какой инструмент вызвать для решения задачи.

---

## Концепция: чем агент отличается от обычного скрипта

| Обычный скрипт | Агент |
|---|---|
| Жёстко задан порядок шагов | Сам выбирает шаги |
| Не может адаптироваться | Реагирует на неожиданные данные |
| Один инструмент | Несколько инструментов на выбор |
| Нет рассуждений | LLM объясняет каждое решение |

---

## Шаг 1: Инструменты — обычные Python-функции

```python
import json
import requests

# Инструмент 1: расчёт премии
def calculate_premium(age: int, accidents: int = 0) -> dict:
    base = 12_000
    premium = base * 1.5 if age < 25 else base
    if accidents > 0:
        premium *= 1 + accidents * 0.2
    return {"premium": round(premium, 2), "currency": "RUB"}

# Инструмент 2: поиск клиента
CLIENTS_DB = [
    {"id": 1, "name": "Иванов А.П.",  "age": 35, "accidents": 0},
    {"id": 2, "name": "Петрова М.С.", "age": 22, "accidents": 1},
    {"id": 3, "name": "Сидоров К.Д.", "age": 47, "accidents": 0},
]

def find_client(name: str) -> dict:
    for c in CLIENTS_DB:
        if name.lower() in c["name"].lower():
            return c
    return {"error": f"Клиент {name!r} не найден"}

# Инструмент 3: проверка документов
def check_documents(client_id: int) -> dict:
    docs_ok = {1: True, 2: False, 3: True}
    ok = docs_ok.get(client_id, False)
    return {"documents_complete": ok, "missing": [] if ok else ["справка о ДТП"]}
```

---

## Шаг 2: Описание инструментов для LLM

```python
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "find_client",
            "description": "Найти клиента по имени в базе данных",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Имя или фамилия клиента"}
                },
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_premium",
            "description": "Рассчитать страховую премию по возрасту",
            "parameters": {
                "type": "object",
                "properties": {
                    "age":       {"type": "integer", "description": "Возраст водителя"},
                    "accidents": {"type": "integer", "description": "Количество аварий за 3 года"},
                },
                "required": ["age"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "check_documents",
            "description": "Проверить наличие документов клиента",
            "parameters": {
                "type": "object",
                "properties": {
                    "client_id": {"type": "integer", "description": "ID клиента"}
                },
                "required": ["client_id"],
            },
        },
    },
]
```

---

## Шаг 3: Реестр инструментов

```python
# Словарь: имя_функции -> сама_функция
TOOL_REGISTRY = {
    "find_client":        find_client,
    "calculate_premium":  calculate_premium,
    "check_documents":    check_documents,
}

def execute_tool(name: str, arguments: dict):
    fn = TOOL_REGISTRY.get(name)
    if fn is None:
        return {"error": f"Инструмент {name!r} не найден"}
    return fn(**arguments)
```

---

## Шаг 4: Агентный цикл (ReAct loop)

```python
import json

def run_agent(user_task: str, max_steps: int = 10) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "Ты — агент страховой компании ПолисПлюс. "
                "Для решения задач используй доступные инструменты. "
                "Сначала найди клиента, затем рассчитай премию и проверь документы."
            ),
        },
        {"role": "user", "content": user_task},
    ]

    for step in range(max_steps):
        print(f"[Шаг {step+1}]")

        # Вызов LLM
        response = requests.post(
            "http://localhost:11434/v1/chat/completions",
            json={
                "model": "llama3.2",
                "messages": messages,
                "tools": TOOLS,
                "temperature": 0.0,
            },
            timeout=60,
        ).json()

        choice = response["choices"][0]
        message = choice["message"]
        messages.append(message)

        # LLM решила использовать инструмент
        if message.get("tool_calls"):
            for call in message["tool_calls"]:
                tool_name = call["function"]["name"]
                tool_args = json.loads(call["function"]["arguments"])

                print(f"  Инструмент: {tool_name}({tool_args})")
                result = execute_tool(tool_name, tool_args)
                print(f"  Результат:  {result}")

                # Добавляем результат инструмента в историю
                messages.append({
                    "role": "tool",
                    "tool_call_id": call["id"],
                    "content": json.dumps(result, ensure_ascii=False),
                })

        # LLM дала финальный ответ
        elif choice["finish_reason"] == "stop":
            return message["content"]

    return "Превышено максимальное количество шагов"

# Запуск
result = run_agent("Обработай заявку клиента Петрова: рассчитай премию и проверь документы")
print("\nФинальный ответ агента:")
print(result)
```

---

## Шаг 5: Интеграция с FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AgentRequest(BaseModel):
    task: str

@app.post("/agent/run")
def agent_endpoint(req: AgentRequest):
    result = run_agent(req.task)
    return {"task": req.task, "result": result}
```

Теперь агент доступен через API:
```bash
curl -X POST "http://localhost:8000/agent/run" \
     -H "Content-Type: application/json" \
     -d '{"task": "Обработай заявку клиента Сидоров"}'
```

---

## Готовые фреймворки (следующий шаг)

| Фреймворк | Когда использовать |
|---|---|
| **smolagents** (HuggingFace) | Простые агенты, open-source модели |
| **LangGraph** | Сложные multi-agent системы |
| **AutoGen** (Microsoft) | Multi-agent диалоги |
| **CrewAI** | Команды агентов с ролями |

Код из этой главы — фундамент для понимания любого из них.

---

## Упражнения

1. Добавьте инструмент `get_risk_history(client_id)` — список прошлых заявлений
2. Напишите агента, который автоматически одобряет простые заявки и эскалирует сложные
3. Сохраняйте историю каждого запуска агента в JSON-файл


---

## ❓ Вопросы которые возникают при изучении

---

### 🙋 Агент — это робот? Программа?

Агент — это просто Python-программа, которая:
1. Получает задачу на словах («Рассчитай премию для Иванова»)
2. Спрашивает LLM: «что делать дальше?»
3. LLM отвечает: «вызови инструмент find_client»
4. Программа вызывает функцию, передаёт результат обратно LLM
5. LLM отвечает: «вызови calculate_premium»
6. Повторяет пока LLM не скажет «готово»

```python
# Весь агент — это цикл:
while True:
    response = ask_llm(messages)
    if response == "FINAL":
        break
    result = call_tool(response["tool"], response["args"])
    messages.append(result)  # передаём результат обратно
```

---

### 🙋 Почему LLM не может просто вызвать функцию напрямую?

LLM — это языковая модель, она генерирует текст. Она не запускает код.
Агентский паттерн — обходной путь: LLM пишет *описание* что нужно вызвать,
Python читает это описание и вызывает реальную функцию.

```
Пользователь: "Рассчитай премию для Иванова 35 лет"
       ↓
LLM: {"tool": "calculate_premium", "args": {"age": 35}}  ← текст, не вызов!
       ↓
Python: calculate_premium(age=35)  ← реальный вызов
       ↓
LLM: получает результат {"premium": 12000} и формулирует ответ
```

---

### 🙋 Что такое `TOOL_REGISTRY` — зачем нужен этот словарь?

**Аллегория: «Сетевой фильтр с наклейками»**

Представь, что твои функции — это электроприборы:
- `calculate_premium` — **Чайник**
- `find_client` — **Радио**
- `check_documents` — **Лампа**

`TOOL_REGISTRY` — это сетевой фильтр (удлинитель) с **наклейками** над каждой розеткой:

```python
TOOL_REGISTRY = {
    "calculate_premium": calculate_premium,  # наклейка "чайник" → прибор Чайник
    "find_client":       find_client,        # наклейка "радио"  → прибор Радио
    "check_documents":   check_documents,    # наклейка "лампа"  → прибор Лампа
}
```

LLM — это человек, который **не умеет** включать приборы, но умеет читать наклейки.
Она говорит: «Мне нужно рассчитать страховую премию — включи **calculate_premium** с параметрами age=35».

Python делает три шага:
1. `name = "calculate_premium"` — LLM дала имя инструмента (прочитала наклейку)
2. `func = TOOL_REGISTRY[name]` — нашли функцию по имени (взяли прибор с полки)
3. `func(**args)` — вызвали функцию с данными (включили прибор в розетку)

---

### 🙋 Что значит `tool_map[action["tool"]](**action["args"])`?

Это три вещи вместе:

```python
# 1. tool_map["calculate_premium"] → функция calculate_premium
# 2. **{"age": 35, "accidents": 0} → разворачивает dict в аргументы
# 3. calculate_premium(age=35, accidents=0) → вызов функции

tool_map = {
    "calculate_premium": calculate_premium,
    "find_client": find_client,
}

action = {"tool": "calculate_premium", "args": {"age": 35}}

result = tool_map[action["tool"]](**action["args"])
# то же что: calculate_premium(age=35)
```

`**dict` — «распаковка словаря в именованные аргументы».

---

### 🙋 ReAct, smolagents, LangGraph — нужно выбирать одно?

На старте — нет. Вот шкала сложности:

| Для чего | Инструмент |
|---|---|
| Понять концепцию | `requests` + чистый Python (этот курс) |
| Быстрый прототип | `smolagents` (HuggingFace, минимум кода) |
| Сложные workflows с состоянием | `LangGraph` |
| Мультиагентные команды | `CrewAI` |

Начните с чистого Python — это даст понимание что происходит «под капотом» любого фреймворка.

---

### 🙋 `temperature: 0` — что это?

Температура управляет «случайностью» ответов модели:
- `0` — детерминировано, одинаковые ответы на одинаковые вопросы (для агентов — лучше)
- `0.7` — балансирует творчество и предсказуемость (для чата — норм)
- `1.0+` — хаотично, творчески, но непредсказуемо (для генерации идей)

Для агентов всегда ставьте `temperature=0` — агент должен делать одно и то же действие,
а не угадывать какой инструмент вызвать «креативно».

---

### 🙋 Что если LLM вернула неправильный JSON?

Это **самая частая проблема** в агентах. Три уровня защиты:

```python
import json, re

raw = llm_response.strip()

# Уровень 1: прямой парсинг
try:
    action = json.loads(raw)
except json.JSONDecodeError:
    pass

# Уровень 2: извлечь JSON из текста
match = re.search(r'\{.*\}', raw, re.DOTALL)
if match:
    try:
        action = json.loads(match.group())
    except:
        pass

# Уровень 3: вернуть в LLM с просьбой исправить
if not action:
    messages.append({"role": "user", "content": "Ошибка: верни ТОЛЬКО JSON без лишнего текста"})
```

В продакшне агенты всегда имеют все три уровня.
