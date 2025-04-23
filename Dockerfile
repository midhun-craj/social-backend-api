FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install --upgrade pip && \
    pip install --no-cache-dir --prefer-binary --prefix=/install -r requirements.txt

COPY . .

FROM python:3.10-slim 

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN useradd -m appUser

WORKDIR /app

COPY --from=builder --chown=appUser:appUser /install /usr/local
COPY --from=builder --chown=appUser:appUser /app /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN chown -R appUser:appUser /app /usr/local

USER appUser

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]