from django.urls import path
from . import views

app_name = 'django_app'

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]