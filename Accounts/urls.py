from django.contrib import admin
from django.urls import path
from .views import SignUp_view, Login_view, Logout_view, goback

app_name = 'Accounts'

urlpatterns = [
    path('SignUp/', SignUp_view, name='SignUp'),
    path('Login/', Login_view, name='Login'),
    path('Logout/', Logout_view, name='Logout'),
    path('goback/', goback, name='goback')
]
