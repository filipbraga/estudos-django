from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
]