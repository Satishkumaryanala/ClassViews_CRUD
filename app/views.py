from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
from app.models import *

# git remote add origin https://github.com/Satishkumaryanala/ClassViews_CRUD.git
# git push -u origin main

class SchoolList(ListView):
    model = School
    context_object_name = 'Schools'

class StudentList(ListView):
    model = Student
    context_object_name = 'students'

class SchoolDetails(DetailView):
    model = School
    context_object_name = 'SCO'

class SchoolCreate(CreateView):
    model = School
    fields = '__all__'

class StudentCreate(CreateView):
    model = Student
    fields = '__all__'

class StudentDetails(DetailView):
    model = Student
    context_object_name = 'STO'

class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'

class SchoolDelete(DeleteView):
    model = School
    context_object_name = 'SOD'
    success_url = reverse_lazy('SchoolList')

