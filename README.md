# Афиша Артёма
Сайт с интерактивной картой интересных мест.

Демо-сайт доступен [тут](http://62.84.122.160/).


## Как установить

Для написания скрипта использовался __Python 3.11__.
Инструмент для управления зависимостями __Poetry__.

1. Склонировать репозиторий.
   
2. Создать виртуальное окружение.
    ```bash
    poetry shell
    ```
3. Установить зависимости:
    ```bash
    poetry install
    ```
4. Скопируйте `.env_example` в `.env`:
   ```bash
   cp .env_example .env
   ```
5. Занесите в `.env` необходимые параметры:
   - `SECRET_KEY` - секретный ключ проекта
   - `DEBUG` - дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
   - `ALLOWED_HOSTS` - см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

   - `LANGUAGE_CODE` - локализация проекта.
   - `TIME_ZONE` - часовой пояс проекта.
   - `USE_I18N` - включение системы перевода в проекте.
   - `USE_TZ` - включение использования часового пояса по умолчанию.
   - `STATIC_URL` - url-адрес используемый для обращения к статическим файлам.
   - `STATIC_ROOT` - путь, куда будет собираться вся статика (команда `collectstatic`)   
   - `MEDIA_ROOT` - путь, куда будут сохраняться загруженные пользователями файлы.
   - `MEDIA_URL` - url-адрес используемый для обращения к файлам загруженным в MEDIA_ROOT.

Значения по умолчанию указаны в файле `.env_example`.

6. Примените миграции:
    ```bash
    python manage.py migrate
    ```
7. Создайте администратора:
    ```bash
    python manage.py createsuperuser
    ```
8. Запустить сервер локально:
   ```bash
   python manage.py runserver
   ```
Сайт будет доступен по адресу [тут](http://127.0.0.1:8000/)

Добавить новое место можно вручную из админки [тут](http://127.0.0.1:8000/admin), либо используйте команду управления load_place с json-путем в качестве параметра:
```bash
python manage.py load_place https://your.json.url
```
Структура JSON:
```
{
    "title": "Title of the location",
    "imgs": [
        "https://link.to.image.1",
        "https://link.to.image.2"
    ],
    "description_short": "Summary for the location or event",
    "description_long": "Full description",
    "coordinates": {
        "lng": longitude_value,
        "lat": latitude_value
    }
}
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).