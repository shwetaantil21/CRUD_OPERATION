from django.shortcuts import render, redirect
# from django.shortcuts import HttpResponse
from .models import *
# Create your views here.

# Read DATA


def index(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp
    }
    return render(request, 'index.html', context)

# Add DATA


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        emp = Employees(
            name=name,
            email=email,
            city=city,
            phone=phone
        )
        # Save data
        emp.save()
        return redirect('index')

    return render(request, 'index.html')


def Edit(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp
    }
    return redirect(request, 'index.html', context)


def Update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        emp = Employees(
            id=id,
            name=name,
            email=email,
            city=city,
            phone=phone
        )
        emp.save()
        return redirect('index')
    return redirect(request, 'index.html')


def Delete(request, id):
    emp = Employees.objects.get(id=id)
    emp.delete()
    return redirect('index')
