#!/usr/bin/env python3
"""
Финальный проект: Калькулятор страховой премии ПолисПлюс
Применяет концепции глав 01–09.
"""

import json
import os
import statistics
from pathlib import Path


# ─── Коэффициенты ──────────────────────────────────────────
def age_factor(age: int) -> float:
    if age < 25:  return 1.5   # молодые водители (до 25)
    if age <= 35: return 1.1   # 25–35 лет
    if age < 55:  return 1.0   # 36–54 года (оптимальный возраст)
    if age < 70:  return 1.2   # 55–69 лет
    return 1.5                 # 70+ лет

def accident_factor(accidents: int) -> float:
    if accidents == 0: return 0.90
    if accidents == 1: return 1.15
    if accidents == 2: return 1.35
    return 1.0 + accidents * 0.25

def experience_factor(years: int) -> float:
    if years < 2: return 1.4
    if years < 5: return 1.1
    if years < 10: return 1.0
    return 0.85


# ─── Расчёт премии ─────────────────────────────────────────
def calculate_premium(client: dict, base_rate: float = 12_000.0) -> dict:
    """Рассчитывает премию и возвращает обогащённый словарь."""
    af = age_factor(client["age"])
    acf = accident_factor(client.get("accidents", 0))
    ef = experience_factor(client.get("experience", 0))

    premium = round(base_rate * af * acf * ef, 2)

    return {
        **client,
        "premium": premium,
        "age_factor": af,
        "accident_factor": acf,
        "experience_factor": ef,
        "policy_number": f"POL-2024-{client['id']:05d}",
    }


# ─── Загрузка / сохранение ─────────────────────────────────
def load_clients(path: str) -> list:
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_results(results: list, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)


# ─── Отчёт ─────────────────────────────────────────────────
def print_report(results: list) -> None:
    premiums = [r["premium"] for r in results]
    sep = "─" * 60

    print(sep)
    print(f"  СТРАХОВОЙ ПОРТФЕЛЬ — ПолисПлюс 2024")
    print(sep)
    print(f"  {'ФИО':<22} {'Возр':>4} {'Авар':>4} {'Стаж':>4} {'Премия':>12}")
    print(sep)

    for r in sorted(results, key=lambda x: x["premium"], reverse=True):
        print(f"  {r['name']:<22} {r['age']:>4} "
              f"{r.get('accidents', 0):>4} "
              f"{r.get('experience', 0):>4} "
              f"{r['premium']:>12,.0f} руб.")

    print(sep)
    print(f"  Полисов:       {len(premiums)}")
    print(f"  Сборов итого:  {sum(premiums):>14,.0f} руб.")
    print(f"  Средняя:       {statistics.mean(premiums):>14,.0f} руб.")
    print(f"  Медиана:       {statistics.median(premiums):>14,.0f} руб.")
    print(sep)


# ─── main ───────────────────────────────────────────────────
def main():
    base_dir = Path(__file__).parent
    clients = load_clients(base_dir / "data" / "clients.json")
    results = [calculate_premium(c) for c in clients]
    save_results(results, base_dir / "output" / "results.json")
    print_report(results)
    print(f"\n✅ Результаты сохранены в output/results.json")


if __name__ == "__main__":
    main()
