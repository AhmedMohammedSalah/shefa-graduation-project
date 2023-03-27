from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import MedicalTest
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse 
# Create your views here.

class TestCreateView(UserPassesTestMixin,LoginRequiredMixin,CreateView):
    model = MedicalTest
    template_name = "upload_test.html"
    fields=['title','test_type','image']
    
    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super().form_valid(form)
    def test_func(self):
            return self.request.user.is_patient
    def get_success_url(self):
        return reverse('medicalAnalysis:login_home')
    
# S9KG2WAj_@BTC7$
@login_required
def home (request):
    if request.user.is_patient:
        context = {}
        return render(request, 'patient.html', context)
    elif request.user.is_doctor:
        context = {}
        return render(request, 'doctor.html', context)
    elif request.user.is_lab_specialist:
        context = {}
        return render(request, 'lab_specialist.html', context)