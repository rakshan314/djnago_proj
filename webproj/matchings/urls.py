from django.urls import path
from . import views
# import class LoginView for login authentication
# https://docs.djangoproject.com/en/2.1/topics/auth/default/#django.contrib.auth.views.LoginView
#from django.contrib.auth.views import LoginView

urlpatterns = [
    # /matchings/
    path('', views.home, name='home'),
    # /matchings/login
    path('login/', views.login, name='login'),
    # /matchings/login
    path('signup/', views.signup, name='signup'),
    # /matchings/login
    path('register/', views.register, name='register'),
]
