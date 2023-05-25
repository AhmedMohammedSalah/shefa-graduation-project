from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.template.defaultfilters import slugify


def image_upload(instance, filename):
    image_name, extension = filename.split(".")
    return "labs/%s/%s.%s" % (instance.name, instance.name, extension)


class CustomUser(AbstractUser):
    user_gender = (
        ("male", "ذكر"),
        ("female", "أنثى"),)
    gender = models.CharField(
        max_length=10, choices=user_gender, default="male", null=True, blank=True)
    birth_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    nid = models.CharField(max_length=14, null=True, blank=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_lab_specialist = models.BooleanField(default=False)
    city = models.ForeignKey('City', related_name="user_city",
                             on_delete=models.CASCADE, blank=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    specialist = models.CharField(max_length=50, blank=True, null=True)
    # lab fields
    name = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to=image_upload, blank=True, null=True)
    manager_name = models.CharField(max_length=30, blank=True, null=True)
    manager_phone = models.CharField(max_length=11, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)
