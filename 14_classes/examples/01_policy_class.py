# Глава 14 — Классы: полная модель страхового полиса
# Запуск: python examples/01_policy_class.py

from dataclasses import dataclass, field
from datetime import date, timedelta


# ── Базовый класс ──────────────────────────────────────────────────────────
class InsurancePolicy:
    """Страховой полис КАСКО."""

    VALID_YEARS = 1  # срок полиса в годах

    def __init__(self, owner: str, car: str, premium: float):
        self.owner    = owner
        self.car      = car
        self.premium  = premium
        self.active   = True
        self.start    = date.today()
        self.end      = self.start + timedelta(days=365 * self.VALID_YEARS)
        self._claims  = []   # история заявлений

    def deactivate(self):
        self.active = False

    def add_claim(self, amount: float, description: str):
        self._claims.append({"amount": amount, "desc": description, "date": date.today()})

    def total_claims(self) -> float:
        return sum(c["amount"] for c in self._claims)

    def __repr__(self):
        status = "активен" if self.active else "закрыт"
        return (
            f"Полис: {self.owner} | {self.car} | "
            f"{self.premium:,.0f} руб./год | {status}"
        )


# ── Наследование ───────────────────────────────────────────────────────────
class OsagoPoliciy(InsurancePolicy):
    """ОСАГО — расчёт по базовой ставке ЦБ."""
    BASE_RATE = 5_648  # рублей, базовая ставка ЦБ 2024

    def __init__(self, owner: str, car: str, kbm: float = 1.0):
        premium = self.BASE_RATE * kbm
        super().__init__(owner, car, premium)
        self.kbm = kbm    # коэффициент бонус-малус

    def __repr__(self):
        return super().__repr__() + f" | КБМ={self.kbm}"


# ── Dataclass ──────────────────────────────────────────────────────────────
@dataclass
class Claim:
    claim_id:    str
    amount:      float
    description: str
    approved:    bool  = False
    tags:        list  = field(default_factory=list)

    def approve(self):
        self.approved = True

    def reject(self):
        self.approved = False

    def __str__(self):
        status = "✅ ОДОБРЕНО" if self.approved else "⏳ на рассмотрении"
        return f"{self.claim_id}: {self.amount:>10,.0f} руб. — {status}"


# ── Демонстрация ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("DEMO: Классы и объекты — страховая компания ПолисПлюс")
    print("=" * 55)

    # Создаём полисы
    p1 = InsurancePolicy("Иванов А.П.",   "Toyota Camry",  14_400)
    p2 = InsurancePolicy("Петрова М.С.",  "Kia Rio",       21_600)
    p3 = OsagoPoliciy("Сидоров В.Н.",     "BMW 320i", kbm=0.8)

    policies = [p1, p2, p3]

    print("
📋 Портфель полисов:")
    for p in policies:
        print(f"  {p}")

    # Добавляем заявления
    p1.add_claim(45_000, "Царапина на двери")
    p1.add_claim(8_500,  "Разбитое зеркало")
    p2.add_claim(120_000, "ДТП на парковке")

    print(f"
💰 Заявления по полису Иванова: {p1.total_claims():,.0f} руб.")
    print(f"💰 Заявления по полису Петровой: {p2.total_claims():,.0f} руб.")

    # Dataclass Claim
    print("
📝 Заявления:")
    claims = [
        Claim("CLM-001", 45_000,  "Царапина на двери"),
        Claim("CLM-002", 120_000, "ДТП на парковке"),
        Claim("CLM-003", 8_500,   "Разбитое зеркало"),
        Claim("CLM-004", 67_000,  "Наезд на столб"),
        Claim("CLM-005", 200_000, "Угон"),
    ]

    # Одобряем суммы до 100 000
    for c in claims:
        if c.amount <= 100_000:
            c.approve()

    for c in claims:
        print(f"  {c}")

    approved = [c for c in claims if c.approved]
    total_approved = sum(c.amount for c in approved)
    print(f"
Одобрено: {len(approved)} заявлений на {total_approved:,.0f} руб.")
