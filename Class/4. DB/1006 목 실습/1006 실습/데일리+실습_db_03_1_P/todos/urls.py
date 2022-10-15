from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.completed, name='completed'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]