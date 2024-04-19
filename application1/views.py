from django.shortcuts import render,HttpResponse
from .models import Employees

# Create your views here.
def about_us(request):
    return render(request,'about_us.html')
def contact_us(request):
    return render(request,'contact_us.html')
def all_emp(request):
    emps= Employees.objects.all()
    context={
     'emps':emps
    }
    return render(request,'all_emp.html',context)
def add_emp(request):
    if request.method=='POST':
        employee_id=int(request.POST['employee_id'])
        first_name=request.POST['first_name']
        second_name=request.POST['second_name']
        phone_num=int(request.POST['phone_num'])
        email=request.POST['email']
        salary=int(request.POST['salary'])
        design=request.POST['design']
        new_emp=Employees(employee_id=employee_id,first_name=first_name,second_name=second_name,phone_num=phone_num,email=email,salary=salary,design=design)
        new_emp.save()
        return render(request,'add_emp.html')
    elif request.method=="GET":
     return render(request,'add_emp.html')
    else:
        return HttpResponse("Error Occured Sorry")
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            removeable_emp= Employees.objects.get(employee_id=emp_id)
            removeable_emp.delete()
        except:
            return render(request,'remove_emp.html',context)
    emps= Employees.objects.all()
    context={
     'emps':emps
    }
    return render(request,'remove_emp.html',context)
def filter_emp(request):
    if request.method=='POST':
        employee_id=int(request.POST['employee_id'])
        emps=Employees.objects.all()
        if employee_id:
            emps=emps.filter(employee_id=employee_id)
        context={
            'emps':emps
        }
        return render(request,'view_emp.html',context)
    elif request.method=='GET':
     return render(request,'filter_emp.html')
    else:
        return HttpResponse("Error Occured Sorry")