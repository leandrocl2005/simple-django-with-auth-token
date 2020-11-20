- > python3 -m venv myvenv
- > . myvenv/Scripts/activate
- > pip install django
- > pip install djangorestframework
- > django-admin startproject myapi
- > cd myapi
- > django-admin startapp core
- Em **settings.py**:
```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'core',
]
```
- > python manage.py migrate
- Em **core/views.py**:
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
```
- Em **urls.py**:
```python
from core.views import HelloView
from django.urls import path

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
]
```
- Teste fazendo um `GET` para *http:localhost:8000/hello/*
- Para proteger a view com autenticação, em **core/views.py**:
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated # new

class HelloView(APIView):
    permission_classes = (IsAuthenticated,) # new
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
```
- Em **settings.py**:
```python
INSTALLED_APPS = [
    ...,
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```
- > python manage.py migrate
- > python manage.py createsuperuser --username lele --email lele@lele.com
- No comando acima, pede password. Digitamos simplesmente "123456".
- > python manage.py drf_create_token lele
- Teste fazendo um `GET` para *http://localhost:8000/hello/* passando no header `Authorization: Token <SEU_TOKEN>`.
- Para criar rota para adquirir token, mude **urls.py** para:
```python
from core.views import HelloView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # new

urlpatterns = [
    path('token/', obtain_auth_token, name='api_token_auth'), # new
    path('hello/', HelloView.as_view(), name='hello'),
]
```
- Teste fazendo um `POST` para *http://localhost:8000/token/* passando no body
```json
{
    "username": "lele",
    "password": "123456"
}
```
- > pip install django-cors-headers
- Em **settings.py**:
```python
INSTALLED_APPS = [
    ...,
    'corsheaders',
]

MIDDLEWARE_CLASSES = [
    ...
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
```

# Deploy Heroku
