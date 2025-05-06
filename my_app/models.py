from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskModel(models.Model):
    task_name=models.CharField(max_length=100)
    created_date=models.DateField(auto_now_add=True) #auto_now_add>> for date of added day
    due_date=models.DateField()
    description=models.TextField(null=True,blank=True)
    category=[('work','work'),
              ('personal','personal'),
              ('urgent','urgent')]
    task_category=models.CharField(max_length=100,choices=category)
    compleated_status=models.BooleanField(default=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE) #its one to many

    def __str__(self):
        return self.task_name
    
class OtpModel(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    otp=models.CharField(max_length=100)
    created_date=models.DateField(auto_now_add=True)