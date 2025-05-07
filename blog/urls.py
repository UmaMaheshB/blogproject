from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.home),
    path('news/', views.news),
]
