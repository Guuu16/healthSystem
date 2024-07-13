from django.shortcuts import render


# Create your views here.
def FillHealthDataView(request):
    return render(request, 'FillHealthData.html')

# Create your views here.
def UpdateHealthView(request):
    return render(request, 'UpadateHealthData.html')

def view_health_Data(request):
    return render(request, 'view_health_data.html')
