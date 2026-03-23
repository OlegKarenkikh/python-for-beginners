def get_discount(experience):
    if experience <= 2:
        return 0
    elif experience <= 5:
        return 5
    elif experience <= 10:
        return 10
    else:
        return 15

print(get_discount(1))   # 0
print(get_discount(4))   # 5
print(get_discount(8))   # 10
print(get_discount(15))  # 15
