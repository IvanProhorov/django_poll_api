[![django_poll_api](https://github.com/IvanProhorov/django_poll_api/actions/workflows/main.yml/badge.svg)](https://github.com/IvanProhorov/foodgram-project/actions/workflows/main.yml)

 API для системы опросов пользователей.
 # Подготовка к работе:


   ```
 docker pull prohivan/django_poll_api
   ```
   ```
 docker run prohivan/django_poll_api
   ```
   ```
   api/v1/votes/<int:user_id>/ Информация о голосовании
   api/v1/choices/<int:choice_id>/ ответы на вопросы 
   api/v1/polls/<int:poll_id>/  Опросники
   ```
## Технологии
* [Python](https://www.python.org/) - высокоуровневый язык программирования общего назначения;
* [Django](https://www.djangoproject.com/) - фреймворк для веб-приложений;
* [Django REST framework](https://www.django-rest-framework.org/) - API фреймворк для Django;
* [Docker](https://www.docker.com/) - ПО для автоматизации развёртывания и управления приложениями в средах с поддержкой контейнеризации;
