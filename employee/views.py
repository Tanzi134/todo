from django.shortcuts import render
from employee.models import Employee
from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse
from employee.models import Employee

# Create your views here.
def employee_details(request, pk):
    employee = get_object_or_404 (Employee, pk=pk )
    context = {
        'employee': employee,
    }
    return render(request,'employee_details.html', context)