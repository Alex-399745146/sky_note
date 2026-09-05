# Sky Note

Веб-приложение для ведения личного дневника.

## Возможности

- Регистрация, вход и выход пользователей
- Создание, просмотр, редактирование и удаление личных записей
- Защита записей: пользователь работает только со своими заметками
- Поиск по заголовку и содержимому
- Административная панель Django
- Адаптивный интерфейс на Django Templates и Bootstrap 5
- Запуск через Docker Compose
- PostgreSQL в качестве базы данных

## Технологии

- Python 3.13
- Django 5.2
- PostgreSQL
- Django ORM
- Django Templates
- Bootstrap 5 (CDN)
- Docker
- Docker Compose
- Git
- Poetry
- flake8, mypy, black, isort

## Структура проекта

```text
sky_note/
├── app_notes/          # Приложение дневниковых записей
├── app_users/          # Приложение пользователей
├── config/             # Настройки Django
├── static/             # Статические файлы (CSS)
├── templates/          # Общие шаблоны (base.html, includes)
├── .docker.env         # Переменные окружения для Docker
├── .env                # Переменные окружения для локального запуска
├── .env.example        # Шаблон переменных окружения
├── .flake8             # Конфигурация flake8
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── mypy.ini
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Установка и запуск

### Локальный запуск

1. Клонировать репозиторий:

   ```bash
   git clone <url-репозитория>
   cd sky_note
   ```

2. Установить Poetry (если не установлен):

   ```bash
   curl -sSL https://install.python-poetry.org | python -
   ```

3. Установить зависимости:

   ```bash
   poetry install
   ```

4. Создать файл `.env` на основе `.env.example`:

   ```bash
   cp .env.example .env
   ```

5. Настроить переменные в `.env`:

   ```env
   DEBUG=True
   SECRET_KEY=django-insecure-change-me-please
   POSTGRES_DB=sky_note_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=*********
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   ```

6. Применить миграции:

   ```bash
   poetry run python manage.py migrate
   ```

7. Создать суперпользователя:

   ```bash
   poetry run python manage.py createsuperuser
   ```

8. Запустить сервер:

   ```bash
   poetry run python manage.py runserver
   ```

9. Открыть в браузере:

   ```text
   http://127.0.0.1:8000/
   ```

### Запуск через Docker Compose

1. Создать файл `.docker.env` на основе `.env.example`:

   ```bash
   cp .env.example .docker.env
   ```

2. Настроить переменные в `.docker.env`:

   ```env
   DEBUG=True
   SECRET_KEY=django-insecure-change-me-please
   POSTGRES_DB=sky_note_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=*********
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

3. Запустить проект:

   ```bash
   docker compose up --build
   ```

4. Открыть в браузере:

   ```text
   http://127.0.0.1:8000/
   ```

5. Остановить проект:

   ```bash
   docker compose down
   ```

## Переменные окружения

| Переменная | Описание |
|---|---|
| `DEBUG` | Режим отладки Django (True/False) |
| `SECRET_KEY` | Секретный ключ Django |
| `POSTGRES_DB` | Имя базы данных PostgreSQL |
| `POSTGRES_USER` | Пользователь PostgreSQL |
| `POSTGRES_PASSWORD` | Пароль PostgreSQL |
| `POSTGRES_HOST` | Хост PostgreSQL (`localhost` для локального запуска, `db` для Docker) |
| `POSTGRES_PORT` | Порт PostgreSQL |

## Линтеры и форматеры

Проект использует:

- `flake8` — проверка стиля кода (PEP 8)
- `mypy` — статическая проверка типов
- `black` — автоматическое форматирование кода
- `isort` — сортировка импортов

Запуск проверок:

```bash
poetry run flake8 .
poetry run mypy app_notes app_users config
poetry run black .
poetry run isort .
```

## Автор

Alex Bachevskiy

## Лицензия

Учебный проект.