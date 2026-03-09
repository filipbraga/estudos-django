
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Importa a login.view do django e chama o template login
    
    path('', auth_views.LoginView.as_view(template_name='registros/login.html'), name='login'),
    
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registros/', include('registros.urls')), 
]