from django.urls import path
from accounts import viewsAdmin  # Pastikan nama aplikasi dan file sesuai

urlpatterns = [
    # Pola URL lainnya...
    path('dashboard/admin/', viewsAdmin.admin, name='admin_dashboard'),
]
