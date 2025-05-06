from django.shortcuts import render,redirect
from django.views.generic import View
from my_app.forms import*
from my_app.models import*
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
import random
# Create your views here.
# ahmw nyus sbid gugc 


def is_user(fn):
    def wrapper(request,**kwargs):
        id=kwargs.get('pk')
        item=TaskModel.objects.get(id = id)
        if item.user_id==request.user:
            return fn(request,**kwargs)
        return redirect('login')
    return wrapper

# user registration

class IndexView(View):
    def get(self,request):
        return render(request,"index.html")

class UserRegistrationView(View):
    def get(self,request):
        form=UserRegistartionForm
        return render(request,"registration.html",{'form':form}) # 3rd object is context
    
    def post(self,request):
        form=UserRegistartionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')
            User.objects.create_user(username=username,password=password,email=email)
            #User.object.create_user( **form.cleaned_data)  (create_user >> is for encripting the password)  
        # form = UserRegistartionForm
        # return render(request,"registration.html",{'form':form})
        return redirect('login')

class LoginView(View):
    
    def get(self,request):
        form=LoginForm
        return render(request,"login.html",{'form':form})
    
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user_obj=authenticate(request,username=username,password=password)
            if user_obj:
                login(request,user_obj)
                return redirect('create')
                
                # return render(request,'index.html')
            else:
                form=LoginForm
                return render(request,'login.html',{'form':form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')


class AddTask(View):
    def get(self,request):
        form=TaskForm
        return render(request,"addtask.html",{'form':form})
    
    def post(self,request):
        form =TaskForm(request.POST)
        if form.is_valid():
            TaskModel.objects.create(user_id=request.user,**form.cleaned_data)
        form=TaskForm
        return render(request,"addtask.html",{'form':form})
    
    
@method_decorator(decorator=is_user,name='dispatch') 
class TaskRead(View):
    def get(self,request):
        items=TaskModel.objects.filter(user_id=request.user)
        return render(request,"read.html",{'items':items})
    

@method_decorator(decorator=is_user,name='dispatch')
class TaskUpadate(View):

    def get(self,request,**kwargs):
        id=kwargs.get('pk')
        item=TaskModel.objects.get(id=id)
        form=TaskForm(instance=item)
        return render(request,"update.html",{'form':form})
    
    def post(self,request,**kwargs):

        id=kwargs.get('pk')
        item= TaskModel.objects.get(id=id)
        form=TaskForm(request.POST,instance=item)
        if form.is_valid():
            form.save()

        form=TaskForm
        return render(request,'update.html',{'form':form})
@method_decorator(decorator=is_user,name='dispatch')  
class Taskdelete(View):
    def get(self,request,**kwargs):
        id= kwargs.get('pk')
        TaskModel.objects.get(id=id).delete()
        return redirect('read')

# to read a specific task
@method_decorator(decorator=is_user,name='dispatch') 
class SpecificDetails(View):
    def get(request,**kwargs):
        id=kwargs.get('pk')
        item=TaskModel.objects.get(id=id)
        return render(request,"details.html",{'item':item})
    
class ForgotPassView(View):

    def get(self,request):
        form=ForgotPassForm
        return render(request,"forgotpassform.html",{'form':form})
    
    def post(self,request):
        form=ForgotPassForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            user_is=User.objects.get(email=email)
            otp=random.randint(1000,9999)
            
            OtpModel.objects.create(userid=user_is,otp=otp)
            # ahmw nyus sbid gugc
            send_mail(subject='otp for password reset',  #smtp (send mail transfer protocol)
                      message=f" nanam undoda malare. inna ninte otp:{str(otp)}. ini melal avarthikaruthu",
                      from_email='jocker27330@gmail.com',recipient_list=[email])
            return redirect('verifypassword')
        
class VerifyOtpview(View):
    def get(self,request):
        form=VerifyotpForm
        return render(request,"verifyotp.html",{'form':form})
    
    def post(self,request):
        form=VerifyotpForm(request.POST)
        if form.is_valid():
            otp=form.cleaned_data.get('votp')
            item= OtpModel.objects.get(otp=otp)
            user_id=item.userid
            user=User.objects.get(id=user_id.id)
            username=user.username
            if item:
                request.session['user'] =username
                return redirect('reset')
            return render(request,"verifyotp.html",{'form':form})
            
class ResetPassView(View):
    def get(self,request):
        form=ResetPassForm
        return render(request,"cpass.html",{'form':form})
    
    def post(self,request):
        form=ResetPassForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            cpassword=form.cleaned_data.get('cpassword')
            if password==cpassword:
                username=request.session.get('user')
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                return redirect('login')
        return render(request,"cpass.html",{'form':form})
    
#filter view

class TaskFilterView(View):
    def get(self,request):
        category=request.GET('category')
        alltask=TaskModel.objects.filter(userid= request.user) #all task of login user
        task=alltask.filter(task_category=category)
        return render(request,"taskfilter.html",{'task':task})
 