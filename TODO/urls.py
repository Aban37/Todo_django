"""
URL configuration for TODO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='home'),
    path('registration/',UserRegistrationView.as_view(),name='registration'),
    path('login/',LoginView.as_view(),name='login'),  #name='login' >> look at view.py top (redirect) if 'registration/' get succes we want to go to 'login/' 
    path('logout/',LogoutView.as_view(),name='logout'),
    path('task/create/',AddTask.as_view(),name='create'),
    path('task/read/',TaskRead.as_view(), name='read'),
    path('task/update/<int:pk>',TaskUpadate.as_view(),name='taskupdate'),
    path('task/delete/<int:pk>',Taskdelete.as_view()),
    path('read/specific/<int:pk>',SpecificDetails.as_view()),
    path('forgotpassword/',ForgotPassView.as_view(),name='forgotpassword'),
    path('verifyotp/',VerifyOtpview.as_view(),name='verifypassword'),
    path('resetpassword/',ResetPassView.as_view(),name='reset'),
    path('filtertask/',TaskFilterView.as_view(),name='filter')
]

