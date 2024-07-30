from django.forms import ModelForm
from django import forms

from.models import Unit, Employee


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ('code',
                  'organization_name',
                  'acronym')


class EditUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ('code',
                  'organization_name',
                  'acronym')


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('service_number',
                  'full_name',
                  'phone_number',
                  'gender',
                  'date_of_birthday',
                  'unit',
                  'position',
                  'email',
                  'photo',
                  'entry_date')


class EditEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('service_number',
                  'full_name',
                  'phone_number',
                  'gender',
                  'date_of_birthday',
                  'position',
                  'email',
                  'photo')


class TransferEmployeeForm(forms.Form):
    to_unit = forms.ModelChoiceField(queryset=Unit.objects.all(), label='Подразделение прибытия')


class SearchEmployeesForm(forms.Form):
    KIND = (
        ('entry_date', 'Действующие'),
        ('transfer_date', 'Переведённые'),
        ('termination_date', 'Уволенные')
    )
    kind_employee = forms.ChoiceField(choices=KIND, label='Статус сотрудников')
    start = forms.DateField(label='Начальная дата', widget=forms.DateInput(attrs={'type': 'date'}))
    end = forms.DateField(label='Конечная дата', widget=forms.DateInput(attrs={'type': 'date'}))
