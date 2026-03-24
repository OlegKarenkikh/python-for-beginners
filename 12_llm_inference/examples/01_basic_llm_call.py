"""
Глава 12: Вызов LLM через HTTP (Ollama / vLLM)
Требует: ollama serve  +  ollama pull llama3.2
"""
import requests
import json

LLM_BASE_URL = "http://localhost:11434"
MODEL = "llama3.2"


def ask_llm(prompt: str, system: str = "") -> str:
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    resp = requests.post(
        f"{LLM_BASE_URL}/v1/chat/completions",
        json={"model": MODEL, "messages": messages, "temperature": 0.1},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def analyze_claim_json(claim_text: str) -> dict:
    prompt = (
        "Проанализируй страховое заявление. Верни ТОЛЬКО JSON:\n"
        '{"risk_level": "low|medium|high", '
        '"recommendation": "approve|investigate|reject", '
        '"reason": "краткое объяснение на русском"}\n\n'
        f"Заявление: {claim_text}"
    )
    text = ask_llm(prompt, system="Ты — страховой аналитик.")
    start = text.find("{")
    end = text.rfind("}") + 1
    if start == -1:
        return {"error": "LLM не вернула JSON", "raw": text}
    return json.loads(text[start:end])


def main():
    print("=== Тест 1: простой вопрос ===")
    answer = ask_llm(
        "Что такое страховая франшиза? Ответь в 2 предложениях.",
        system="Ты — ассистент страховой компании ПолисПлюс.",
    )
    print(answer)

    print("\n=== Тест 2: анализ заявления → JSON ===")
    claim = "Toyota Camry, ДТП на перекрёстке, есть справка ГИБДД, свидетели есть, ущерб 85 000 руб."
    result = analyze_claim_json(claim)
    print(json.dumps(result, ensure_ascii=False, indent=2))

    print("\n=== Тест 3: сложное заявление ===")
    claim2 = "BMW X7, повреждения без свидетелей, ночь, парковка без камер, ущерб 550 000 руб."
    result2 = analyze_claim_json(claim2)
    print(json.dumps(result2, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
