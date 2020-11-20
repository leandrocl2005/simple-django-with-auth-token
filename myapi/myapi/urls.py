from core.views import HelloView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token/', obtain_auth_token, name='api_token_auth'),
    path('hello/', HelloView.as_view(), name='hello'),
]
