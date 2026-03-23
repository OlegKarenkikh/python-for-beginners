# Глава 06 — Упражнение 1
# Напишите функцию format_policy_card(client_dict),
# которая принимает словарь с данными клиента и
# возвращает отформатированную строку-карточку.

def format_policy_card(client):
    """
    client: dict с ключами: name, age, car, premium, policy_number
    Возвращает: многострочную строку с карточкой полиса
    """
    pass  # ваш код

test_client = {
    "name": "Волков Денис Андреевич",
    "age": 41,
    "car": "Kia Sportage",
    "premium": 18_400,
    "policy_number": "POL-2024-00157"
}

print(format_policy_card(test_client))
