# Глава 01 — Пример 2: Данные страхового клиента
# Запустите: python examples/02_insurance_client.py

# Данные клиента «ПолисПлюс»
client_name = "Петрова Мария Сергеевна"
client_age = 22
car_brand = "Toyota Camry"
driving_experience = 2       # лет стажа
accidents_count = 1          # количество аварий
is_vip = False               # VIP-клиент?

# Выводим карточку клиента
print("=" * 40)
print("КАРТОЧКА КЛИЕНТА — ПолисПлюс")
print("=" * 40)
print(f"ФИО:         {client_name}")
print(f"Возраст:     {client_age} лет")
print(f"Автомобиль:  {car_brand}")
print(f"Стаж:        {driving_experience} лет")
print(f"Аварии:      {accidents_count}")
print(f"VIP:         {is_vip}")
print("=" * 40)
