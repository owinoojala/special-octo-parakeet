from django.urls import path
from . import views

urlpatterns = [
    path('accounts/register', views.register, name = 'register'),
    path('accounts/login', views.login, name = 'login'),
    path('accounts/logout', views.logout, name = 'logout'),
    path('accounts/verify/<uidb64>/<token>', views.verify, name = 'verify')
    
]