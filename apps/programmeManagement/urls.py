from django.urls import path
from . import views

urlpatterns = [
    # 其他URL配置...
    path('register_entertainment_program/', views.register_entertainment_program,
         name='register_entertainment_program'),
    path('register_health_program/', views.register_health_program,
         name='register_health_program'),
    path('check_in_program/', views.check_in_program,
             name='check_in_program'),
    path('modify_program_info/', views.modify_project,
         name='modify_program_info'),
    path('view_programmes/', views.view_programmes,
         name='view_programmes'),
    path('update_programme/', views.update_programme,
         name='update_programme'),
    path('add_programme/', views.add_programme,
         name='add_programme'),
    path('coach_view_programme/', views.coach_view_programme,
         name='coach_view_programme'),
    # path('submit_entertainment_program/', views.submit_entertainment_program, name='submit_entertainment_program'),
]
