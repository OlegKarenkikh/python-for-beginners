# Глава 02 — Строки: основные операции
full_name = "Козлова Ирина Владимировна"
print("Длина имени:", len(full_name))
print("Верхний регистр:", full_name.upper())
parts = full_name.split()
print(f"Фамилия: {parts[0]}, Имя: {parts[1]}")
print(f"Инициалы: {parts[0]} {parts[1][0]}.{parts[2][0]}.")
