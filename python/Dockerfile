FROM python:3.10-slim

# Установка зависимостей
RUN pip install --upgrade pip

# Установка основных библиотек
RUN pip install \
    flask \
    tensorflow \
    torch \
    pandas \
    numpy \
    pymongo

# Настройка рабочей директории
WORKDIR /app

# Копирование исходного кода
COPY . .

# Запуск приложения
CMD ["flask", "run", "--host=0.0.0.0"]
