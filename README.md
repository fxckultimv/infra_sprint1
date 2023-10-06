# Kittygram
### Описание
Cоциальная сеть для обмена фотографиями любимых питомцев. Проект состоит из бэкенд-приложения на Django и фронтенд-приложения на React.
### Технологии
Django 3.2.3 | djangorestframework 3.12.4 | djoser 2.1.0 | webcolors 1.11.1 | Pillow 9.0.0 | pytest 6.2.4 | pytest-django 4.4.0 | pytest-pythonpath 0.7.3 | python-dotenv 0.19.0

## Деплой проекта на удалённый сервер:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/esaviv/infra_sprint1.git
```
```
cd infra_sprint1/
```
Создать файл .env и заполнить его по образцу .env.template.

Для отображения фотографий на сайте создать директорию media в системной директории веб-сервера Nginx:
```
sudo mkdir /var/www/kittygram/media/
```
Назначить текущего пользователя владельцем директории media, чтобы Django-приложение могло сохранять картинки:
```
sudo chown -R <имя_пользователя> /var/www/kittygram/media/
```
Создать и активировать виртуальное окружение:
```
python3 -m venv venv
```
```
source env/bin/activate
```
```
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Перейдите в директорию бэкенд-приложение проекта:
```
cd backend/
```
Выполнить миграции:
```
python manage.py migrate
```
Создать суперпользователя:
```
python manage.py createsuperuser
```
Собрать статику бэкенд-приложения:
```
python manage.py collectstatic 
```
Скопировать созданную директорию static_backend/ в системную директорию веб-сервера Nginx:
```
sudo cp -r static_backend/ /var/www/kittygram/
```
Перейдите в директорию фронтенд-приложение проекта, установить зависимости:
```
cd ../frontend/
```
```
npm i
```
Собрать статику фронтенд-приложения:
```
npm run build 
```
Скопировать содержимое созданной папки build/ в системную директорию веб-сервера Nginx:
```
sudo cp -r build/. /var/www/kittygram/
```
Cоздать файл gunicorn_kittygram.service:
```
sudo nano /etc/systemd/system/gunicorn_kittygram.service
```
```
[Unit]
Description=kittygram_backend daemon 

After=network.target 

[Service]
User=<имя-пользователя-в-системе>

WorkingDirectory=/home/<имя-пользователя-в-системе>/infra_sprint1/backend/

ExecStart=/home/<имя-пользователя-в-системе>/infra_sprint1/venv/bin/gunicorn --bind 0.0.0.0:8080 kittygram_backend.wsgi

[Install]
WantedBy=multi-user.target
```
Запустить процесс gunicorn_kittygram.service:
```
sudo systemctl start gunicorn_kittygram
```
Добавить процесс в список автозапуска операционной системы на удалённом сервере:
```
sudo systemctl enable gunicorn_kittygram
```
Проверить работоспособность запущенного демона:
```
sudo systemctl status gunicorn_kittygram
```
Описать настройки для работы со статикой фронтенд-приложения:
```
sudo nano /etc/nginx/sites-enabled/default 
```
```
server {
    server_name <ваш-ip> <ваш-домен>;

    location /api/ {
        proxy_pass http://127.0.0.1:8080;
    }
    

    location /admin/ {
        proxy_pass http://127.0.0.1:8080;
    }

    location /media/ {
        alias /var/www/kittygram/media/;
    }

    location / {
        root   /var/www/kittygram;
        index  index.html index.htm;
        try_files $uri /index.html;
    }
} 
```
Проверить файл конфигурации на ошибки:
```
sudo nginx -t 
```
Перезагрузить конфигурацию Nginx:
```
sudo systemctl reload nginx 
```
Получить и настроить SSL-сертификат Вашим любимым способом.
