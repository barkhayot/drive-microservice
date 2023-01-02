from django.urls import path
from . import views
from . import driver

urlpatterns = [
    path('register', views.register),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('profile/<int:pk>', views.profile),
    path('update/<int:pk>', views.update_profile),

    path('get', driver.get_list),
    path('create', driver.create_drive),
    path('get/<int:pk>', driver.get_drive)
]