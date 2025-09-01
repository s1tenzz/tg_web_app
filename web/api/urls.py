from django.urls import path
from .views import get_all_users

urlpatterns = [
    path('users/', get_all_users, name='get_all_users'),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('web.api.urls')),
]

