claims = [
    {"id": "CLM-001", "amount": 45_000, "approved": True},
    {"id": "CLM-002", "amount": 120_000, "approved": False},
    {"id": "CLM-003", "amount": 8_500, "approved": True},
    {"id": "CLM-004", "amount": 67_000, "approved": True},
    {"id": "CLM-005", "amount": 200_000, "approved": False},
    {"id": "CLM-006", "amount": 33_000, "approved": True},
]

approved = [c for c in claims if c["approved"]]
rejected = [c for c in claims if not c["approved"]]

print(f"Одобрено: {len(approved)}")
print(f"Сумма выплат: {sum(c['amount'] for c in approved):,} руб.")

if rejected:
    biggest_rejected = max(rejected, key=lambda c: c["amount"])
    print(f"Крупнейший отказ: {biggest_rejected['id']} — {biggest_rejected['amount']:,} руб.")
