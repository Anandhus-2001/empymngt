from django.shortcuts import render
from django.views.generic import View
from calculator.forms import OperationForm
# Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,"cal-home.html")
class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1+n2
            print(form.cleaned_data)
            return render(request, "add.html",{"add":result,"form":form})
        else:
            return render(request,"add.html",{"form":form})

class SubView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"sub.html",{"form":form})
    def post(self,request):
        # n1 =request.POST.get("num1")
        # n2 =request.POST.get("num2")
        # result = int(n1)-int(n2)
        form=OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"sub.html",{"form":form})
        n1=form.cleaned_data.get("num1")
        n2=form.cleaned_data.get("num2")
        result=n1-n2
        return render(request,"sub.html",{"sub":result,"form":form})

class MulView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"mul.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result= int(n1)*int(n2)
        # return render(request,"mul.html",{"mulres":result}
        form=OperationForm(request.POST)
        if not form.is_valid():
            return render(request,"mul.html",{"from":form})
        n1=form.cleaned_data.get("num1")
        n2=form.cleaned_data.get("num2")
        result=n1*n2
        return render(request,"mul.html",{"mulres":result,"form":form})


class DivView(View):
    def get(self, request):
        return render(request, "div.html")

    def post(self, request):
        n1 = request.POST.get("num1")
        n2 = request.POST.get("num2")
        result = int(n1)/int(n2)
        return render(request,"div.html",{"divres":result})
class ModView(View):
    def get(self, request):
        return render(request, "mod.html")

    def post(self, request):
        n1 = request.POST.get("num1")
        n2 = request.POST.get("num2")
        result = int(n1)%int(n2)
        return render(request,"mod.html",{"modres":result})
class FactView(View):
    def get(self, request):
        return render(request, "fact.html")

    def post(self, request):
        n1 = int(request.POST.get("num1"))
        result=1
        for i in range(1,n1+1):
            result=result*(i)
        return render(request,"fact.html",{"factres":result})


class ExpView(View):
    def get(self, request):
        return render(request, "exp.html")

    def post(self, request):
        n1 =request.POST.get("num1")
        result=int(n1)**2
        return render(request, "exp.html", {"expres": result})
class WordCountView(View):
    def get(self,request):
        return render(request,"wordcount.html")
    def post(self,request):
        word = request.POST.get("word")
        words = word.split(" ")
        wc = {}
        for w in words:
            if w not in wc:
                wc[w] = 1
            else:
                wc[w] +=1
        print(wc)
        return render(request, "wordcount.html",{"wordcounts":wc})

#class PrimeView(View):
 #   def get(self,request):
  #      return render(request,"primenumber.html")
  #  def post(self,request):
   #     n1=int(request.POST.get("num1"))
   #     n2=int(request.POST.get('num2'))
    #    prime=[]
    #    for i in range









