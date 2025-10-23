from django.urls import path, include

urlpatterns = [
    path('cuentas/', include('allauth.urls')),
]
