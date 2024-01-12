
from django.urls import path, include
from django.conf import settings
from  .views import password_generator

urlpatterns = [
    path('', password_generator, name='password_generator'),
]