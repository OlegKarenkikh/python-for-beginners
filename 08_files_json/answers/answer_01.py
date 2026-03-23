import json, os

claims = [
    {"id": "CLM-001", "client": "Иванов", "amount": 45_000, "approved": True},
    {"id": "CLM-002", "client": "Петрова", "amount": 120_000, "approved": False},
    {"id": "CLM-003", "client": "Сидоров", "amount": 33_000, "approved": True},
]

with open("claims.json", "w", encoding="utf-8") as f:
    json.dump(claims, f, ensure_ascii=False, indent=2)

with open("claims.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

approved = [c for c in loaded if c["approved"]]
print(f"Одобрено: {len(approved)}")
for c in approved:
    print(f"  {c['id']} — {c['client']}: {c['amount']:,} руб.")
print(f"Итого выплат: {sum(c['amount'] for c in approved):,} руб.")

os.remove("claims.json")
