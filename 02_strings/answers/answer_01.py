full_name = "Новикова Светлана Борисовна"
parts = full_name.split()
short = f"{parts[0]} {parts[1][0]}.{parts[2][0]}."
policy = f"{parts[0][:3].upper()}-{parts[1][0]}-{parts[2][0]}"
print(short)    # Новикова С.Б.
print(policy)   # НОВ-С-Б (или адаптировать)
