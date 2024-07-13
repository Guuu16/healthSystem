from django.shortcuts import render


def register_entertainment_program(request):
    return render(request, 'register_entertainment.html')


def register_health_program(request):
    return render(request, 'register_health_management_program.html')


def check_in_program(request):
    return render(request, 'check_in_program.html')


def modify_project(request):
    return render(request, 'modify_project_info.html')


def view_programmes(request):
    return render(request, 'view_programmes.html')


def update_programme(request):
    return render(request, 'update_programme.html')


def add_programme(request):
    return render(request, 'add_programme.html')


def coach_view_programme(request):
    return render(request, 'coach_view_program.html')
