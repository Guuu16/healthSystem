from django.shortcuts import render


def employee_login_view(request):
    return render(request, 'employee_login.html')


def hr_login_view(request):
    return render(request, 'hr_login.html')

def coach_login_view(request):
    return render(request, 'coach_login.html')