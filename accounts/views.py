from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import CreateView
from django.template import RequestContext
from .forms import PatientCreationForm, DoctorCreationForm,LabCreationForm

# Create your views here.


class CustomUserSignUpView(CreateView):
    form_class = PatientCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form2 = DoctorCreationForm()
    
        # Modify form3
        form3 = LabCreationForm()
        # name ,city ,manager_name,phone,email,username
        
        # form 2
        form2.fields['username'].widget.attrs['class'] = "form-control form-control"
        form2.fields['username'].label = ""
        form2.fields['username'].help_text = ""
        # end
        
        form2.fields['email'].widget.attrs['class'] = "form-control form-control"
        form2.fields['email'].label = ""
        form2.fields['email'].help_text = ""
        # end 
        
        form2.fields['specialist'].widget.attrs['class'] = "form-control form-control"
        form2.fields['specialist'].label = ""
        form2.fields['specialist'].help_text = ""
        # end 
        form2.fields['city'].widget.attrs['class'] = "form-control form-control"
        form2.fields['city'].label = ""
        form2.fields['city'].help_text = ""
        # end 
        
        form2.fields['first_name'].label = ""
        form2.fields['first_name'].widget.attrs['class'] = "form-control form-control"
        form2.fields['first_name'].help_text = ""
        # end
        form2.fields['gender'].widget.attrs['class'] = "form-control form-control"
        form2.fields['gender'].label = ""
        form2.fields['gender'].help_text = ""
        # end
        form2.fields['city'].widget.attrs['class'] = "form-control form-control"
        form2.fields['city'].label = ""
        form2.fields['city'].help_text = ""
        # end
        form2.fields['phone'].widget.attrs['class'] = "form-control form-control"
        form2.fields['phone'].label = ""
        form2.fields['phone'].help_text = ""
        # end
        form2.fields['password1'].widget.attrs['class'] = "form-control form-control"
        form2.fields['password1'].label = ""
        form2.fields['password1'].help_text = ""
        # end
        form2.fields['password2'].widget.attrs['class'] = "form-control form-control"
        form2.fields['password2'].label = ""
        form2.fields['password2'].help_text = ""
        # end
        # form3
        form3.fields['username'].widget.attrs['class'] = "form-control form-control"
        form3.fields['username'].label = ""
        form3.fields['username'].help_text = ""
        # end
        form3.fields['password1'].widget.attrs['class'] = "form-control form-control"
        form3.fields['password1'].label = ""
        form3.fields['password1'].help_text = ""
        # end
        form3.fields['password2'].widget.attrs['class'] = "form-control form-control"
        form3.fields['password2'].label = ""
        form3.fields['password2'].help_text = ""
        # end
        form3.fields['name'].widget.attrs['class'] = "form-control form-control"
        form3.fields['name'].label = ""
        form3.fields['name'].help_text = ""
        # end
        form3.fields['city'].widget.attrs['class'] = "form-control form-control"
        form3.fields['city'].label = ""
        form3.fields['city'].help_text = ""
        # end
        form3.fields['manager_name'].widget.attrs['class'] = "form-control form-control"
        form3.fields['manager_name'].label = ""
        form3.fields['manager_name'].help_text = ""
        # end
        form3.fields['phone'].widget.attrs['class'] = "form-control form-control"
        form3.fields['phone'].label = ""
        form3.fields['phone'].help_text = ""
        # end
        form3.fields['email'].widget.attrs['class'] = "form-control form-control"
        form3.fields['email'].label = ""
        form3.fields['email'].help_text = ""
        # end
        
        
        
        
        # Assign the modified forms to the context
            
        context['form2'] = form2
        context['form3'] = form3
        return context
    def form_valid(self, form):
        if form.instance.specialist==None and form.instance.name ==None:
            form.instance.is_doctor = False
            form.instance.is_lab_specialist = False
            form.instance.is_patient = True
            def get_success_url(self):
                return reverse('medicalAnalysis:login_home')

        
            return super().form_valid(form)
        elif form.instance.specialist!=None and form.instance.name ==None:
            form.instance.is_lab_specialist = False
            form.instance.is_patient = False
            form.instance.is_doctor = True
            def get_success_url(self):
                return reverse('medicalAnalysis:login_home')
            return super().form_valid(form)
        else:
            print("is_lab_specialist")
            form.instance.is_doctor = False
            form.instance.is_patient = False
            form.instance.is_lab_specialist = True
            
            def get_success_url(self):
                return reverse('medicalAnalysis:login_home')
            return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # form1
        form.fields['username'].widget.attrs['class'] = "form-control form-control"
        form.fields['username'].label = ""
        form.fields['username'].help_text = ""
        # end
        form.fields['first_name'].widget.attrs['class'] = "form-control form-control"
        form.fields['first_name'].label = ""
        form.fields['first_name'].help_text = ""
        # end
        form.fields['gender'].widget.attrs['class'] = "form-control form-control"
        form.fields['gender'].label = ""
        form.fields['gender'].help_text = ""
        # end
        form.fields['city'].widget.attrs['class'] = "form-control form-control"
        form.fields['city'].label = ""
        form.fields['city'].help_text = ""
        # end
        form.fields['birth_date'].widget.attrs['class'] = "form-control form-control"
        form.fields['birth_date'].label = ""
        form.fields['birth_date'].help_text = ""
        # end
        form.fields['nid'].widget.attrs['class'] = "form-control form-control"
        form.fields['nid'].label = ""
        form.fields['nid'].help_text = ""
        # end
        form.fields['phone'].widget.attrs['class'] = "form-control form-control"
        form.fields['phone'].label = ""
        form.fields['phone'].help_text = ""
        # end
        form.fields['password1'].widget.attrs['class'] = "form-control form-control"
        form.fields['password1'].label = ""
        form.fields['password1'].help_text = ""
        # end
        form.fields['password2'].widget.attrs['class'] = "form-control form-control"
        form.fields['password2'].label = ""
        form.fields['password2'].help_text = ""
        # end
        form.fields['gender'].widget.attrs['class'] = "form-control form-control"
        form.fields['gender'].label = ""
        form.fields['gender'].help_text = ""
        # end
        
        return form


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
