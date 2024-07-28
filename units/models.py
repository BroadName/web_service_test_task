from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


def validate_code_field(value: str):
    if len(value) != 4 or not value.isdigit():
        raise ValidationError(_('Код подразделения должен состоять из 4 цифр.'), params={'value': value},)


GENDER_SELECTION = (
    ('Мужской', 'Мужской'),
    ('Женский', 'Женский')
)


class Unit(models.Model):
    code = models.CharField(max_length=4, validators=[validate_code_field], verbose_name='Код подразделения')
    organization_name = models.CharField(max_length=255, verbose_name='Полное наименование')
    acronym = models.CharField(max_length=20, verbose_name='Аббревиатура')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True)
    liquidation_date = models.DateTimeField(blank=True, verbose_name='Дата ликвидации')

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name_plural = 'Подразделения'
        verbose_name = 'Подразделение'


class Employee(models.Model):
    service_number = models.CharField(max_length=30, unique=True, verbose_name='Табельный номер')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    gender = models.CharField(choices=GENDER_SELECTION, verbose_name='Пол')
    date_of_birthday = models.DateField(verbose_name='Дата рождения')
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name='employees', verbose_name='Подразделение')
    position = models.CharField(max_length=255, verbose_name='Должность')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email', unique=True)
    photo = models.ImageField(upload_to='photos/', default='default_man.png', verbose_name='Фотография')
    entry_date = models.DateField(verbose_name='Дата приёма/перевода-прибытия')
    termination_date = models.DateField(blank=True, null=True, verbose_name='Дата увольнения/перевода-выбытия')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Работники'
        verbose_name = 'Работник'
