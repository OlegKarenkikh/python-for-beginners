for i in range(1, 11):
    policy = f"КАСКО-2024-{i:03d}"
    premium = i * 5_000
    print(f"{policy}   {premium:,} руб.")
