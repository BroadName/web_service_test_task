import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView

from .forms import UnitForm, EmployeeForm, EditUnitForm, EditEmployeeForm

from .models import Unit, Employee


def list_units(request):
    units = Unit.objects.filter(is_active=True).all()
    context = {'units': units}
    return render(request, 'units/list_units.html', context)


def detail_unit(request, unit_id):
    unit = Unit.objects.filter(pk=unit_id).first()
    context = {'unit': unit}
    return render(request, 'units/detail_unit.html', context)


def terminate_unit(request, unit_id):
    unit = get_object_or_404(Unit, pk=unit_id)
    unit.is_active = not unit.is_active
    unit.liquidation_date = datetime.date.today()
    unit.save()
    return redirect(reverse('list_units'))


class UnitCreateView(CreateView):
    template_name = 'units/unit_create.html'
    form_class = UnitForm
    success_url = reverse_lazy('list_units')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['units'] = Unit.objects.all()
    #     return context


class UnitUpdateView(UpdateView):
    model = Unit
    template_name = 'units/edit_unit.html'
    form_class = EditUnitForm
    success_url = reverse_lazy('list_units')


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['employees'] = Employee.objects.all()
    #     return context


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employees/edit_employee.html'
    form_class = EditEmployeeForm
    success_url = reverse_lazy('list_employees')
