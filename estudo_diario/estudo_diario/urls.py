
from django.contrib import admin
from django.urls import path, include
from registros import views # Importa as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registros/', include('registros.urls')), # Inclui as rotas do app
    path('', views.home, name='home'), # Define a home na raiz do site 
]