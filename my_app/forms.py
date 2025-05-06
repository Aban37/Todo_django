from django import forms
from my_app.models import User,TaskModel


class UserRegistartionForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={"username":forms.TextInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter ur Name"}),
                 "password":forms.PasswordInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter ur password"}),
                 "email":forms.TextInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Enter ur email"})}

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control w-50 mx-auto " ,"placeholder":"Enter ur Name"}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control w-50 mx-auto mt-3","placeholder":"password"}))

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        exclude=['created_date','compleated_status','user_id']#(exclude>> the item we dont want ) 0r
        #fields=[' the wanted items']
        widgets={'task_name':forms.TextInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Task name"}),
                'due_date':forms.DateInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Task name"}),
                'description':forms.Textarea(attrs={"class":"form-control w-50 mx-auto","placeholder":"Task name"}),
                'category':forms.ChoiceField(attrs={"class":"form-control w-50 mx-auto","placeholder":"Task name"}),
                'task_category':forms.TextInput(attrs={"class":"form-control w-50 mx-auto","placeholder":"Task name"})}

class ForgotPassForm(forms.Form):
    email=forms.CharField(max_length=100)
    

class VerifyotpForm(forms.Form):
    votp=forms.CharField(max_length=100)


class ResetPassForm(forms.Form):
    password=forms.CharField(max_length=100)
    cpassword=forms.CharField(max_length=100)

