from django.urls import path
from . import views

urlpatterns = [
    path('', views.Promocoes, name='home'),
    path('livros/', views.Index_livros, name='livros'),
    path('promocoes/', views.Promocoes, name='promocoes'),
    path('cadastro_usuarios/', views.Cadastro, name='cadastro_usuarios'),

    
]
