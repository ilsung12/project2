from django.urls import path, include
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoTV.as_view(), name='index'),
]
