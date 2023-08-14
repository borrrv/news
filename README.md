# News
## Описание
С помощью данного сервиса пользователи могут создавать, редактировать и удалять свои новости, а также комментировать их и ставить лайки
##### Проект доступен по адресу http://158.160.60.152/
### В задании было указано, что доступно только 2 роли, поэтому все запросы доступны только авторизованным пользователям
### Запуск проекта локально
- Клонировать проект
```
git clone https://github.com/borrrv/news.git
```
- Переименовать файлы ```.env_example``` в ```.env```
- В консоле перейти в папку с файлом ```docker-compose.yml```
- Выполнить команду
```
sudo docker-compose up -d --build
```
- Перейти в контейнер ```web``` 
```
sudo docker exec -it <CONTAINER ID> bash
```
- Применить миграции, собрать статику и создать суперпользователя
```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```
- Проект готов к локальной работе
##### Создание пользователей доступно только через админку
### В задании было указано, что доступно только 2 роли, поэтому все запросы доступны только авторизованным пользователям
### Эндпоинты (если локально, то относительно http://localhost/, иначе относительно http://158.160.60.152/)
#### Данные для входа в админку
```
login: admin
password: admin
```
- (POST) Получение токена
```
api/auth/
```
##### request
```
{
    "username": "admin",
    "password": "admin"
}
```
##### response
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MjA4MTEwNiwiaWF0IjoxNjkxOTk0NzA2LCJqdGkiOiJkYzQwZDI4ZWVjOWI0Y2QyYmQzMDhhZWM1ZTk0M2I0YyIsInVzZXJfaWQiOjF9.zJrO4ZAq8jzSrxdUFKj1Cs1MpC5-Da34g6mPQK0NjZU",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkyMDgxMTA2LCJpYXQiOjE2OTE5OTQ3MDYsImp0aSI6ImI1M2I0ZDVlYjFiMjRkYWM5NjI2NWNhNjMzMDk3NzJhIiwidXNlcl9pZCI6MX0.4NI_XZOudDjjv9Pyh3Kxivmoe-PlHj2iLYbJQQ1sGHw"
}
```
- (POST, GET) Создание и получение новостей
```
api/news/
```
##### request (POST)
```
{
    "title": "News 2 test",
    "text": "text for news"
}
```
##### response (POST)
```
{
    "id": 6,
    "title": "News 2 test",
    "text": "text for news",
    "author": "admin",
    "pub_date": "2023-08-14T10:04:27.922856+03:00",
    "likes_count": 0,
    "comments_count": 0,
    "comments": []
}
```
##### response (GET)
````
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "title": "News 2 test",
            "text": "text for news 2",
            "author": "admin",
            "pub_date": "2023-08-13T12:04:15.874936+03:00",
            "likes_count": 1,
            "comments_count": 15,
            "comments": [
                {
                    "id": 26,
                    "news": 2,
                    "text": "12",
                    "pub_date": "2023-08-13T16:54:14.667847+03:00"
                },
              ]
          }
      ]
}
````
- (GET, PUT, DELETE) Получение, изменение, удаление новости по id
```
api/news/2/
```
##### request (PUT)
```
{
    "title": "News 2 test",
    "text": "text for news"
}
```
##### response
```
{
    "id": 2,
    "title": "News 2 test",
    "text": "text for news",
    "author": "admin",
    "pub_date": "2023-08-14T09:53:50.289999+03:00",
    "likes_count": 1,
    "comments_count": 15,
    "comments": [
        {
            "id": 26,
            "news": 2,
            "text": "12",
            "pub_date": "2023-08-13T16:54:14.667847+03:00"
        },
    ]
}
```
- (POST, GET) Создание комментария к новости и получения всех комментариев к новости
```
/api/news/2/comment/
```
##### request (POST)
```
{
    "text": "test comment"
}
```
##### response (POST)
```
{
    "id": 27,
    "news": 2,
    "text": "test comment",
    "pub_date": "2023-08-14T09:57:59.460439+03:00"
}
```
##### response (GET)
```
{
    "count": 15,
    "next": "http://127.0.0.1:8000/api/news/2/comment/?page=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "news": 2,
            "text": "test comment patch",
            "pub_date": "2023-08-13T11:52:50.181651+03:00"
        },
        {
            "id": 4,
            "news": 2,
            "text": "1 comment patch",
            "pub_date": "2023-08-12T22:26:33.009174+03:00"
        },
        {
            "id": 6,
            "news": 2,
            "text": "2 comment",
            "pub_date": "2023-08-12T22:34:51.457024+03:00"
        },
        {
            "id": 10,
            "news": 2,
            "text": "test comment 2",
            "pub_date": "2023-08-13T12:05:01.964723+03:00"
        },
        {
            "id": 14,
            "news": 2,
            "text": "6",
            "pub_date": "2023-08-13T13:19:03.576771+03:00"
        },
        {
            "id": 15,
            "news": 2,
            "text": "7",
            "pub_date": "2023-08-13T13:19:06.374306+03:00"
        },
        {
            "id": 16,
            "news": 2,
            "text": "8",
            "pub_date": "2023-08-13T13:19:11.762153+03:00"
        },
        {
            "id": 17,
            "news": 2,
            "text": "9",
            "pub_date": "2023-08-13T13:19:14.117434+03:00"
        },
        {
            "id": 18,
            "news": 2,
            "text": "10",
            "pub_date": "2023-08-13T13:19:16.652626+03:00"
        },
        {
            "id": 19,
            "news": 2,
            "text": "11",
            "pub_date": "2023-08-13T13:19:20.323212+03:00"
        }
    ]
}
```
- (DELETE) Удалить комментарий по id комментария
```
/api/comment/5/
```
- (POST, DELETE) Поставить или убрать лайк с новости
```
/api/news/2/like/
```
##### response (POST)
```
Вы поставили лайк на новость
```
##### response (DELETE)
```
Вы убрали лайк с новости
```
