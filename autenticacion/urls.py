from django.urls import path
from . import views

urlpatterns = [
    path('accounts/ml/login/', views.login_page, name='cuentas'),
    path('accounts/ml/logout/', views.logout_page, name='logout'),
    path('accounts/ml/register/', views.register_page, name='register'),
    path('accounts/ml/profile/', views.profile_page, name='profile'),
    path('accounts/ml/profile/edit/', views.edit_profile, name='edit_profile'),
    path('accounts/ml/password_change/', views.change_password, name='change_password'),
]