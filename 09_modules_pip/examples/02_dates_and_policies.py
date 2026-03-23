# Глава 09 — Работа с датами страховых полисов
from datetime import date, timedelta

def create_policy(client_name, start_date=None, duration_days=365):
    if start_date is None:
        start_date = date.today()
    end_date = start_date + timedelta(days=duration_days)
    return {
        "client": client_name,
        "start": str(start_date),
        "end": str(end_date),
        "active": date.today() <= end_date,
        "days_remaining": max(0, (end_date - date.today()).days),
    }

clients = ["Иванов А.П.", "Петрова М.С.", "Сидоров В.Н."]

for name in clients:
    policy = create_policy(name)
    status = "✅ Активен" if policy["active"] else "❌ Истёк"
    print(f"{name:<22} {status} | осталось {policy['days_remaining']} дней")
