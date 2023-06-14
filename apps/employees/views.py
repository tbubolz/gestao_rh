from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Employees


class EmployeesList(ListView):
    model = Employees