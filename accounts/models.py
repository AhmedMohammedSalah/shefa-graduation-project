from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    user_gender = (
        ("male", "ذكر"),
        ("female", "أنثى"),)
    gender = models.CharField(max_length=10, choices=user_gender, default="male")
    birth_date = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    nid = models.CharField(max_length=14)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_lab_specialist = models.BooleanField(default=False)
    city = models.ForeignKey('City', related_name="user_city",on_delete=models.CASCADE, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone =models.CharField( max_length=11,null=True, blank=True)
    specialist=models.CharField(max_length=50,blank=True, null=True)
    
class City(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.name)




def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "labs/%s/%s.%s" % (instance.name, instance.name, extension)
class Lab (models.Model):
    name =models.TextField(max_length=60)
    image=models.ImageField(upload_to=image_upload)
    city =models.ForeignKey("City", blank=True, null=True, related_name="lab_city",on_delete=models.CASCADE)
    manager=models.OneToOneField("CustomUser",on_delete=models.CASCADE, related_name="lab_manager")
    empolyess=models.ForeignKey("CustomUser", on_delete=models.CASCADE, related_name="lab_empolyee")
    
