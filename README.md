# test-case-greenatom
Тестовое задание АО "Гринатом"


## Описание
Приложение (веб-страница) для оценки тональности отзывов о фильмах. Для обучения модели машинного обучения использовались отзывы с сайта IMDB. 

## Зависимости (requirements.txt)
- django
- virtualenv
- tensorflow

## Описание содержимого
**/venv/** - содержит виртуальное окружение для Python. Создаеется и настраивается с помощью последовательности команд:
```
$ python -m venv venv
$ venv\Scripts\activate
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```
**/test_case_review/** - каталог с Django-проектом. Создаем его с помощью команды:
```
$ django-admin.exe startproject test_case_review .
```

**/review/** - каталог приложениея **Review**. Создаем его с помощью команды:
```
$ python manage.py startapp review
```
**/review/static/** - стили CSS

**/review/templates/** - шаблон страницы

## Запуск приложения
Заходим в витруальное окружение и запускаем командами:
```
$ test_case_review\venv\Scripts\activate
$ python manage.py runserver
```

Приложение доступно по адресу: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
