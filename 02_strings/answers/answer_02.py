email = "agent.ivanov@polisplus.ru"
is_valid = "@" in email and (email.endswith(".ru") or email.endswith(".com"))
print("Валидный" if is_valid else "Невалидный")
