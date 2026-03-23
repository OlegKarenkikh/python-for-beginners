insured_value = 3_500_000
base_rate = 0.038
alarm_discount = 0.005
young_driver_surcharge = 0.012

final_rate = base_rate - alarm_discount + young_driver_surcharge
base_premium = round(insured_value * base_rate, 2)
final_premium = round(insured_value * final_rate, 2)

print(f"Базовый взнос:     {base_premium:>12,.2f} руб.")
print(f"Итоговый взнос:    {final_premium:>12,.2f} руб.")
print(f"Ежемесячно:        {final_premium/12:>12,.2f} руб.")
