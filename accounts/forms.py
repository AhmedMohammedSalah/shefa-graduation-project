from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm ,AuthenticationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields = UserCreationForm.Meta.fields + ('age','gender','birth_date','nid','is_patient','is_doctor','is_lab_specialist','city',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


