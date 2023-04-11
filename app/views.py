from django.shortcuts import render

# Create your views here.
from app.models import *
def display_dept(request):
    dop=dept.objects.all()
    d={'department':dop}
    return render(request,'dept.html',d)
from app.models import *
def display_emp(request):
    eop=emp.objects.all()
    eop=emp.objects.filter(hiredate__year=1980)
    eop=emp.objects.all()
    eop=emp.objects.filter(hiredate__month=4)
    eop=emp.objects.all()
    eop=emp.objects.filter(hiredate__day=22)
    eop=emp.objects.all()
    eop=emp.objects.filter(Ename__startswith='j')
    eop=emp.objects.filter(job__endswith='r')
    eop=emp.objects.filter(Ename__in=('Smith','Martin'))
    eop=emp.objects.filter(empno__contains=6)
    eop=emp.objects.all()
    emp.objects.filter(job='clerk').update(sal='1600')
    eop=emp.objects.all()
    emp.objects.update_or_create(job='MANAGER',defaults={'Ename':'gana'})
    eop=emp.objects.all()
    emp.objects.filter(job='MANAGER').delete()
    eop=emp.objects.all()


    
    d={'employee':eop}
    return render(request,'emp.html',d)