from django.urls import path
from .views import SignUpView,login
app_name='accounts'
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/",login,name="login")
]