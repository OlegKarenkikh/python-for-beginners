has_passport = True
has_license = True
has_sts = False
has_valuation = False
is_new_car = False

missing = []
if not has_passport: missing.append("Паспорт")
if not has_license: missing.append("Водительское удостоверение")
if not has_sts: missing.append("СТС")
if not is_new_car and not has_valuation: missing.append("Справка об оценке авто")

if not missing:
    print("✅ Одобрено — все документы в наличии")
else:
    print("❌ Не хватает документов:")
    for doc in missing:
        print(f"  • {doc}")
