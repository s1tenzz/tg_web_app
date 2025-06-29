from django.urls import path

from api.views import UserCreate, UserGet

urlpatterns = [
    path('user-create', UserCreate.as_view()),
    path('user-get', UserGet.as_view()),
]