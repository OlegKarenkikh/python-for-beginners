# 🤖 Глава 12: Вызов LLM-моделей через API

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/llm_inference_flow.jpg" width="95%"/>
</div>

> LLM-модель — это программа, которая понимает текст и отвечает на него.
> Вызываем её как обычный HTTP API через `requests`.

---

## Что такое инференс-сервер

**Инференс-сервер** — программа, которая загружает LLM-модель и принимает запросы.

| Сервер | Когда использовать | Запуск |
|---|---|---|
| **Ollama** | Локально, разработка, CPU/GPU | `ollama serve` |
| **vLLM** | Продакшн, высокая нагрузка, GPU | `vllm serve model` |
| **llama.cpp server** | Слабое железо, quantized модели | `./server -m model.gguf` |

Все три сервера имеют **совместимый с OpenAI API** — один и тот же код.

---

## Установка Ollama (самый простой старт)

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Загрузить модель (3.8GB)
ollama pull llama3.2

# Запустить сервер (в отдельном терминале)
ollama serve
```

---

## Первый вызов: requests (прямой API)

```python
import requests
import json

# Ollama API (аналогично для vLLM)
url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2",
    "prompt": "Клиент Иванов 35 лет, 0 аварий. Одобрить страховку КАСКО?",
    "stream": False,
}

response = requests.post(url, json=payload)
data = response.json()

print(data["response"])
```

---

## OpenAI-совместимый API (работает с Ollama и vLLM)

```python
import requests

# Этот формат работает с Ollama, vLLM, OpenAI и любым совместимым сервером
def ask_llm(prompt: str, model: str = "llama3.2",
            base_url: str = "http://localhost:11434") -> str:
    url = f"{base_url}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Ты — ассистент страховой компании ПолисПлюс."},
            {"role": "user",   "content": prompt},
        ],
        "temperature": 0.1,
        "max_tokens": 500,
    }
    response = requests.post(url, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Использование
answer = ask_llm("Клиент 22 года, 1 авария. Какой риск?")
print(answer)
```

---

## Структурированный ответ (JSON из LLM)

```python
import requests
import json

def analyze_claim(claim_text: str) -> dict:
    prompt = f"""Проанализируй страховое заявление и верни JSON:
{{
  "risk_level": "low|medium|high",
  "recommendation": "approve|investigate|reject",
  "reason": "краткое объяснение"
}}

Заявление: {claim_text}

Верни ТОЛЬКО JSON, без лишнего текста."""

    url = "http://localhost:11434/v1/chat/completions"
    response = requests.post(url, json={
        "model": "llama3.2",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
    }, timeout=60)

    text = response.json()["choices"][0]["message"]["content"]

    # Парсим JSON из ответа
    start = text.find("{")
    end = text.rfind("}") + 1
    return json.loads(text[start:end])

# Пример
claim = "BMW X5, парковка, ночь, свидетелей нет, ущерб 450 000 руб"
result = analyze_claim(claim)
print(result["recommendation"])  # investigate
print(result["reason"])
```

---

## Потоковый ответ (streaming)

```python
import requests
import json

def stream_answer(prompt: str):
    url = "http://localhost:11434/api/generate"
    response = requests.post(
        url,
        json={"model": "llama3.2", "prompt": prompt, "stream": True},
        stream=True,
    )
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            print(chunk["response"], end="", flush=True)
            if chunk.get("done"):
                break
    print()  # перевод строки

stream_answer("Объясни что такое страховая франшиза")
```

---

## vLLM — запуск для продакшн

```bash
# Установка
pip install vllm

# Запуск сервера
vllm serve Qwen/Qwen2.5-7B-Instruct \
    --host 0.0.0.0 \
    --port 8000 \
    --max-model-len 8192
```

Python-код **идентичен** — только меняем `base_url`:
```python
answer = ask_llm("Вопрос...", model="Qwen/Qwen2.5-7B-Instruct",
                  base_url="http://localhost:8000")
```

---

## Упражнения

1. Напишите функцию `summarize_claim(text)` — кратко суммирует заявление (3 предложения)
2. Сделайте функцию `classify_risk(client_data)` — возвращает `{"risk": "low|medium|high"}`
3. Оберните вызов LLM в FastAPI эндпоинт `POST /analyze-claim`


---

## ❓ Вопросы которые возникают при изучении

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/qa_llm_agents.png" alt="Вопросы о LLM и агентах" width="95%"/>
</div>

---

### 🙋 Что такое `"role"` в messages? Зачем системе знать роль?

OpenAI-совместимые API (Ollama, vLLM) ожидают разговор как список сообщений с ролями:

```python
messages = [
    {"role": "system", "content": "Ты страховой агент. Отвечай только по делу."},
    {"role": "user",   "content": "Посчитай премию для водителя 22 лет"},
    {"role": "assistant", "content": "Для 22 лет базовая премия умножается на 1.5..."},
    {"role": "user",   "content": "А для 35 лет?"},   # следующий вопрос
]
```

- `system` — инструкции для модели (роль, правила, формат ответа)
- `user` — сообщение от пользователя
- `assistant` — предыдущий ответ модели (для сохранения контекста диалога)

---

### 🙋 `stream=True` — что значит «поток»?

**Без stream:** модель думает 10 секунд, потом выдаёт весь ответ сразу.
**С stream:** модель выдаёт ответ по кускам по мере генерации — как живой набор текста.

```python
# Без stream — ждёте до конца
response = client.chat.completions.create(
    model="llama3", messages=messages
)
print(response.choices[0].message.content)

# С stream — выводите по мере получения
for chunk in client.chat.completions.create(
    model="llama3", messages=messages, stream=True
):
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

---

### 🙋 LLM всегда возвращает JSON? Что если нет?

Нет! Даже если попросить — модель иногда добавляет пояснения:
«Конечно! Вот JSON: `{...}`». Реальный код всегда оборачивает в `try/except`:

```python
import json, re

raw = response.choices[0].message.content

# Попытка 1: прямой парсинг
try:
    result = json.loads(raw)
except json.JSONDecodeError:
    # Попытка 2: извлечь JSON из текста
    match = re.search(r'\{.*\}', raw, re.DOTALL)
    if match:
        result = json.loads(match.group())
    else:
        result = {"error": "invalid response", "raw": raw}
```

---

### 🙋 Паттерн ReAct — как Python «понимает» что LLM думает?

Python не понимает мышление. ReAct — это паттерн **промптинга**:
в системном промпте модели объяснено отвечать строго в формате:

```
Thought: [что думаю о задаче]
Action: {"tool": "calculate_premium", "args": {"age": 35}}
```

Python парсит этот текст и извлекает JSON из строки `Action:`.

```python
import re, json

response_text = \"\"\"Thought: Нужно рассчитать премию для возраста 35.
Action: {\"tool\": \"calculate_premium\", \"args\": {\"age\": 35}}\"\"\"\"

match = re.search(r'Action:\s*(\{.*?\})', response_text, re.DOTALL)
if match:
    action = json.loads(match.group(1))
    tool_name = action["tool"]      # "calculate_premium"
    args = action["args"]           # {"age": 35}
```

---

### 🙋 `tool_map = {t["name"]: t["func"] for t in tools}` — функция как значение словаря?

Да! В Python функции — это объекты. Их можно класть куда угодно.

```python
def check_fraud(claim): ...
def calculate(claim): ...

tools = [
    {"name": "check_fraud", "func": check_fraud},
    {"name": "calculate",   "func": calculate},
]

tool_map = {t["name"]: t["func"] for t in tools}
# {"check_fraud": <function check_fraud>, "calculate": <function calculate>}

# Динамический вызов по имени:
tool_map["check_fraud"](my_claim)   # вызвали нужную функцию
```

Это паттерн «реестр инструментов» — основа агентных систем.
