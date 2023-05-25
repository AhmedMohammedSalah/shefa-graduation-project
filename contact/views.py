from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_message(request):
    info=Info.objects.first
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        send_mail(
            name,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )
    else:
        pass
    context={'info':info}
    return render (request ,'contact/contact.html',context)
