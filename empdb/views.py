from django.shortcuts import render, redirect
from empdb.models import Employees
# from .forms import EmployeeForm

def insert_emp(request):
    if request.method == "POST":
        # print("yessssssssssssss")
        EmployeeID = request.POST['EmployeeID']
        EmployeeName = request.POST['EmployeeName']
        Department = request.POST['Department']
        DateOfJoining = request.POST['DateOfJoining']
        PhotoFileName = request.POST['PhotoFileName']
        data = Employees(EmployeeID=EmployeeID, EmployeeName=EmployeeName, Department=Department, DateOfJoining=DateOfJoining, PhotoFileName= PhotoFileName)
        data.save()
  
        return redirect('show/')
    else:
        return render(request, 'insert.html')
def show_emp(request):
    employees = Employees.objects.all().values()

    print("employees",employees)
    print("type",type(employees))
    return render(request,'show.html',{'employees':employees})

def edit_emp(request,pk):
    print("pk",pk)
    employee = Employees.objects.get(EmployeeID=pk)
    print("aaaara hai ")
    if request.method == 'POST':
        return redirect('/show'/pk)

    context = {
        'employees': employee,
    }

    return render(request,'edit.html',context)
def remove_emp(request, pk):
    print('pk',pk)
    employee = Employees.objects.get(EmployeeID=pk)
    
    if request.method == 'POST':
        if employee:
            employee.delete()
        else:
            print("not exist")
    context = {
        'employees': employee,
    }

    print("Hello")

    return render(request, 'delete.html', context)