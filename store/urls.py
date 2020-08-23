from django.contrib import admin
from django.urls import path
from .views.home import index
from .views.signup import signup
from .views.login import Login

urlpatterns = [
    path('', index.as_view(), name='homepage'),
    path('signup',signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login')
]
