from accounts.models import CustomUser
from django import forms


class UpdateUserForm(forms.ModelForm):
    """Form definition for ApplyForm."""
    password1 = forms.CharField(strip=False)
    password2 = forms.CharField(strip=False)

    class Meta:
        """Meta definition for ApplyForm."""
        model = CustomUser
        fields = ['first_name', 'last_name', 'birth_date', 'nid', 'city',
                    'gender', 'phone', 'username', 'email', 'password1', 'password2']
    def save(self, commit=True):
        user = super(UpdateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user