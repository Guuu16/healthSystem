from django.urls import path
from .views import hr_dashboard, add_employee, update_employee, delete_employee

urlpatterns = [
    path('add_employee/', add_employee, name='add_employee'),
    path('update_employee/', update_employee, name='update_employee'),
    path('delete_employee/', delete_employee, name='delete_employee'),
]