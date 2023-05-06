from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView 
from .models import MedicalTest
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from accounts.models import CustomUser
from .forms import UpdateUserForm
# Create your views here.


class TestCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = MedicalTest
    template_name = "upload_test.html"
    fields = ['title', 'image']
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)    
        form.fields['title'].widget.attrs['class'] = "form-control"
        form.fields['title'].widget.attrs['placeholder'] = "عنوان التحليل (اسم التحليل )"
        form.fields['image'].widget.attrs['class'] = "form-control"
        form.fields['image'].widget.attrs['placeholder'] = "صورة التحليل "
        form.fields['title'].label = ""
        form.fields['image'].label = ""
        return form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_patient or self.request.user.is_lab_specialist

    def get_success_url(self):
        return reverse('medicalAnalysis:login_home')

# S9KG2WAj_@BTC7$


def updateUser(request, slug):
    user = CustomUser.objects.get(slug=slug)
     # post or not
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
          

            # print ("done")
    else:
        form = UpdateUserForm()

    form.fields['first_name'].label = ""
    form.fields['first_name'].widget.attrs['value'] = user.first_name
    # end field
    form.fields['birth_date'].label = ""
    form.fields['birth_date'].widget.attrs['value'] = user.birth_date
    # end field
    form.fields['nid'].label = ""
    form.fields['nid'].widget.attrs['value'] = user.nid
    # end field
    
    form.fields['city'].label = ""
    form.fields['city'].widget.attrs['value'] = user.city
    # end field
    
    form.fields['gender'].label = ""
    form.fields['gender'].widget.attrs['value'] = user.gender
    # end field
    
    form.fields['phone'].label = ""
    form.fields['phone'].widget.attrs['value'] = user.phone
    # end field
    
    form.fields['username'].label = ""
    form.fields['username'].help_text = ""
    form.fields['username'].widget.attrs['value'] = user.username
    # end field
    
    form.fields['email'].label = ""
    form.fields['email'].widget.attrs['value'] = user.email
    # end field
    
    form.fields['password1'].label = ""
    # end field
    
    form.fields['password2'].label = ""
    # end field
    
    context = {'form': form}
    return render(request, 'psettings.html', context)

class TestsListView(UserPassesTestMixin, LoginRequiredMixin,ListView):
    model = MedicalTest
    template_name = "p_history.html"
    context_object_name='tests'
    def test_func(self):
        return self.request.user.is_patient or self.request.user.is_lab_specialist
        

@login_required
def home(request):
    if request.user.is_patient:
        context = {}
        return render(request, 'patient.html', context)
    elif request.user.is_doctor:
        context = {}
        return render(request, 'doctor.html', context)
    elif request.user.is_lab_specialist:
        context = {}
        return render(request, 'lab_specialist.html', context)
