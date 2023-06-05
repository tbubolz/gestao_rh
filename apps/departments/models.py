from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the Department')

    def __str__(self):
        return self.name
