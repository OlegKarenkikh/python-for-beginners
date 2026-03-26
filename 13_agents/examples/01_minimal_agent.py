"""
Глава 13: Минимальный агент — LLM + инструменты + цикл
Требует: ollama serve + ollama pull llama3.2
"""
import requests
import json


# ── Инструменты ─────────────────────────────────────────────────────────────

CLIENTS_DB = [
    {"id": 1, "name": "Иванов А.П.",  "age": 35, "accidents": 0},
    {"id": 2, "name": "Петрова М.С.", "age": 22, "accidents": 1},
    {"id": 3, "name": "Сидоров К.Д.", "age": 47, "accidents": 0},
]


def find_client(name: str) -> dict:
    for c in CLIENTS_DB:
        if name.lower() in c["name"].lower():
            return c
    return {"error": f"Клиент не найден: {name!r}"}


def calculate_premium(age: int, accidents: int = 0) -> dict:
    base = 12_000
    premium = base * 1.5 if age < 25 else base
    if accidents > 0:
        premium *= 1 + accidents * 0.2
    return {"premium": round(premium, 2), "currency": "RUB"}


def check_documents(client_id: int) -> dict:
    docs = {1: True, 2: False, 3: True}
    ok = docs.get(client_id, False)
    return {
        "complete": ok,
        "missing": [] if ok else ["справка о ДТП"],
    }


TOOL_REGISTRY = {
    "find_client":       find_client,
    "calculate_premium": calculate_premium,
    "check_documents":   check_documents,
}

# ── Как работает вызов инструмента ──────────────────────────────────────────
# LLM возвращает имя функции и аргументы, Python выполняет в три шага:
#
#   1. fn_name = "calculate_premium"          # имя функции (от LLM)
#   2. fn_args = {"age": 35, "accidents": 0}  # аргументы  (от LLM)
#
#   3. func   = TOOL_REGISTRY[fn_name]        # находим функцию по имени
#      result = func(**fn_args)               # вызываем с именованными аргументами
#
# Запись TOOL_REGISTRY[fn_name](**fn_args) — это шаг 3, записанный в одну строку.

TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "find_client",
            "description": "Найти клиента по имени",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_premium",
            "description": "Рассчитать страховую премию",
            "parameters": {
                "type": "object",
                "properties": {
                    "age":       {"type": "integer"},
                    "accidents": {"type": "integer"},
                },
                "required": ["age"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "check_documents",
            "description": "Проверить документы клиента по его ID",
            "parameters": {
                "type": "object",
                "properties": {"client_id": {"type": "integer"}},
                "required": ["client_id"],
            },
        },
    },
]


# ── Агентный цикл ────────────────────────────────────────────────────────────

def run_agent(task: str, max_steps: int = 8) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "Ты — агент страховой компании ПолисПлюс. "
                "Используй инструменты для ответа на запрос. "
                "Сначала найди клиента, затем рассчитай премию и проверь документы."
            ),
        },
        {"role": "user", "content": task},
    ]

    for step in range(max_steps):
        print(f"  [Шаг {step + 1}] Вызов LLM...")

        resp = requests.post(
            "http://localhost:11434/v1/chat/completions",
            json={
                "model": "llama3.2",
                "messages": messages,
                "tools": TOOLS_SCHEMA,
                "temperature": 0.0,
            },
            timeout=60,
        ).json()

        msg = resp["choices"][0]["message"]
        messages.append(msg)

        if msg.get("tool_calls"):
            for call in msg["tool_calls"]:
                fn_name = call["function"]["name"]
                fn_args = json.loads(call["function"]["arguments"])
                print(f"  → {fn_name}({fn_args})")

                result = TOOL_REGISTRY[fn_name](**fn_args)
                print(f"  ← {result}")

                messages.append({
                    "role": "tool",
                    "tool_call_id": call["id"],
                    "content": json.dumps(result, ensure_ascii=False),
                })

        elif resp["choices"][0]["finish_reason"] == "stop":
            return msg["content"]

    return "Превышен лимит шагов"


def main():
    tasks = [
        "Обработай заявку Петрова: рассчитай премию и проверь документы",
        "Что нужно сделать для клиента Иванов?",
    ]
    for task in tasks:
        print(f"\n{'='*60}")
        print(f"Задача: {task}")
        print(f"{'='*60}")
        result = run_agent(task)
        print(f"\nОтвет агента:\n{result}")


if __name__ == "__main__":
    main()
