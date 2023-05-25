from django.contrib import admin
from django.urls import path
from .views import TestCreateView, home, TestsListView, updatePatient, updateLab, updateDoctor, LapDeleteView, PatientDeleteView, DoctorDeleteView, ResultDetailView, search_user, RateUpdateView, AddPatientView

app_name = "medicalAnalysis"

urlpatterns = [
    path('', home, name='login_home'),
    path('upload_test', TestCreateView.as_view(), name='upload_test'),
    path('tests', TestsListView.as_view(), name='tests'),
    path('setting/<str:slug>/delete',
         PatientDeleteView.as_view(), name='p_delete'),
    path('setting/<str:slug>/', updatePatient, name='setting'),

    path('lab/add-patient/', AddPatientView.as_view(), name='add_patient'),
    # AddPatientView
    path('lab-setting/<str:slug>/', updateLab, name='lab_setting'),
    path('lab-setting/<str:slug>/delete',
         LapDeleteView.as_view(), name='lab_delete'),

    path('doctor-setting/<str:slug>/', updateDoctor, name='doctor_setting'),
    path('doctor-setting/<str:slug>/delete',
         DoctorDeleteView.as_view(), name='doctor_delete'),
    path('lab-patients', TestsListView.as_view(), name='lab_patients'),
    path('result/<int:pk>/', ResultDetailView.as_view(), name='result'),
    path('result-review/<int:pk>/', RateUpdateView.as_view(), name='result_review'),
    path('doctor-search/', search_user, name='doctor_search'),

    # search_user

]
