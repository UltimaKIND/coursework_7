# Трекер привычек
приложение направленное на создание новых (полезных) привычек и искоренение старых (плохих)

## Содержание
- [Технологии](#технологии)
- [Использование](#начало-работы)
- [Разработка](#тестирование)
- [Тестирование](#deploy-и-ci/cd)

## Технологии
- [Django](https://www.djangoproject.com/)
- [django-res-framework](https://www.django-rest-framework.org/)
- [celery](https://docs.celeryq.dev/en/stable/)
- [requests](https://pypi.org/project/requests/)

## Использование

планировщик и worker celery
```sh
$ celery -A config worker -l INFO
```
```sh
$ celery -A config beat -l info -s django
```

## Разработка

### Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
$ poetry install
```

### Запуск Development сервера
Чтобы запустить сервер для разработки, выполните команду:
```sh
$ python3 manage.py runserver
```


## Тестирование

Наш проект покрыт тестами. Для их запуска выполните команду:
```sh
$
```
