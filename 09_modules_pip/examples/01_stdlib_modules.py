# Глава 09 — Стандартные модули Python
import statistics
import json
import os
from datetime import date, timedelta

# statistics — статистика портфеля
premiums = [15_200, 34_800, 8_500, 22_100, 19_600, 45_000, 12_800]

print("📊 Статистика портфеля:")
print(f"  Среднее:  {statistics.mean(premiums):,.0f} руб.")
print(f"  Медиана:  {statistics.median(premiums):,.0f} руб.")
print(f"  Станд. откл.: {statistics.stdev(premiums):,.0f} руб.")

# datetime — даты полисов
today = date.today()
expiry = today + timedelta(days=365)
print(f"\n📅 Дата оформления: {today}")
print(f"   Дата истечения:   {expiry}")
print(f"   Осталось дней:    {(expiry - today).days}")
