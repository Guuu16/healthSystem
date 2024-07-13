from django.urls import path
from .views import *
from apps.healthManagement.views import FillHealthDataView

urlpatterns = [
    path('view_report/', view_report, name='view_report'),
    path('hr_view_report/', hr_view_report, name='hr_view_report'),
    path('coach_view_report/', coach_view_report, name='coach_view_report')

]
