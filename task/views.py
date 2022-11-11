from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import View
from task.models import Task
from task.forms import RegistrationForm,LoginForm


# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")        

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"register.html")  

class AddTaskView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addtask.html")  

    def post(self,request,*args,**kwargs):
        user=request.POST.get("user")
        task=request.POST.get("task")
        Task.objects.create(task_name=Task,
        user=user)
        return render(request,"addtask.html")

class TaskListView(View):
    def get(self,request,*args,**kwargs):
        qs=Task.objects.all()
        return render(request,"tasklist.html",{"todos":qs})    


class TaskDetailView(View):
    def get(self,request,*arg,**kwargs):
        id=kwargs.get("id")
        task=Task.objects.get(id=id) 
        return render(request,"taskdetail.html",{"todos":task})      

class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Task.objects.filter(id=id).delete()
        return redirect("todo-all") 


#user
#from django.contrib.auth
# model AbstractBaseuser.Abstractuser.user          

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registers.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("todo-all")
        else:
            return render(request,"registers.html",{"form":form})   

class LoginView(View):

    def get(self,request,*args,**kw):
        form=LoginForm()
        return render(request,"logins.html",{"form":form})                 


    


