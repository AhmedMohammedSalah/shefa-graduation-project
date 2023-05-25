from django.urls import path
from .views import CustomUserSignUpView,login
from django.views.generic.base import TemplateView  
app_name='accounts'
urlpatterns = [
    path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path("login/",login,name="login"),
]