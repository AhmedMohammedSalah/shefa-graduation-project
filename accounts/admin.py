from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,City,Lab
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
        'is_lab_specialist'
        ,'city',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age','gender','birth_date','nid','is_patient','is_doctor','is_lab_specialist','city','phone','specialist')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age','gender','birth_date','nid','is_patient','is_doctor','is_lab_specialist','city','phone','specialist')}),)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(City)
admin.site.register(Lab)


