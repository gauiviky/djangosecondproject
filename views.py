from django.shortcuts import render
#from django.http import HttpResponse
from secondapp.models import Employee
from . import forms
from django.views.generic import TemplateView


# Create your views here.
def d(request):
    obj=Employee.objects.all()
    return render(request,"secondapp/data.html",{'html':obj})
def e(request):
    jegan=forms.student()
    if request.method=='POST':
        jegan=forms.student(request.POST)
        if jegan.is_valid():    
            return render(request,"secondapp/input.html",{'Form':jegan})
    return render(request,"secondapp/input.html",{'Form':jegan})
def f(request):
    Employee=forms.Emp_data()
    if request.method=='POST':
        Employee=forms.Emp_data(request.POST)
        if Employee.is_valid():
            Employee.save()
            return d(request)
    return render(request,"secondapp/well.html",{'silence':Employee})
def g(request,pk):
    Data=Employee.objects.get(Emp_id=pk)
    d1=forms.Emp_data(instance=Data)
    if request.method=='POST':
        d1=forms.Emp_data(request.POST,instance=Data)
        if d1.is_valid():
            d1.save()
            return d(request)
    return render(request,"secondapp/d3.html",{'data':d1})
def h(request,pk):
    Data=Employee.objects.get(Emp_id=pk)
    if request.method=='POST':
        Data.delete()
        return d(request)
    return render(request,"secondapp/delete.html",{'Key':Data})   
    
class logic(TemplateView):
    template_name="secondapp/input.html"
    def get_context_data(self, **kwargs):
        a= super().get_context_data(**kwargs)
        a['Key']="hello"
        return a


