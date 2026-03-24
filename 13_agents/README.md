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
