from .views import *
from django.urls import path, include
urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('news/', NewsView.as_view(), name='news'),
    path('detail/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]