from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),      # tempaltes에서 url 쓸 일이 없으므로 name은 필요없다. (app_name도 필요없음)
]
