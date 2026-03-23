# Глава 08 — Чтение и запись файлов
import os

# Создаём файл с клиентами
clients_data = """Иванов А.П.|35|14400
Петрова М.С.|22|21600
Сидоров В.Н.|68|18000
Козлова Е.В.|31|12800
"""

with open("clients.txt", "w", encoding="utf-8") as f:
    f.write(clients_data)

print("Файл создан. Читаем обратно:")
print("-" * 40)

total = 0
count = 0
with open("clients.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, age, premium = line.split("|")
        total += int(premium)
        count += 1
        print(f"  {name:<20} {age:>3} лет  {int(premium):>8,} руб.")

print("-" * 40)
print(f"Итого: {count} клиентов, {total:,} руб.")

os.remove("clients.txt")  # чистим за собой
