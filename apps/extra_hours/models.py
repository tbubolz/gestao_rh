from django.db import models
from apps.employees.models import Employees


class Extra_Hours(models.Model):
    hours = models.IntegerField()
    employee = models.ForeignKey(Employees, on_delete=models.PROTECT)

