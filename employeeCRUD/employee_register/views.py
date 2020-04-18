from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Here are the views for every page in the app


def employee_list(request):
    context = {"employee_list": Employee.objects.all()}
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        # INSERT
        if id == 0:
            form = EmployeeForm()
        # UPDATE
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {"form": form})
    else:
        # INSERT
        if id == 0:
            form = EmployeeForm(request.POST)
        # UPDATE
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect("/employee/list")


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

