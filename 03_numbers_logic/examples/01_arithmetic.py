# Глава 03 — Арифметика в страховании

# Базовые данные
car_value = 2_400_000     # стоимость авто
kasko_rate = 0.045        # тариф КАСКО 4.5%
osago_base = 4_118        # базовая ставка ОСАГО (ЦБ РФ)
age_coeff = 1.4           # коэффициент возраста
territory_coeff = 1.8     # коэффициент территории (Москва)
accident_coeff = 1.0      # КБМ

# Расчёт
kasko = round(car_value * kasko_rate, 2)
osago = round(osago_base * age_coeff * territory_coeff * accident_coeff, 2)
total = kasko + osago

print(f"{'КАСКО':20} {kasko:>15,.2f} руб.")
print(f"{'ОСАГО':20} {osago:>15,.2f} руб.")
print(f"{'─'*38}")
print(f"{'Итого в год':20} {total:>15,.2f} руб.")
print(f"{'Ежемесячно':20} {total/12:>15,.2f} руб.")
