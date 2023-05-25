from accounts.models import CustomUser
from django import forms
from .models import MedicalTest
class DeleteUser(forms.Form):
    """DeleteUser definition."""
    class Meta:
        """Meta definition for ApplyForm."""
        model = CustomUser
        fields = []

    # TODO: Define form fields here

class UpdateDoctorForm(forms.ModelForm):
    """Form definition for ApplyForm."""
    password1 = forms.CharField(strip=False)
    password2 = forms.CharField(strip=False)

    class Meta:
        """Meta definition for ApplyForm."""
        model = CustomUser
        fields = ['first_name', 'city',
                    'gender', 'phone', 'username', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super(UpdateDoctorForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UpdatePatientForm(forms.ModelForm):
    """Form definition for ApplyForm."""
    password1 = forms.CharField(strip=False)
    password2 = forms.CharField(strip=False)

    class Meta:
        """Meta definition for ApplyForm."""
        model = CustomUser
        fields = ['first_name',  'birth_date', 'nid', 'city',
                    'gender', 'phone', 'username', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super(UpdatePatientForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UpdateLapForm(forms.ModelForm):
    """Form definition for ApplyForm."""
    password1 = forms.CharField(strip=False)
    password2 = forms.CharField(strip=False)

    class Meta:
        """Meta definition for ApplyForm."""
        model = CustomUser
        fields = ['name',  'image', 'city',
                    'manager_name', 'phone', 'username', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super(UpdateLapForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserSearchForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    

    def search_user(self):
        username = self.cleaned_data.get('username')
        try:
            user = CustomUser.objects.get(username=username)
            return user
        except CustomUser.DoesNotExist:
            return None    
