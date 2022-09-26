from django.urls import path
from . import views

urlpatterns = [
    path('manga/add/', views.mangaAdd),
    path('manga/get/', views.mangaGetAll)
]
