from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 , redirect
from django.db.models import Q
from .models import Courses, Batch, Person, Image, Contact
from django.views.generic import CreateView,DeleteView,UpdateView, View, ListView , DetailView
from django.core.urlresolvers import reverse_lazy
from .forms import Userform
import re


class apply(CreateView):
    model = Person()
    fields = ['email_id', 'resume_file']
    template_name = 'intern/apply.html'


def contact(request):
    all_courses = Courses.objects.all()
    all_batch = Batch.objects.all()
    all_contact = Contact.objects.all()
    return render(request, 'intern/contact.html', {'all_courses': all_courses, 'all_batch': all_batch, 'all_contact': all_contact})

def new(request):
    ur_Person = Person.objects.filter(user=request.user)
    return render(request, 'intern/ur_index.html', {'ur_Person': ur_Person})



class ap_detail(DetailView):
    model = Person
    template_name = 'intern/in_detail.html'


'''class create_Person(CreateView):
    model = Person
    fields = ['company', 'company_logo', 'Post', 'about', 'role', 'time', 'benefits', 'skills']

class update_Person(UpdateView):
    model = Person
    fields = ['company', 'company_logo', 'Post', 'about', 'role', 'time', 'benefits', 'skills']
'''
class delete_Person(DeleteView):
    model = Person
    success_url = reverse_lazy('intern:index')

class UserFormView(View):
    form_class = Userform
    template_name = 'intern/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit= False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username , password = password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('intern:index')
        return render(request, self.template_name, {'form': form})

def base(request):
    all_courses = Courses.objects.all()
    all_batch = Batch.objects.all()
    return render(request, 'intern/base.html', {'all_courses': all_courses,'all_batch': all_batch})


def internship(request):
    all_Person = Person.objects.all()
    return render(request, 'intern/internship.html', {'all_Person': all_Person})

def imggallery(request):
    all_courses = Courses.objects.all()
    all_batch = Batch.objects.all()
    img = Image.objects.all()
    return render(request, 'intern/contact1.html', {'all_courses': all_courses, 'all_batch': all_batch , 'img':img })

def cgallery(request , courses_Course):
    all_courses = Courses.objects.all()
    all_batch = Batch.objects.all()
    all_image = get_object_or_404(Courses, pk=courses_Course)
    return render(request, 'intern/cgallery.html', {'all_courses': all_courses, 'all_batch': all_batch , 'all_image': all_image })

def career(request):
    all_courses = Courses.objects.all()
    all_batch = Batch.objects.all()
    return render(request, 'intern/career.html', {'all_courses': all_courses, 'all_batch': all_batch})

def home(request):
    all_courses = Courses.objects.all()
    all_batch = Batch.objects.all()
    return render(request, 'intern/home.html', {'all_courses': all_courses,'all_batch': all_batch})


def detail(request, courses_Course, batch_Batch_No):
    all_courses = Courses.objects.all()
    all_batch = Batch.objects.all()
    batch = get_object_or_404(Batch, pk=batch_Batch_No)
    courses = get_object_or_404(Courses, pk=courses_Course)
    return render(request, 'intern/detail.html', {'all_courses': all_courses,'all_batch': all_batch, 'batch': batch, 'courses': courses})


def pdetail(request, person_id):
    all_courses = Courses.objects.all()
    all_batch = Batch.objects.all()
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'intern/pdetail.html', {'all_courses': all_courses,'all_batch': all_batch,'person': person})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                Person = Person.objects.filter(user=request.user)
                return render(request, 'intern/base.html', {'Person': Person})
            else:
                return render(request, 'intern/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'intern/login.html', {'error_message': 'Invalid login'})
    return render(request, 'intern/login.html')
