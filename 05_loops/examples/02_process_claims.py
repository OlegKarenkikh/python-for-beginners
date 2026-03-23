# Глава 05 — Обработка пакета заявлений
claims = [
    {"id": "CLM-001", "amount": 45_000, "days": 15, "docs": True},
    {"id": "CLM-002", "amount": 120_000, "days": 35, "docs": True},
    {"id": "CLM-003", "amount": 8_500, "days": 5, "docs": False},
    {"id": "CLM-004", "amount": 67_000, "days": 20, "docs": True},
]

approved = []
rejected = []

for claim in claims:
    issues = []
    if claim["days"] > 30:
        issues.append("пропущен срок подачи")
    if not claim["docs"]:
        issues.append("нет документов")

    if issues:
        rejected.append((claim["id"], ", ".join(issues)))
    else:
        approved.append(claim)

print(f"✅ Одобрено: {len(approved)}")
total = sum(c["amount"] for c in approved)
print(f"   Сумма выплат: {total:,} руб.")

print(f"\n❌ Отклонено: {len(rejected)}")
for claim_id, reason in rejected:
    print(f"   {claim_id}: {reason}")
