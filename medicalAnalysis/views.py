from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import MedicalTest
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from accounts.models import CustomUser
from .forms import UpdatePatientForm, DeleteUser, UpdateLapForm, UpdateDoctorForm,UserSearchForm
from django.contrib.auth import logout, authenticate, login
from .machine_result import update_result

# Create your views here.

from django.contrib import messages
class TestCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = MedicalTest
    template_name = "upload_test.html"
    fields = ['title', 'image']

    error_message = None 
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
        if self.request.user.is_patient:
            form.instance.user = self.request.user
        else:
            username = self.request.POST.get('username')
            try:
                user = CustomUser.objects.get(username=username, is_patient=True)
                form.instance.user = user
            except CustomUser.DoesNotExist:
                messages.error(self.request, 'المريض غير موجود من فضلك قم باضافته ')
    
                return self.form_invalid(form) 
        response= super().form_valid(form)
        update_result(self.object)
        return response
    def test_func(self):
        return self.request.user.is_patient or self.request.user.is_lab_specialist

    def get_success_url(self):
        return reverse('medicalAnalysis:result', args=(self.object.id,))
    def get_template_names(self):
        if self.request.user.is_patient:
            template_names = ['upload_test.html']
        elif self.request.user.is_lab_specialist:
            template_names = ['send-result.html']
        return template_names

# S9KG2WAj_@BTC7$


@login_required
def updatePatient(request, slug):
    user = CustomUser.objects.get(slug=slug)

    # post or not
    if request.method == 'POST':
        form = UpdatePatientForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            # user.save()
            # # إنشاء session مرة أخرى
            user = authenticate(
                request, username=request.user.username, password=request.POST.get('password1'))
            if user is not None:
                login(request, user)
            return redirect('medicalAnalysis:login_home')

    else:
        form = UpdatePatientForm()
    form.fields['first_name'].widget.attrs['class'] = "form-control"
    form.fields['first_name'].label = ""
    form.fields['first_name'].widget.attrs['value'] = user.first_name
    # end field
    form.fields['birth_date'].widget.attrs['class'] = "form-control"
    form.fields['birth_date'].label = ""
    form.fields['birth_date'].widget.attrs['value'] = user.birth_date
    # end field
    form.fields['nid'].widget.attrs['class'] = "form-control"
    form.fields['nid'].label = ""
    form.fields['nid'].widget.attrs['value'] = user.nid
    # end field

    form.fields['city'].widget.attrs['class'] = "form-control"
    form.fields['city'].label = ""
    form.fields['city'].widget.attrs['value'] = user.city
    # end field

    form.fields['gender'].widget.attrs['class'] = "form-control"
    form.fields['gender'].label = ""
    form.fields['gender'].widget.attrs['value'] = user.gender
    # end field

    form.fields['phone'].widget.attrs['class'] = "form-control"
    form.fields['phone'].label = ""
    form.fields['phone'].widget.attrs['value'] = user.phone
    # end field

    form.fields['username'].widget.attrs['class'] = "form-control"
    form.fields['username'].label = ""
    form.fields['username'].help_text = ""
    form.fields['username'].widget.attrs['value'] = user.username
    # end field

    form.fields['email'].widget.attrs['class'] = "form-control"
    form.fields['email'].label = ""
    form.fields['email'].widget.attrs['value'] = user.email
    # end field

    form.fields['password1'].widget.attrs['class'] = "form-control"
    form.fields['password1'].label = ""
    # end field

    form.fields['password2'].widget.attrs['class'] = "form-control"
    form.fields['password2'].label = ""
    # end field

    context = {'form': form}
    return render(request, 'psettings.html', context)


class TestsListView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = MedicalTest
    template_name = "p_history.html,"
    context_object_name = 'tests'

    def get_template_names(self):
        if self.request.user.is_patient:
            template_names = ['p_history.html']
        elif self.request.user.is_lab_specialist:
            template_names = ['l-patients.html']
        elif self.request.user.is_doctor:
            template_names = ['tests.html']
        return template_names
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     return render(request, self.get_template_names(), {'form': form})

    def test_func(self):
        return self.request.user.is_patient or self.request.user.is_lab_specialist or self.request.user.is_doctor


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


@login_required
def updateDoctor(request, slug):
    user = CustomUser.objects.get(slug=slug)

    # post or not
    if request.method == 'POST':

        form = UpdateDoctorForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            # user.save()
              # # إنشاء session مرة أخرى
            user = authenticate(
                request, username=request.user.username, password=request.POST.get('password1'))
            if user is not None:
                login(request, user)
    else:
        form = UpdateDoctorForm()
    context = {'form': form}
    form.fields['first_name'].label = ""
    form.fields['first_name'].widget.attrs['value'] = user.first_name
    # end field

    form.fields['gender'].label = ""
    form.fields['gender'].widget.attrs['value'] = user.gender
    # end field

    form.fields['city'].label = ""
    form.fields['city'].widget.attrs['value'] = user.city
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

    return render(request, 'dsettings.html', context)


@login_required
def updateLab(request, slug):
    user = CustomUser.objects.get(slug=slug)

    # post or not
    if request.method == 'POST':

        form = UpdateLapForm(request.POST, request.FILES,
                            instance=request.user)

        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.user.username, password=request.POST.get('password1'))
            if user is not None:
                login(request, user)
            # user.save()
    else:
        form = UpdateLapForm()
        
    form.fields['name'].widget.attrs['class'] = "form-control form-control"
    form.fields['name'].label = ""
    form.fields['name'].widget.attrs['value'] = user.name
    # end field
    form.fields['image'].widget.attrs['class'] = "form-control form-control"
    form.fields['image'].label = ""
    form.fields['image'].widget.attrs['value'] = user.image
    # end field
    form.fields['manager_name'].widget.attrs['class'] = "form-control form-control"
    form.fields['manager_name'].label = ""
    form.fields['manager_name'].widget.attrs['value'] = user.manager_name
    # end field
    form.fields['city'].widget.attrs['class'] = "form-control form-control"
    form.fields['city'].label = ""
    form.fields['city'].widget.attrs['value'] = user.city
    # end field
    form.fields['phone'].widget.attrs['class'] = "form-control form-control"
    form.fields['phone'].label = ""
    form.fields['phone'].widget.attrs['value'] = user.phone
    # end field

    form.fields['username'].widget.attrs['class'] = "form-control form-control"
    form.fields['username'].label = ""
    form.fields['username'].help_text = ""
    form.fields['username'].widget.attrs['value'] = user.username
    # end field

    form.fields['email'].widget.attrs['class'] = "form-control form-control"
    form.fields['email'].label = ""
    form.fields['email'].widget.attrs['value'] = user.email
    # end field

    form.fields['password1'].widget.attrs['class'] = "form-control form-control"
    form.fields['password1'].label = ""
    # end field

    form.fields['password1'].widget.attrs['class'] = "form-control form-control"
    form.fields['password2'].label = ""
    context = {'form': form}
    return render(request, 'lsettings.html', context)


class LapDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "lab_deleted.html"
    success_url = reverse_lazy('medicalAnalysis:login_home')

    def delete(self, request, *args, **kwargs):
        """
        Overrides delete method to logout the user before deleting their account.
        """
        logout(request)
        return super().delete(request, *args, **kwargs)


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "doctor_deleted .html"
    success_url = reverse_lazy('medicalAnalysis:login_home')

    def delete(self, request, *args, **kwargs):
        """
        Overrides delete method to logout the user before deleting their account.
        """
        logout(request)
        return super().delete(request, *args, **kwargs)


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "p_deleted.html"
    success_url = reverse_lazy('medicalAnalysis:login_home')

    def delete(self, request, *args, **kwargs):
        """
        Overrides delete method to logout the user before deleting their account.
        """
        logout(request)
        return super().delete(request, *args, **kwargs)

class ResultDetailView(DetailView):
    model = MedicalTest
    template_name = 'report-result.html'
    context_object_name = 'test'
    
    

def search_user(request):
    error_message = None 
    if request.method == 'POST':
        form = UserSearchForm(request.POST)
        if form.is_valid():
            user = form.search_user()
            if user and user.is_patient:
                # استرد نتائج التحاليل الخاصة بالمستخدم وقم بتمريرها إلى القالب
                test_results = MedicalTest.objects.filter(user=user)
                return render(request, 'd_p_history.html', { 'tests': test_results})
            else:
                error_message = 'المريض غير موجود ' 
    else:
        form = UserSearchForm()

    return render(request, 'patient-search.html', {'form': form, 'error_message': error_message})


class RateUpdateView(UpdateView):
    model = MedicalTest
    template_name = "report-review.html"
    fields = ['rate1','rate4','rate2','rate3','rate5','review','reviewed_by']
    def get_success_url(self):
        return reverse('medicalAnalysis:lab_patients')
    def form_valid(self, form):
        if form.instance.rate2:
            form.instance.rate1=True
        if form.instance.rate3:
            form.instance.rate1=True
            form.instance.rate2=True        
        if form.instance.rate4:
            form.instance.rate1=True
            form.instance.rate2=True
            form.instance.rate3=True        
        if form.instance.rate5:
            form.instance.rate1=True
            form.instance.rate2=True
            form.instance.rate3=True
            form.instance.rate4=True
        test = form.save(commit=False)  # الحصول على النموذج المقدم وعدم حفظه حتى الآن
        test.reviewed_by = self.request.user  # تعيين الحقل reviewed_by بالمستخدم المقدم
        test.save() 
        return super().form_valid(form)   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        test = MedicalTest.objects.get(pk=self.kwargs['pk'])
        context['test'] = test
        return context



from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')


class AddPatientView(CreateView):
    model = CustomUser
    template_name = 'add-patient.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('medicalAnalysis:upload_test')

    def form_valid(self, form):
        form.instance.is_patient = True
        return super().form_valid(form)
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # form.fields['image'].widget.attrs['placeholder'] = "صورة التحليل "
        form.fields['username'].label = "ادخل اسم المستخدم "
        form.fields['password1'].label = "ادخل كلمة المرور"
        form.fields['username'].help_text = "يجب ان يكون اسم المستخدم مكتوب باللغة الانجليزية   "
        form.fields['password2'].label = "تاكيد كلمة المرور "
        form.fields['password1'].help_text = "كلمة المرور تكون كبي رة ومكونة من ارقام وحروف"
        form.fields['password2'].help_text = "يجب ان تكون كلمتان المرور متطابقتين"
        return form
# class AddPatientView(LoginRequiredMixin,CreateView):
#     model = CustomUser
#     template_name = 'add-patient.html'
#     success_url = reverse_lazy('medicalAnalysis:upload_test')
#     fields=["username","password1","is_patient"]

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password1 = form.cleaned_data['password1']
#         form.instance.is_patient = True
        
#         return super().form_valid(form)


