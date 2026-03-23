# Глава 02 — Форматирование страховых данных
client = "Волков Денис Андреевич"
policy_number = "POL-2024-00842"
premium = 34_800.0
coverage = 1_500_000.0

print("=" * 45)
print(f"  СТРАХОВОЙ ПОЛИС — ПолисПлюс")
print("=" * 45)
print(f"  Страхователь:  {client}")
print(f"  Номер полиса:  {policy_number}")
print(f"  Премия:        {premium:>12,.0f} руб.")
print(f"  Страховая сумма: {coverage:>10,.0f} руб.")
print("=" * 45)
