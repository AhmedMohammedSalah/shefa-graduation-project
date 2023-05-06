from django.contrib import admin
from django.urls import path
from .views import TestCreateView,home,TestsListView,updateUser

app_name="medicalAnalysis"

urlpatterns = [
    path('',home,name='login_home' ),
    path('upload_test',TestCreateView.as_view(),name='upload_test' ),
    path('tests',TestsListView.as_view(),name='tests' ),
    path('setting/<str:slug>/',updateUser,name='setting' ),

]