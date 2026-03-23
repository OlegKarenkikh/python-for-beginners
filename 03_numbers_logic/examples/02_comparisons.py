# Глава 03 — Сравнения и булева логика

# Параметры клиента
age = 22
experience = 2
accidents = 1
car_value = 500_000
city = "Казань"

# Флаги риска
is_young = age < 25
is_inexperienced = experience < 3
has_accidents = accidents > 0
high_value_car = car_value > 1_000_000
risk_city = city in ["Москва", "СПб", "Казань", "Екатеринбург"]

# Итоговый профиль
print("Профиль риска клиента:")
print(f"  Молодой водитель (< 25):   {is_young}")
print(f"  Малый стаж (< 3 лет):      {is_inexperienced}")
print(f"  Есть аварии:               {has_accidents}")
print(f"  Дорогое авто (> 1 млн):    {high_value_car}")
print(f"  Рискованный регион:        {risk_city}")

# Уровень риска
high_risk = (is_young and is_inexperienced) or (has_accidents and high_value_car)
print(f"\nВысокий риск: {high_risk}")
