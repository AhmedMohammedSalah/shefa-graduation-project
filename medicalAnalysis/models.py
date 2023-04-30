
from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Create your models here.
def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "tests/%s/%s.%s" % (instance.user, instance.title, extension)

class MedicalTest(models.Model):
    test_types = (
        ("anemia", "أنيميا"),
        ("anemia-hada", "أنيميا حادة "),)
    test_type=models.CharField(max_length=50, choices=test_types, default="anemia")
    user=models.ForeignKey( CustomUser,on_delete=models.CASCADE)
    title=models.CharField( max_length=30)
    image=models.ImageField( upload_to=image_upload, height_field=None, width_field=None, max_length=None)
    upload_date=models.DateTimeField( auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return ( self.title)
