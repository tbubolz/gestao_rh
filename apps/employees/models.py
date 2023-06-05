from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the employee')
