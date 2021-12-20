from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page),
    path('add_news', views.add_news)
]