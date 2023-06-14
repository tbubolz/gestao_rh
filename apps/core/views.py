from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.employees.models import Employees


@login_required()
def home(request):
    data = {'user': request.user}
    return render(request, 'core/index.html', data)

