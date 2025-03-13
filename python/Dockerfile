FROM python:3.10-slim

# Установка зависимостей
RUN pip install --upgrade pip

# Установка основных библиотек
RUN pip install --default-timeout=900 \
    flask \
    tensorflow \
    torch \
    pandas \
    numpy \
    pymongo

# Установка переменной окружения FLASK_APP
ENV FLASK_APP=main.py


# Настройка рабочей директории
WORKDIR /app

# Копирование исходного кода
COPY . .

# Запуск приложения
CMD ["python", "main.py"]


