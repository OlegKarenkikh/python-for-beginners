# 📁 Глава 08: Второй взгляд — Файлы и JSON ловушки

---

## Страшная сторона: файл без закрытия

```python
# ОПАСНО — файл останется открытым при ошибке
f = open("clients.json", "r", encoding="utf-8")
data = json.load(f)
# ... если здесь ошибка — f.close() не вызовется!
f.close()

# ПРАВИЛЬНО — with гарантирует закрытие
with open("clients.json", "r", encoding="utf-8") as f:
    data = json.load(f)
# файл закрыт автоматически, даже при ошибке
```

---

## Страшная сторона: JSON и типы данных

```python
import json

# Python → JSON → Python: типы могут измениться!
data = {
    "id":      42,
    "name":    "Иванов",
    "premium": 12000.0,
    "active":  True,
    "extra":   None
}

json_str = json.dumps(data)
restored = json.loads(json_str)

# None → null → None  ✓
# True → true → True  ✓
# int/float → number → int/float  ✓ (но могут стать float!)
# tuple → array → list  ← тип изменился!

original = (1, 2, 3)
as_json  = json.dumps(original)   # "[1, 2, 3]"
back     = json.loads(as_json)    # [1, 2, 3] — список, не кортеж!
```

---

## Страшная сторона: кириллица в JSON

```python
client = {"name": "Иванов А.П.", "city": "Москва"}

# По умолчанию Python экранирует не-ASCII символы
json.dumps(client)
# '{"name": "\u0418\u0432\u0430\u043d\u043e\u0432..."}'  — нечитаемо!

# Правильно — ensure_ascii=False
json.dumps(client, ensure_ascii=False, indent=2)
# {
#   "name": "Иванов А.П.",
#   "city": "Москва"
# }
```

---

## Безопасное чтение JSON из неизвестного источника

```python
import json
from pathlib import Path

def load_claims(filepath: str) -> list:
    path = Path(filepath)
    
    if not path.exists():
        print(f"Файл не найден: {filepath}")
        return []
    
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Ошибка разбора JSON: {e}")
        return []
    except PermissionError:
        print(f"Нет доступа к файлу: {filepath}")
        return []
    
    if not isinstance(data, list):
        print("Ожидали список, получили что-то другое")
        return []
    
    return data

claims = load_claims("claims.json")
print(f"Загружено {len(claims)} заявлений")
```
