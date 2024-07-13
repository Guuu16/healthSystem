from django.urls import path
from .views import *

urlpatterns = [
    path('fill_in_health_data/', FillHealthDataView, name='fill_in_health_data'),
    path('update_health_data/', UpdateHealthView, name='update_health_data'),
    path('view_health_data/', view_health_Data, name='view_health_Data'),
]
