from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('shodka/<int:shodki_id>/', views.shodka_detail, name='shodka_detail'),
    path('create_shodka/', views.create_shodka, name="create_shodka"),
]