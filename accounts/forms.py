from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm 

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields = UserCreationForm.Meta.fields + ('age','gender','birth_date','nid','city','phone','first_name','email','specialist')

class PatientCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields = UserCreationForm.Meta.fields + ('age','gender','birth_date','nid','city','phone','first_name','email','specialist','name','image','manager_name','manager_phone',)
class DoctorCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields = UserCreationForm.Meta.fields + ('age','gender','birth_date','nid','city','phone','first_name','email','specialist','name','image','manager_name','manager_phone',)


class LabCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields = UserCreationForm.Meta.fields + ('age','birth_date','nid','city','phone','first_name','email','name','manager_name','manager_phone',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


