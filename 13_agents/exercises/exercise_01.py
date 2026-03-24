# Глава 13 — Упражнение
# Добавьте агенту инструмент get_risk_history(client_id)
# который возвращает список прошлых заявлений клиента.
# Затем запустите агента с задачей:
# "Посмотри историю заявлений клиента 1 и реши нужна ли проверка СБ"

RISK_HISTORY = {
    1: [{"year": 2022, "amount": 45_000, "cause": "царапина"},
        {"year": 2023, "amount": 8_500,  "cause": "зеркало"}],
    2: [{"year": 2023, "amount": 120_000, "cause": "ДТП"}],
    3: [],
}

# Ваш код:
# def get_risk_history(client_id: int) -> dict:
#     history = RISK_HISTORY.get(client_id, [])
#     total = sum(h["amount"] for h in history)
#     return {"client_id": client_id, "claims_count": len(history),
#             "total_amount": total, "history": history}

# Зарегистрируйте инструмент в TOOL_REGISTRY и запустите агента
