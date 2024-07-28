from django.forms import ModelForm

from.models import Unit, Employee


class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = ('code',
                  'organization_name',
                  'acronym',
                  'is_active',
                  'liquidation_date')


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
                  'entry_date',
                  'termination_date')
