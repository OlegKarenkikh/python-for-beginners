payouts = [12_000, 85_000, 34_500, 9_800, 156_000,
           45_200, 7_300, 92_400, 28_700, 61_000]

total = sum(payouts)
average = total / len(payouts)
maximum = max(payouts)
big_claims = [p for p in payouts if p > 50_000]

print(f"Сумма выплат:     {total:,} руб.")
print(f"Средняя выплата:  {average:,.0f} руб.")
print(f"Максимум:         {maximum:,} руб.")
print(f"Выплат > 50 000:  {len(big_claims)}")
