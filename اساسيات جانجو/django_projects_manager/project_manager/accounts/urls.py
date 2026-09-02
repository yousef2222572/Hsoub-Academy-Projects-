
from django.contrib.auth.views import LoginView
from django.urls import path,include

from accounts.views import register_view , EditProfile
from .forms import UserLoginForm, UserProfileView


urlpatterns=[
    path('accounts/profile/',EditProfile, name='profile'),
    path('accounts/logout/',LoginView.as_view(authentication_form=UserLoginForm), name='Login'),
    path('accounts/logup/',register_view.as_view(), name='Register'),
    path('',include('django.contrib.auth.urls'))
]