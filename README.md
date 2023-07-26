# Компактный веб-сервер для работы с авторами и книгами
Это Django-приложение, реализующее веб-сервис для сохранения и получения  информации о книгах и авторах.
## Зависимости
Для запуска приложения нам потребуется Python>=3.9 и следующие python библиотеки:
- Django
- Django REST Framework
Вы можете установить все необходимые библиотеки с помощью pip, выполнив команду:  
<code class="lang-markdown">pip install -r requirements.txt</code>
## Запуск приложения
1. Склонируйте репозиторий на свой компьютер.
2. Перейдите в директорию с проектом.
3. Выполните миграции для создания базы данных:  
<code class="lang-markdown">python manage.py migrate</code>
4. Создайте супер-пользователя к админ-панеле:  
<code class="lang-markdown">python manage.py createsuperuser</code>
5. Запустите сервер разработки  
<code class="lang-markdown">python manage.py runserver</code>
6. Откройте браузер и перейдите на страницу <code class="lang-markdown">http://localhost:8000</code>   для доступа к API.
## API
Сервис предоставляет следующие HTTP-методы и эндпоинты:
- GET /api/books/ - получение списка всех книг
- POST /api/books/ - сохранение информации о книге
- GET /api/books/int:pk/ - получение информации о конкретной книге по идентификатору
- POST /api/authors/ - сохранение информации об авторе
- GET /api/authors/ - получение списка всех авторов
- GET /api/authors/int:pk/ - получение информации о конкретном авторе по идентификатору
