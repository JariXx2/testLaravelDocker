FROM node:18 as development

# Установка глобальных зависимостей
RUN npm install -g @vue/cli

# Настройка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY package*.json ./

# Установка основных зависимостей
RUN npm install \
    vue-router@4 \
    pinia \
    axios \
    vuetify@next \
    sass \
    sass-loader@13 \
    pug \
    pug-plain-loader

# Копирование исходного кода
COPY . .

# Режим разработки
CMD ["npm", "run", "serve"]

# Production сборка
FROM development as builder
RUN npm run build

FROM nginx:alpine as production
COPY --from=builder /app/dist /usr/share/nginx/html
COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
