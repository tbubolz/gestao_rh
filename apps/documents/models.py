from django.db import models
from apps.employees.models import Employees


class Documents(models.Model):
    name = models.CharField(max_length=70, help_text='Name of the Document')
    owner_employee = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
