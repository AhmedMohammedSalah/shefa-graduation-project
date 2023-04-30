from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import CreateView
from django.template import RequestContext
from .forms import CustomUserCreationForm

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def login(request):
    form = AuthenticationForm(request)
    form.fields['username'].widget.attrs['class'] = "form-control"
    form.fields['username'].widget.attrs['placeholder'] = "اسم المستخدم"
    form.fields['password'].widget.attrs['class'] = "form-control"
    form.fields['password'].widget.attrs['placeholder'] = "كلمة المرور "
    form.fields['username'].label = ""
    form.fields['password'].label = ""
    msg = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                msg.append("login successful")

            else:
                msg.append("disabled account")
        else:
            msg.append("invalid login")
        return redirect(reverse('medicalAnalysis:login_home'))
    return render(request, "registration/login.html", {'form': form, 'errors': msg})
