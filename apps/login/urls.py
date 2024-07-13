from django.urls import path
from .views import employee_login_view, hr_login_view,coach_login_view

urlpatterns = [
    path('employee_login/', employee_login_view, name='employee_login'),
    path('hr_login/', hr_login_view, name='hr_login'),
    path('coach_login/', coach_login_view, name='coach_login'),
]
