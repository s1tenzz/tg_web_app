from django.urls import path

from api.views import UserCreate

urlpatterns = [
    path('test', UserCreate.as_view()),
]