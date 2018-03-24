# Telegram Login Widget Django Example

Простое приложение-каркас для демонстрации функции авторизации через Telegram Login Widget.

Для настройки необходимо:
* Создать .env файл рядом с settings.py (можно переименовать .env-template в .env)
* Внутри .env файла присвоить переменной `SOCIAL_AUTH_TELEGRAM_BOT_TOKEN` токен бота
* В `templates/login.html` добавить свой скрипт виджета, полученный после настройки

Статья: [Авторизация через Telegram в Django и Python](https://khashtamov.com/ru/telegram-auth-django/)
