# Глава 20: Виртуальные окружения и секреты

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/secrets_levels.jpg" width="95%"/></div>

> **Главное правило безопасности**: пароли, токены, ключи — никогда не попадают в git.
> Это правило важнее любого другого в разработке.

---

## Часть 1: Виртуальное окружение (venv)

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/venv_isolation.jpg" width="95%"/></div>

### Зачем нужно виртуальное окружение?

Представьте: у вас два проекта.
- Страховой сервис требует `FastAPI 0.110`
- Старый банковский проект работает только на `FastAPI 0.95`

Если установить обе версии в системный Python — они конфликтуют.
**Виртуальное окружение** изолирует зависимости каждого проекта.

```
/home/user/
├── project-insurance/
│   ├── venv/               ← своя копия Python + пакеты
│   │   └── lib/FastAPI-0.110/
│   └── main.py
│
└── project-bank/
    ├── venv/               ← другая изолированная копия
    │   └── lib/FastAPI-0.95/
    └── app.py
```

### Создание и активация

```bash
# Создать окружение (один раз на проект)
python3 -m venv venv

# Активировать — macOS/Linux
source venv/bin/activate

# Активировать — Windows
venv\Scripts\activate

# Признак активации: в терминале появится (venv)
(venv) $ 
```

### Управление пакетами

```bash
# Установить пакет (только в текущее окружение)
pip install fastapi sqlalchemy kafka-python

# Посмотреть установленное
pip list

# Сохранить список зависимостей
pip freeze > requirements.txt

# Развернуть у коллеги или на сервере
pip install -r requirements.txt

# Деактивировать окружение
deactivate
```

### requirements.txt — список зависимостей проекта

```text
fastapi==0.110.0
uvicorn==0.29.0
sqlalchemy==2.0.29
psycopg2-binary==2.9.9
kafka-python==2.0.2
prometheus-client==0.20.0
streamlit==1.33.0
python-dotenv==1.0.1
hvac==2.1.0
```

```bash
# Установить всё из файла
pip install -r requirements.txt
```

### Что добавить в .gitignore

```gitignore
# Виртуальное окружение — никогда не коммитим
venv/
.venv/
env/

# Секреты
.env
.env.local
.env.production

# Кэш Python
__pycache__/
*.pyc
*.pyo

# IDE
.vscode/
.idea/
```

---

## Часть 2: Секреты в .env (разработка)

### Что такое .env файл?

Файл с переменными окружения — пары `КЛЮЧ=ЗНАЧЕНИЕ`.
Хранится **только на вашем компьютере**, в git не попадает.

```bash
# .env — файл в корне проекта
DB_HOST=localhost
DB_PORT=5432
DB_NAME=insurance
DB_USER=postgres
DB_PASSWORD=my_local_password_123

KAFKA_BROKERS=localhost:9092
KAFKA_TOPIC=insurance.claims

API_SECRET_KEY=dev-secret-key-not-for-production
LLM_API_URL=http://localhost:11434

PROMETHEUS_PORT=8000
LOG_LEVEL=DEBUG
```

### Чтение .env в Python

```bash
pip install python-dotenv
```

```python
# config.py — единая точка конфигурации
from dotenv import load_dotenv
import os

load_dotenv()   # читает .env файл

class Settings:
    # База данных
    DB_HOST:     str = os.getenv("DB_HOST", "localhost")
    DB_PORT:     int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME:     str = os.getenv("DB_NAME", "insurance")
    DB_USER:     str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    
    # Kafka
    KAFKA_BROKERS: str = os.getenv("KAFKA_BROKERS", "localhost:9092")
    KAFKA_TOPIC:   str = os.getenv("KAFKA_TOPIC", "insurance.claims")
    
    # API
    API_SECRET_KEY: str = os.getenv("API_SECRET_KEY", "")
    LOG_LEVEL:      str = os.getenv("LOG_LEVEL", "INFO")
    
    @property
    def db_url(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()

# Использование везде в проекте
print(settings.db_url)
print(settings.KAFKA_BROKERS)
```

```python
# main.py — используем settings
from config import settings
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=settings.LOG_LEVEL)

engine = create_engine(settings.db_url)
```

### .env.example — что коммитим вместо .env

```bash
# .env.example — шаблон без реальных значений
# Скопируйте в .env и заполните своими данными:
# cp .env.example .env

DB_HOST=localhost
DB_PORT=5432
DB_NAME=insurance
DB_USER=postgres
DB_PASSWORD=          # ← заполнить

KAFKA_BROKERS=localhost:9092
KAFKA_TOPIC=insurance.claims

API_SECRET_KEY=       # ← заполнить
LLM_API_URL=http://localhost:11434

LOG_LEVEL=DEBUG
```

### Распространённая ошибка

```bash
# ОШИБКА: случайно закоммитили .env с паролями
git add .
git commit -m "initial commit"
# → .env с паролями теперь в истории git навсегда!

# Даже если удалить файл — он останется в git log
# Придётся менять ВСЕ пароли и токены

# КАК ПРОВЕРИТЬ перед коммитом
git status          # видно какие файлы попадут
git diff --staged   # что именно меняется

# Если случилось — немедленно меняйте все секреты!
```

---

## Часть 3: Azure DevOps — секреты в CI/CD

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/azure_devops_secrets.jpg" width="95%"/></div>

### Зачем нужны Variable Groups?

В пайплайне `.yml` файл хранится в репозитории — значит его видят все.
Пароли туда класть нельзя.
**Variable Groups** хранят секреты отдельно, передают в пайплайн как переменные.

### Настройка Variable Group (UI)

```
Azure DevOps → Pipelines → Library → Variable Groups
  → New Variable Group
    Name: insurance-prod-secrets
    Variables:
      DB_PASSWORD      = ******  (нажать замочек!)
      API_SECRET_KEY   = ******
      KAFKA_PASSWORD   = ******
      VAULT_TOKEN      = ******
```

### azure-pipelines.yml — используем переменные

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include: [main]

pool:
  vmImage: ubuntu-latest

variables:
  - group: insurance-prod-secrets       # подключаем группу секретов
  - name: PYTHON_VERSION
    value: "3.12"

stages:
  - stage: Test
    jobs:
      - job: RunTests
        steps:
          - task: UsePythonVersion@0
            inputs:
              versionSpec: $(PYTHON_VERSION)
          
          - script: |
              python -m venv venv
              source venv/bin/activate
              pip install -r requirements.txt
            displayName: "Установка зависимостей"
          
          - script: |
              source venv/bin/activate
              pytest tests/ -v --tb=short
            displayName: "Запуск тестов"
            env:
              DB_PASSWORD: $(DB_PASSWORD)        # из Variable Group
              API_SECRET_KEY: $(API_SECRET_KEY)  # из Variable Group
  
  - stage: Deploy
    dependsOn: Test
    condition: succeeded()
    jobs:
      - deployment: DeployProd
        environment: production
        strategy:
          runOnce:
            deploy:
              steps:
                - script: |
                    echo "Деплой на прод..."
                    # DB_PASSWORD доступен как переменная окружения
                  env:
                    DB_PASSWORD: $(DB_PASSWORD)
```

### Разные секреты для dev/prod

```
Variable Group: insurance-dev-secrets
  DB_HOST = dev-db.company.ru
  DB_PASSWORD = dev_password

Variable Group: insurance-prod-secrets
  DB_HOST = prod-db.company.ru
  DB_PASSWORD = ******* (сложный пароль)
```

```yaml
variables:
  - ${{ if eq(variables['Build.SourceBranch'], 'refs/heads/main') }}:
    - group: insurance-prod-secrets
  - ${{ else }}:
    - group: insurance-dev-secrets
```

---

## Часть 4: HashiCorp Vault — секреты в продакшне

<div align="center"><img src="https://raw.githubusercontent.com/OlegKarenkikh/python-for-beginners/main/images/vault_flow.jpg" width="95%"/></div>

### Зачем Vault если есть .env и Azure DevOps?

| Сценарий | .env | Azure DevOps | Vault |
|---|---|---|---|
| Локальная разработка | ✅ | — | — |
| CI/CD пайплайн | — | ✅ | ✅ |
| Автоматическая ротация паролей | ❌ | ❌ | ✅ |
| Динамические учётные данные | ❌ | ❌ | ✅ |
| Аудит: кто что запросил | ❌ | частично | ✅ |
| Отзыв доступа мгновенно | ❌ | ❌ | ✅ |

**Динамические секреты** — главная фишка Vault:
вместо одного пароля к БД, который знают все приложения,
Vault создаёт уникальный временный пароль для каждого запроса.
Через час он автоматически перестаёт работать.

### Установка клиента

```bash
pip install hvac
```

### Запись и чтение секретов

```python
import hvac
import os

# Подключение к Vault
client = hvac.Client(
    url=os.getenv("VAULT_ADDR", "http://localhost:8200"),
    token=os.getenv("VAULT_TOKEN")           # или AppRole/K8s auth
)

# Проверить подключение
if not client.is_authenticated():
    raise RuntimeError("Vault: не аутентифицирован!")

# --- Запись секрета (один раз, администратором) ---
client.secrets.kv.v2.create_or_update_secret(
    path="insurance/database",
    secret={
        "host":     "prod-db.company.ru",
        "port":     "5432",
        "name":     "insurance_prod",
        "user":     "insurance_app",
        "password": "ultra-secret-prod-password"
    }
)

# --- Чтение секрета (приложением) ---
response = client.secrets.kv.v2.read_secret_version(
    path="insurance/database"
)
db_secrets = response["data"]["data"]

print(f"Host:     {db_secrets['host']}")
print(f"User:     {db_secrets['user']}")
print(f"Password: {'*' * len(db_secrets['password'])}")

# Используем для подключения к БД
db_url = (
    f"postgresql://{db_secrets['user']}:{db_secrets['password']}"
    f"@{db_secrets['host']}:{db_secrets['port']}/{db_secrets['name']}"
)
```

### AppRole аутентификация (для production)

```python
import hvac, os

# AppRole — для приложений, не для людей
client = hvac.Client(url=os.getenv("VAULT_ADDR"))

# Аутентификация через role_id + secret_id
resp = client.auth.approle.login(
    role_id=os.getenv("VAULT_ROLE_ID"),
    secret_id=os.getenv("VAULT_SECRET_ID")
)

# Токен действителен TTL секунд (например, 1 час)
print(f"Token TTL: {resp['auth']['lease_duration']}s")

# Теперь можем читать секреты
db = client.secrets.kv.v2.read_secret_version(
    path="insurance/database"
)["data"]["data"]
```

### Интеграция в config.py

```python
# config.py — production-ready версия
import os
from dotenv import load_dotenv

# Загружаем .env только если он есть (для локальной разработки)
load_dotenv(override=False)

def _get_from_vault(path: str, key: str) -> str | None:
    """Читает секрет из Vault если настроен."""
    vault_addr = os.getenv("VAULT_ADDR")
    vault_token = os.getenv("VAULT_TOKEN")
    
    if not (vault_addr and vault_token):
        return None  # Vault не настроен — используем .env
    
    try:
        import hvac
        client = hvac.Client(url=vault_addr, token=vault_token)
        secret = client.secrets.kv.v2.read_secret_version(path=path)
        return secret["data"]["data"].get(key)
    except Exception as e:
        print(f"Vault недоступен: {e}, используем .env")
        return None


class Settings:
    # При наличии Vault — берём оттуда, иначе из .env
    DB_PASSWORD: str = (
        _get_from_vault("insurance/database", "password")
        or os.getenv("DB_PASSWORD", "")
    )
    DB_HOST: str = (
        _get_from_vault("insurance/database", "host")
        or os.getenv("DB_HOST", "localhost")
    )
    DB_USER: str = (
        _get_from_vault("insurance/database", "user")
        or os.getenv("DB_USER", "postgres")
    )
    DB_NAME: str = os.getenv("DB_NAME", "insurance")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    
    @property
    def db_url(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

settings = Settings()
```

---

## Итоговая схема: что где хранить

```
Среда          Где хранить секреты           Как читать
-----------    --------------------------    --------------------
Локальная      .env (только на диске)        python-dotenv
разработка     НЕ коммитить в git!           os.getenv()

CI/CD          Azure DevOps Variable Groups  Переменные окружения
тесты/билд     GitHub Secrets                в шаге пайплайна

Продакшн       HashiCorp Vault               hvac + AppRole
(прод сервер)  (KV v2 или Dynamic Secrets)   или K8s Vault Agent

Резервно       Azure Key Vault               azure-identity
(Azure)        AWS Secrets Manager           boto3
```

---

## Чеклист перед деплоем

```bash
# 1. .env не попал в git?
cat .gitignore | grep ".env"    # должно быть там

# 2. Нет паролей в коде?
grep -r "password\s*=" src/ --include="*.py" | grep -v "os.getenv\|settings\."

# 3. Нет токенов в коде?
grep -rE "(token|secret|key)\s*=\s*['\"][a-zA-Z0-9]{10,}" src/

# 4. requirements.txt актуален?
pip freeze > requirements.txt
git diff requirements.txt

# 5. .env.example существует и обновлён?
diff .env .env.example   # должны совпадать по ключам
```

---

## Упражнения

1. Создайте виртуальное окружение и установите `fastapi`, `python-dotenv`, `sqlalchemy`.
2. Создайте `.env` с настройками БД и убедитесь что он в `.gitignore`.
3. Напишите `config.py` — класс `Settings` читает все параметры из `.env`.
4. Создайте `.env.example` с пустыми значениями для коллег.
5. Прочитайте об Azure DevOps Variable Groups и создайте группу для учебного проекта.
6. Установите Vault локально через Docker и прочитайте секрет через `hvac`.

```bash
# Vault через Docker для экспериментов
docker run -d --name vault \
  -p 8200:8200 \
  -e VAULT_DEV_ROOT_TOKEN_ID=dev-token \
  hashicorp/vault

export VAULT_ADDR=http://localhost:8200
export VAULT_TOKEN=dev-token

# Проверка
curl $VAULT_ADDR/v1/sys/health | python3 -m json.tool
```
