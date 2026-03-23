# Глава 06 — Функции валидации заявления

def validate_age(age):
    """Проверяет допустимый возраст страхователя."""
    return 18 <= age <= 80

def validate_amount(amount, max_amount=500_000):
    """Проверяет сумму претензии."""
    return 0 < amount <= max_amount

def validate_days(days, limit=30):
    """Проверяет срок подачи заявления."""
    return days <= limit

def validate_claim(age, amount, days):
    """Комплексная проверка заявления. Возвращает (ok, issues)."""
    issues = []
    if not validate_age(age): issues.append(f"Возраст {age} вне диапазона 18–80")
    if not validate_amount(amount): issues.append(f"Сумма {amount:,} вне допустимого диапазона")
    if not validate_days(days): issues.append(f"Прошло {days} дней > 30")
    return len(issues) == 0, issues

# Тест
claims = [
    (35, 45_000, 15),
    (16, 10_000, 5),
    (40, 45_000, 35),
    (55, 600_000, 10),
]

for age, amount, days in claims:
    ok, issues = validate_claim(age, amount, days)
    status = "✅ ОДОБРЕНО" if ok else "❌ ОТКЛОНЕНО"
    print(f"{status} (возр={age}, сумма={amount:,}, дней={days})")
    for issue in issues:
        print(f"  • {issue}")
