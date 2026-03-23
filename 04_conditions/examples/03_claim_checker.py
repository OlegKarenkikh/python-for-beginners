# Глава 04 — Проверка заявления на выплату

# Входные данные заявления
claim_amount = 85_000
days_since_accident = 28
has_police_report = True
has_photos = True
is_policy_active = True

# Проверяем условия
issues = []

if not is_policy_active:
    issues.append("Полис не активен")

if days_since_accident > 30:
    issues.append("Превышен срок подачи (30 дней)")

if not has_police_report:
    issues.append("Нет справки ГИБДД")

if not has_photos:
    issues.append("Нет фотографий с места ДТП")

if claim_amount > 500_000:
    issues.append("Сумма > 500 000 руб. — требуется экспертиза")

# Результат
if not issues:
    print("✅ Заявление прошло проверку — одобрено к выплате")
    print(f"   Сумма выплаты: {claim_amount:,} руб.")
else:
    print("❌ Заявление не прошло проверку:")
    for issue in issues:
        print(f"   • {issue}")
