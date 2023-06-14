from django.views.generic.edit import CreateView, UpdateView
from .models import Company
from django.http import HttpResponse


class CompanyCreate(CreateView):
    model = Company
    fields = [
        'name'
    ]

    def form_valid(self, form):
        obj = form.save()
        employee = self.request.user.employees
        employee.company = obj
        employee.save()
        return HttpResponse('OK')


class CompanyEdit(UpdateView):
    model = Company
    fields = [
        'name'
    ]

