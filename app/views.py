from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.
from app.models import *

# git remote add origin https://github.com/Satishkumaryanala/ClassViews_CRUD.git
# git push -u origin main

class SchoolList(ListView):
    model = School
    context_object_name = 'Schools'


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