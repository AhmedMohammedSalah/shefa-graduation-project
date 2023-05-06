from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, City
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        'age',
        'is_patient',
        'is_doctor',
        'is_lab_specialist', 'city', 'phone', 'specialist', 'name', 'image', 'manager_name', 'manager_phone','slug',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age', 'gender', 'birth_date', 'nid', 'is_patient', 'is_doctor',
                                        'is_lab_specialist', 'city', 'phone', 'specialist', 'name', 'image', 'manager_name', 'manager_phone','slug',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age', 'gender', 'birth_date', 'nid', 'is_patient',
                                                'is_doctor', 'is_lab_specialist', 'city', 'phone', 'specialist', 'name', 'image', 'manager_name', 'manager_phone','slug',)}),)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(City)
