# Глава 19: Streamlit

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/streamlit_dashboard.jpg" width="95%"/></div>

> **Аналогия**: Streamlit — как Excel, но красивее и умнее. Пишете Python-скрипт, получаете веб-приложение. Без HTML, CSS, JavaScript.

---

## Зачем Streamlit?

| Задача | Без Streamlit | С Streamlit |
|---|---|---|
| Показать таблицу данных | HTML + CSS + JS | `st.dataframe(df)` |
| Построить график | Plotly + frontend | `st.bar_chart(data)` |
| Фильтр по городу | React-компонент | `st.selectbox(...)` |
| Загрузить файл | Multipart upload | `st.file_uploader(...)` |

---

## Установка

```bash
pip install streamlit pandas plotly
streamlit run app.py
# Открывается: http://localhost:8501
```

---

## Первые 10 минут

```python
# app.py
import streamlit as st

st.title("ПолисПлюс — дашборд")
st.write("Добро пожаловать!")

# Числа
st.metric("Активных полисов", 847, delta="+12 за неделю")

# Текст с разметкой
st.markdown("**Жирный** текст, *курсив*, `код`")

# Предупреждение
st.warning("3 заявления ожидают проверки")
st.success("Система работает нормально")
st.error("Соединение с БД прервано")
```

```bash
streamlit run app.py
```

---

## Работа с данными

```python
import streamlit as st
import pandas as pd
import json

st.title("База клиентов")

# --- Боковая панель (sidebar) ---
with st.sidebar:
    st.header("Фильтры")
    city_filter = st.selectbox("Город", ["Все", "Москва", "СПб", "Казань"])
    max_age     = st.slider("Максимальный возраст", 18, 80, 65)
    show_risk   = st.checkbox("Только группа риска", value=False)

# --- Данные ---
clients = [
    {"name": "Иванов А.П.",  "age": 35, "city": "Москва", "premium": 12000, "accidents": 0},
    {"name": "Петрова М.С.", "age": 22, "city": "СПб",    "premium": 18000, "accidents": 1},
    {"name": "Сидоров К.Д.", "age": 47, "city": "Москва", "premium": 12000, "accidents": 0},
    {"name": "Орлова Е.В.",  "age": 19, "city": "Казань", "premium": 18000, "accidents": 0},
    {"name": "Козлов В.И.",  "age": 60, "city": "Москва", "premium": 20280, "accidents": 2},
]

df = pd.DataFrame(clients)

# Применяем фильтры
if city_filter != "Все":
    df = df[df["city"] == city_filter]

df = df[df["age"] <= max_age]

if show_risk:
    df = df[df["accidents"] > 0]

# --- Метрики ---
col1, col2, col3 = st.columns(3)
col1.metric("Клиентов",     len(df))
col2.metric("Средняя премия", f"{df['premium'].mean():,.0f} руб." if len(df) else "—")
col3.metric("Итого сборов",   f"{df['premium'].sum():,.0f} руб." if len(df) else "—")

# --- Таблица ---
st.subheader("Список клиентов")
st.dataframe(df, use_container_width=True)
```

---

## Графики

```python
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    "city":    ["Москва", "СПб", "Казань", "Новосибирск"],
    "clients": [450, 210, 87, 63],
    "premium": [12500, 11800, 13200, 11200]
})

st.subheader("Клиенты по городам")

# Встроенный bar chart
st.bar_chart(df.set_index("city")["clients"])

# Plotly — интерактивно
fig = px.scatter(
    df, x="clients", y="premium",
    text="city",
    title="Количество клиентов vs средняя премия",
    labels={"clients": "Клиентов", "premium": "Средняя премия, руб."}
)
st.plotly_chart(fig, use_container_width=True)

# Pie chart
fig2 = px.pie(df, names="city", values="clients", title="Доля клиентов по городам")
st.plotly_chart(fig2, use_container_width=True)
```

---

## Загрузка JSON-файла

```python
import streamlit as st
import pandas as pd
import json

st.title("Загрузка базы клиентов")

uploaded = st.file_uploader("Выберите JSON-файл", type=["json"])

if uploaded is not None:
    try:
        data = json.load(uploaded)
        df = pd.DataFrame(data)
        
        st.success(f"Загружено {len(df)} клиентов")
        st.dataframe(df)
        
        # Кнопка экспорта
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Скачать как CSV",
            data=csv,
            file_name="clients.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"Ошибка: {e}")
else:
    st.info("Загрузите JSON-файл для анализа")
```

---

## Полный дашборд страховщика

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

st.set_page_config(
    page_title="ПолисПлюс",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ ПолисПлюс — Дашборд управления")

# Подключаемся к БД (из главы 16)
@st.cache_data(ttl=60)   # кэш на 60 секунд
def load_data():
    conn = sqlite3.connect("insurance.db")
    conn.row_factory = sqlite3.Row
    
    clients = pd.read_sql(
        "SELECT c.name, c.age, c.city, p.car, p.premium "
        "FROM clients c JOIN policies p ON p.client_id = c.id",
        conn
    )
    conn.close()
    return clients

df = load_data()

# Метрики
c1, c2, c3, c4 = st.columns(4)
c1.metric("Всего клиентов",    len(df))
c2.metric("Средняя премия",    f"{df['premium'].mean():,.0f} ₽")
c3.metric("Максимальная",      f"{df['premium'].max():,.0f} ₽")
c4.metric("Итого сборов",      f"{df['premium'].sum():,.0f} ₽")

st.divider()

# Два столбца с графиками
col1, col2 = st.columns(2)

with col1:
    st.subheader("Премии по городам")
    city_stats = df.groupby("city")["premium"].mean().reset_index()
    fig = px.bar(city_stats, x="city", y="premium", color="city")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Распределение возраста")
    fig2 = px.histogram(df, x="age", nbins=10, color_discrete_sequence=["#636EFA"])
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Все клиенты")
st.dataframe(df, use_container_width=True)
```

---

## Полезные компоненты

```python
# Текстовый ввод
name = st.text_input("Имя клиента", placeholder="Иванов А.П.")

# Числовой ввод
age = st.number_input("Возраст", min_value=18, max_value=100, value=35)
amount = st.number_input("Сумма страхования", min_value=0.0, step=10_000.0)

# Выпадающий список
city = st.selectbox("Город", ["Москва", "СПб", "Казань", "Другой"])

# Кнопка
if st.button("Рассчитать премию"):
    premium = 12_000 * 1.5 if age < 25 else 12_000
    st.success(f"Премия: {premium:,.0f} руб.")

# Форма (отправка одной кнопкой)
with st.form("claim_form"):
    client = st.text_input("Клиент")
    amount = st.number_input("Сумма")
    submitted = st.form_submit_button("Подать заявление")
    
    if submitted:
        st.write(f"Заявление от {client} на {amount:,.0f} руб. принято")
```

---

## Упражнения

1. Запустите `streamlit run app.py` с примером метрик выше.
2. Добавьте фильтр по городу и слайдер по возрасту.
3. Нарисуйте bar chart: средняя премия по городам.
4. Загрузите JSON-файл из главы 8 и отобразите как таблицу.
5. Подключитесь к SQLite из главы 16 и сделайте живой дашборд.
