
from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
# Create your models here.
def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "tests/%s/%s.%s" % (instance.user, instance.title, extension)

class MedicalTest(models.Model):
    test_type=models.CharField(max_length=50, default="anemia")
    user=models.ForeignKey( CustomUser,on_delete=models.CASCADE)
    title=models.CharField( max_length=30) 
    image=models.ImageField( upload_to=image_upload, height_field=None, width_field=None, max_length=None)
    upload_date=models.DateTimeField( auto_now=True, auto_now_add=False)
    result = models.CharField(max_length=50,blank=True,null=True)
    review=models.CharField( max_length=150,blank=True,null=True)
    rate1=models.BooleanField(default=False)
    rate2=models.BooleanField(default=False)
    rate3=models.BooleanField(default=False)
    rate4=models.BooleanField(default=False)
    rate5=models.BooleanField(default=False)
    reviewed_by=models.ForeignKey( CustomUser,on_delete=models.CASCADE,related_name='reviewed_doctor',blank=True,null=True)
    def __str__(self):
        return ( str(self.title) )
