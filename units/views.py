import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView

from .forms import UnitForm, EmployeeForm, EditUnitForm, EditEmployeeForm, TransferEmployeeForm, SearchEmployeesForm

from .models import Unit, Employee, TransferEmployee


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
    return redirect(reverse('unit_detail', kwargs={'unit_id': unit_id}))


class UnitCreateView(CreateView):
    template_name = 'units/unit_create.html'
    form_class = UnitForm
    success_url = reverse_lazy('list_units')


class UnitUpdateView(UpdateView):
    model = Unit
    template_name = 'units/edit_unit.html'
    form_class = EditUnitForm
    success_url = reverse_lazy('list_units')


def list_employees(request):
    form = SearchEmployeesForm(request.GET)
    employees = Employee.objects.all().filter(termination_date=None)
    if form.is_valid():
        start = form.cleaned_data.get('start')
        end = form.cleaned_data.get('end')
        kind = form.cleaned_data.get('kind_employee')
        if start and end:
            if kind == 'termination_date':
                employees = Employee.objects.filter(termination_date__range=(start, end))
            elif kind == 'entry_date':
                employees = Employee.objects.filter(termination_date=None).filter(entry_date__range=(start, end))
            else:
                transferred_employee_ids = TransferEmployee.objects.values_list('employee_id', flat=True).distinct()
                employees = Employee.objects.filter(id__in=transferred_employee_ids)\
                    .filter(entry_date__range=(start, end))

    context = {'employees': employees,
               'form': form}
    return render(request, 'employees/list_employees.html', context)


def detail_employee(request, employee_id):
    employee = Employee.objects.filter(pk=employee_id).first()
    current_date = datetime.date.today()
    time_in_company = current_date - employee.entry_date
    years = (str(time_in_company/365)[:2]).replace(':', '')

    context = {'employee': employee,
               'time_in_company': years}

    return render(request, 'employees/detail_employee.html', context)


def transfer_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        form = TransferEmployeeForm(request.POST)
        if form.is_valid():
            to_unit = form.cleaned_data.get('to_unit')
            TransferEmployee.objects.create(employee=employee, from_unit=employee.unit, to_unit=to_unit)
            employee.unit = to_unit
            employee.save()
            return redirect(reverse('employee_detail', kwargs={'employee_id': employee_id}))
    else:
        form = TransferEmployeeForm()
    return render(request, 'employees/transfer_employee.html', {'form': form, 'employee': employee})


def fire_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if not employee.termination_date:
        employee.termination_date = datetime.date.today()
    else:
        employee.termination_date = None
    employee.save()
    return redirect(reverse('employee_detail', kwargs={'employee_id': employee_id}))


class EmployeeCreateView(CreateView):
    template_name = 'employees/employee_create.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('list_employees')


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employees/edit_employee.html'
    form_class = EditEmployeeForm
    success_url = reverse_lazy('list_employees')
