from django.shortcuts import render


# Create your views here.
def view_report(request):
    return render(request, 'view_report.html')


def hr_view_report(request):
    return render(request, 'hr_view_reports.html')


def coach_view_report(request):
    return render(request, 'coach_view_reports.html')
