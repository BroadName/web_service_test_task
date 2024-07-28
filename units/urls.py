from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import list_units, detail_unit, UnitCreateView, list_employees, detail_employee, EmployeeCreateView

urlpatterns = [
    path('add_unit/', UnitCreateView.as_view(), name='add_unit'),
    path('units/<int:unit_id>/', detail_unit, name='unit_detail'),
    path('units/', list_units, name='list_units'),
    path('add_employee/', EmployeeCreateView.as_view(), name='add_employee'),
    path('employees/<int:employee_id>/', detail_employee, name='employee_detail'),
    path('employees/', list_employees, name='list_employees'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)