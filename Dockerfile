FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Устанавливаем системные зависимости для psycopg
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости проекта
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Копируем весь проект
COPY . .

EXPOSE 8000

# Команда по умолчанию будет переопределена в docker-compose.yaml
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]