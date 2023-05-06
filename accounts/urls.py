from django.urls import path
from .views import CustomUserSignUpView,login
app_name='accounts'
urlpatterns = [
    path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path("login/",login,name="login")
]