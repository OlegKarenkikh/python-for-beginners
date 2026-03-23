# Глава 06 — Калькулятор страховой премии

def get_age_factor(age):
    if age < 25: return 1.5
    elif age < 35: return 1.1
    elif age < 55: return 1.0
    elif age < 70: return 1.2
    else: return 1.5

def get_accident_factor(accidents):
    if accidents == 0: return 0.9     # бонус-малус
    elif accidents == 1: return 1.15
    elif accidents == 2: return 1.35
    else: return 1.0 + accidents * 0.25

def get_experience_factor(years):
    if years < 2: return 1.4
    elif years < 5: return 1.1
    elif years < 10: return 1.0
    else: return 0.85

def calculate_total_premium(base, age, accidents, experience):
    """Итоговая премия с учётом всех коэффициентов."""
    total = (base
             * get_age_factor(age)
             * get_accident_factor(accidents)
             * get_experience_factor(experience))
    return round(total, 2)

# Тестируем на 3 клиентах
test_cases = [
    ("Иванов А.П.", 35, 0, 12),
    ("Петрова М.С.", 22, 1, 2),
    ("Сидоров В.Н.", 68, 0, 30),
]

BASE = 12_000
print(f"{'Клиент':<20} {'Возр':>4} {'Авар':>4} {'Стаж':>4} {'Премия':>12}")
print("-" * 50)
for name, age, acc, exp in test_cases:
    p = calculate_total_premium(BASE, age, acc, exp)
    print(f"{name:<20} {age:>4} {acc:>4} {exp:>4} {p:>12,.0f} руб.")
