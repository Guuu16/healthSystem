from django.urls import path
from .views import *
from apps.healthManagement.views import FillHealthDataView

urlpatterns = [
    path('employee/', dashboard_view, name='employee_dashboard'),
    path('hr/', dashboardhr_view, name='hr_dashboard'),
    path('coach/', coach_dashboard, name='coach_dashboard')
]
