from django.urls import path
from app_mecanica import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('', views.home, name='home'),
]
