from django.urls import path
from . import views

urlpatterns = [
    path('list', views.get_drives),
    path('create', views.create_drives),
    path('get/<int:pk>', views.get_drive),
    path('update/<int:pk>', views.update)
]