from django.shortcuts import render


# Create your views here.
def dashboard_view(request):
    return render(request, 'employee_dashboard.html')


def dashboardhr_view(request):
    return render(request, 'hr_dashboard.html')


def coach_dashboard(request):
    return render(request, 'coach_dashboard.html')
