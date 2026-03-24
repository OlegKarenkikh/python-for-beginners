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


---

## ❓ Вопросы которые возникают при изучении

<div align="center">
<img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/qa_files_json.png" alt="Вопросы о файлах и JSON" width="95%"/>
</div>

---

### 🙋 Что такое `as f` в `with open(...) as f:`?

`as f` — псевдоним (alias). Вы говорите: «объект файла называть `f` в этом блоке».
Имя может быть любым, но `f` — стандартное соглашение Python.

```python
with open("clients.json", "r", encoding="utf-8") as f:
    data = json.load(f)   # f — объект файла с методами read/write
# ← файл автоматически закрыт при выходе из блока with
```

---

### 🙋 Все режимы открытия файла:

```python
"r"  — чтение (по умолчанию). Ошибка если файл не существует.
"w"  — запись. Создаёт файл. ⚠️ ПЕРЕЗАПИСЫВАЕТ если существует!
"a"  — добавление (append). Добавляет в конец, не стирает.
"x"  — создать новый. Ошибка если файл уже существует.
"rb" — чтение в бинарном режиме (для изображений, PDF, Excel)
"wb" — запись в бинарном режиме
```

> ⚠️ **Самая опасная ловушка:** `"w"` молча сотрёт файл если он существует!
> Для добавления логов используйте `"a"`.

---

### 🙋 `json.dump` vs `json.dumps` — в чём разница?

Мнемоника: `s` в конце = **S**tring (работа со строками).

```python
# Без s — работа с ФАЙЛОМ
json.dump(data, file)     # записать в файл
json.load(file)           # прочитать из файла

# С s — работа со СТРОКОЙ
json.dumps(data)          # словарь → строка
json.loads(text)          # строка  → словарь
```

Применение:
```python
# dumps — когда нужно передать данные по сети или в логи
text = json.dumps({"status": "ok"}, ensure_ascii=False)
logger.info(f"Результат: {text}")

# dump — когда нужно сохранить в файл
with open("result.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

---

### 🙋 `ensure_ascii=False` — что это?

По умолчанию json экранирует все не-ASCII символы (кириллицу):

```python
data = {"name": "Иванов"}

json.dumps(data)                           # '{"name": "\u0418\u0432\u0430\u043d\u043e\u0432"}'
json.dumps(data, ensure_ascii=False)       # '{"name": "Иванов"}'
```

**Всегда** указывайте `ensure_ascii=False` при работе с кириллицей.

---

### 🙋 Python конвертирует `True/False` автоматически?

Да, `json.dump`/`json.load` делают это прозрачно:

```
Python → JSON:   True  → true   |  False → false  |  None → null
JSON   → Python: true  → True   |  false → False  |  null → None
```

```python
data = {"active": True, "deleted": None}
text = json.dumps(data)         # '{"active": true, "deleted": null}'
back = json.loads(text)         # {'active': True, 'deleted': None}
print(back["active"] is True)   # True
```
