from django.contrib import admin
from django.urls import path
from .views import TestCreateView,home

app_name="medicalAnalysis"

urlpatterns = [
    path('',home,name='login_home' ),
    path('upload_test',TestCreateView.as_view(),name='upload_test' ),

]