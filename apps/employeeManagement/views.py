from django.shortcuts import render, redirect
from django.contrib import messages


def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')


def add_employee(request):
    # if request.method == 'POST':
    #     # 处理添加员工的逻辑
    #     messages.success(request, 'Employee added successfully.')
    #     return redirect('hr_dashboard')
    return render(request, 'add_employee.html')


def update_employee(request):
    # if request.method == 'POST':
    #     # 处理更新员工信息的逻辑
    #     messages.success(request, 'Employee updated successfully.')
    #     return redirect('hr_dashboard')
    return render(request, 'update_employee.html')


def delete_employee(request):
    # if request.method == 'POST':
    #     # 处理删除员工的逻辑
    #     messages.success(request, 'Employee deleted successfully.')
    #     return redirect('hr_dashboard')
    return render(request, 'delete_employee.html')
