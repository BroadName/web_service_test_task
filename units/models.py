from django.core.exceptions import ValidationError
from django.utils import timezone
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
    liquidation_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата ликвидации')

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
    phone_number = models.CharField(max_length=20, unique=True, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email', unique=True)
    photo = models.ImageField(upload_to='photos/', default='default_man.png', verbose_name='Фотография')
    entry_date = models.DateField(default=timezone.now, verbose_name='Дата приёма')
    termination_date = models.DateField(blank=True, null=True, default=None, verbose_name='Дата увольнения')

    def save(self, *args, **kwargs):
        if self.photo == 'default_man.png':
            if self.gender == 'Женский':
                self.photo = 'default_woman.png'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Работники'
        verbose_name = 'Работник'
        ordering = ['-entry_date', 'full_name']


class TransferEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')
    from_unit = models.ForeignKey(Unit, related_name='transfer_from', on_delete=models.CASCADE, verbose_name='Подразделение выбытия')
    to_unit = models.ForeignKey(Unit, related_name='transfer_to', on_delete=models.CASCADE, verbose_name='Подразделение прибытия')
    transfer_date = models.DateField(auto_now_add=True, verbose_name='Дата перевода')
