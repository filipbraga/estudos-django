
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Importe as views de auth

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registros/login.html'), name='login'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('registros.urls')), 
]