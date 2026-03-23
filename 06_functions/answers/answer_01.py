def format_policy_card(client):
    sep = "─" * 38
    return (
        f"{sep}\n"
        f"  СТРАХОВОЙ ПОЛИС — ПолисПлюс\n"
        f"{sep}\n"
        f"  ФИО:    {client['name']}\n"
        f"  Возраст:{client['age']} лет\n"
        f"  Авто:   {client['car']}\n"
        f"  Полис:  {client['policy_number']}\n"
        f"  Премия: {client['premium']:,} руб./год\n"
        f"{sep}"
    )

test_client = {"name": "Волков Денис Андреевич", "age": 41,
               "car": "Kia Sportage", "premium": 18_400, "policy_number": "POL-2024-00157"}
print(format_policy_card(test_client))
