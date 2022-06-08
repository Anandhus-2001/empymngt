from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from employee.forms import LoginForms
from employee.forms import RegForm,EmployeeForm
# Create your views here.

# function based views
# class based views

# def index(request):
#     return HttpResponse("<h1> hello world </h1>")
#
# def login(request):
#     print(",,,,,,,,,,,,,,,,,,,",request)
#     return render(request,"login.html")
#
# def registraion(request):
#     return render(request,"reg.html")
#

class LogineView(View):

    def get(self,request):
        form=LoginForms()
        return render(request,"login.html",{'form':form})
    def post(self,request):
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        return render(request,"login.html")

class RegistrationView(View):

    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{'form':form})
    def post(self,request):
        print(request.POST.get("fn_name"))
        print(request.POST.get("l_name"))
        print(request.POST.get("e_mail"))
        print(request.POST.get("pwd"))
        print(request.POST.get("u_name"))


        return render(request,"reg.html")


class EmployeeCreateView(View):
    form_class=EmployeeForm
    template_name="emp-add.html"

    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("id"))
            print(form.cleaned_data.get("employee_name"))
            print(form.cleaned_data.get("designation"))
            print(form.cleaned_data.get("salary"))
            print(form.cleaned_data.get("email"))
            print(form.cleaned_data.get("experience"))
            return render(request,self.template_name,{"form":form})
        else:
            return render(request,self.template_name,{"form":form})