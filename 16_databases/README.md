# Глава 16: Базы данных

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/db_evolution.jpg" width="95%"/></div>

> **Аналогия**: CSV-файл — это листок бумаги. SQLite — картотека. PostgreSQL — архив с тысячами папок и поисковиком.

---

## Зачем нужна база данных?

| Ситуация | Файл | База данных |
|---|---|---|
| 100 клиентов | OK | OK |
| 100 000 клиентов | медленно | быстро |
| Несколько пользователей одновременно | поломается | OK |
| Поиск по имени за 1 мс | нет | да (индекс) |
| Удалить без потери данных | опасно | транзакция |

---

## SQLite — начинаем здесь

SQLite — файл-база данных, входит в Python, ничего устанавливать не нужно.

```python
import sqlite3

conn = sqlite3.connect("insurance.db")
conn.row_factory = sqlite3.Row   # строки как словари
cur  = conn.cursor()
```

```python
# Создаём таблицы
cur.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        age     INTEGER,
        city    TEXT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS policies (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER REFERENCES clients(id),
        car       TEXT,
        premium   REAL,
        active    INTEGER DEFAULT 1
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS claims (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
        policy_id INTEGER REFERENCES policies(id),
        amount    REAL,
        status    TEXT DEFAULT 'pending'
    )
""")
conn.commit()
print("Таблицы созданы")
```

```python
# INSERT — добавление данных
cur.execute(
    "INSERT INTO clients (name, age, city) VALUES (?, ?, ?)",
    ("Иванов А.П.", 35, "Москва")
)
client_id = cur.lastrowid

cur.execute(
    "INSERT INTO policies (client_id, car, premium) VALUES (?, ?, ?)",
    (client_id, "BMW X5", 12000.0)
)
conn.commit()
print(f"Клиент добавлен, id={client_id}")
```

```python
# SELECT — чтение
rows = cur.execute("SELECT * FROM clients").fetchall()
for row in rows:
    print(dict(row))

# С фильтром
young = cur.execute(
    "SELECT name, age FROM clients WHERE age < ?", (25,)
).fetchall()
print("Молодые:", [dict(r) for r in young])
```

```python
# JOIN — соединяем таблицы
result = cur.execute("""
    SELECT c.name, c.age, p.car, p.premium
    FROM clients c
    JOIN policies p ON p.client_id = c.id
    WHERE p.active = 1
    ORDER BY p.premium DESC
""").fetchall()

for row in result:
    print(f"{row['name']} — {row['car']} — {row['premium']:,.0f} руб.")
```

```python
# Статистика по городам
stats = cur.execute("""
    SELECT c.city,
           COUNT(*)       AS clients,
           AVG(p.premium) AS avg_premium,
           SUM(p.premium) AS total
    FROM clients c
    JOIN policies p ON p.client_id = c.id
    GROUP BY c.city
    ORDER BY total DESC
""").fetchall()

print(f"{'Город':<12} {'Клиентов':>10} {'Средняя':>12} {'Итого':>14}")
print("-" * 52)
for row in stats:
    print(
        f"{row['city']:<12} {row['clients']:>10} "
        f"{row['avg_premium']:>12,.0f} {row['total']:>14,.0f}"
    )
```

```python
# UPDATE
cur.execute(
    "UPDATE policies SET premium = ? WHERE id = ?",
    (14400.0, 1)
)

# DELETE с условием
cur.execute("DELETE FROM claims WHERE status = 'rejected'")
conn.commit()
```

---

## PostgreSQL + psycopg2

```bash
pip install psycopg2-binary
```

```python
import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    host="localhost", port=5432,
    dbname="insurance", user="postgres", password="secret"
)
cur = conn.cursor(cursor_factory=RealDictCursor)

# Синтаксис тот же, только %s вместо ?
cur.execute(
    "INSERT INTO clients (name, age, city) VALUES (%s, %s, %s) RETURNING id",
    ("Петрова", 22, "СПб")
)
new_id = cur.fetchone()["id"]
conn.commit()
```

---

## SQLAlchemy ORM — классы = таблицы

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Session

engine = create_engine("sqlite:///insurance.db")

class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__ = "clients"
    id       = Column(Integer, primary_key=True)
    name     = Column(String(100))
    age      = Column(Integer)
    city     = Column(String(50))
    policies = relationship("Policy", back_populates="client")

class Policy(Base):
    __tablename__ = "policies"
    id        = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    car       = Column(String(100))
    premium   = Column(Float)
    client    = relationship("Client", back_populates="policies")

Base.metadata.create_all(engine)

# Работа без SQL
with Session(engine) as session:
    c = Client(name="Иванов", age=35, city="Москва")
    p = Policy(car="BMW X5", premium=12000.0, client=c)
    session.add_all([c, p])
    session.commit()
    
    young = session.query(Client).filter(Client.age < 25).all()
    for client in young:
        print(client.name, client.age)
```

---

## ClickHouse — аналитика на миллиардах строк

```bash
pip install clickhouse-connect
```

```python
import clickhouse_connect

client = clickhouse_connect.get_client(host="localhost", port=8123)

# Аналитический запрос (работает мгновенно на 10 млрд строк)
result = client.query("""
    SELECT city, avg(premium), count()
    FROM insurance.premiums
    GROUP BY city
    ORDER BY count() DESC
""")

for row in result.result_rows:
    print(row)
```

---

## Частые ошибки с базами данных

```python
# ОШИБКА 1: SQL-инъекция — НИКОГДА так не делайте!
name = input("Имя:")
cur.execute(f"SELECT * FROM clients WHERE name = '{name}'")
# Если name = "' OR '1'='1" — вернёт всех клиентов!

# ПРАВИЛЬНО — всегда параметры
cur.execute("SELECT * FROM clients WHERE name = ?", (name,))

# ОШИБКА 2: не закрыли соединение
conn = sqlite3.connect("insurance.db")
# ... работа ...
# забыли conn.close() — файл заблокирован

# ПРАВИЛЬНО — используйте with
with sqlite3.connect("insurance.db") as conn:
    cur = conn.cursor()
    # ...
    conn.commit()
# соединение закрыто автоматически

# ОШИБКА 3: забыли commit()
cur.execute("INSERT INTO clients ...")
# следующий SELECT не видит новую запись!

# ПРАВИЛЬНО
cur.execute("INSERT INTO clients ...")
conn.commit()   # сохранить изменения
```

---

## Упражнения

1. Создайте SQLite-базу с таблицами `clients`, `policies`, `claims`.
2. Добавьте 5 клиентов и по 1 полису каждому.
3. JOIN-запрос: имя клиента + его автомобиль + премия.
4. Статистика: средняя и максимальная премия по городам.
5. Класс `ClientDB` с методами `add()`, `get(id)`, `all()`, `delete(id)`.
