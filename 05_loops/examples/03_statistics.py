# Глава 05 — Статистика по портфелю
import statistics

premiums = [15_200, 34_800, 8_500, 22_100, 19_600,
            45_000, 12_800, 28_400, 9_900, 33_100]

print("📊 Статистика страхового портфеля:")
print(f"  Полисов:    {len(premiums)}")
print(f"  Сборов:     {sum(premiums):,} руб.")
print(f"  Средняя:    {statistics.mean(premiums):,.0f} руб.")
print(f"  Медиана:    {statistics.median(premiums):,.0f} руб.")
print(f"  Минимум:    {min(premiums):,} руб.")
print(f"  Максимум:   {max(premiums):,} руб.")

# Сколько полисов выше среднего
avg = statistics.mean(premiums)
above = [p for p in premiums if p > avg]
print(f"  Выше средней: {len(above)} полисов ({len(above)/len(premiums)*100:.0f}%)")
