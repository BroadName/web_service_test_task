from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UnitForm, EmployeeForm

from .models import Unit, Employee


def list_units(request):
    units = Unit.objects.all()
    context = {'units': units}
    return render(request, 'units/list_units.html', context)


def detail_unit(request, unit_id):
    unit = Unit.objects.filter(pk=unit_id).first()
    context = {'unit': unit}
    return render(request, 'units/detail_unit.html', context)


class UnitCreateView(CreateView):
    template_name = 'units/unit_create.html'
    form_class = UnitForm
    success_url = reverse_lazy('list_units')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['units'] = Unit.objects.all()
        return context


def list_employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'employees/list_employees.html', context)


def detail_employee(request, employee_id):
    employee = Employee.objects.filter(pk=employee_id).first()
    context = {'employee': employee}
    return render(request, 'employees/detail_employee.html', context)


class EmployeeCreateView(CreateView):
    template_name = 'employees/employee_create.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('list_employees')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context
