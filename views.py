from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request,'Second_page.html')

def Complain(request):
	return render(request,'Complain_Form.html')

def Cse(request):
    return render(request,'CSE_Faculy.html')

def Me(request):
    return render(request,'ME_Faculty.html')

def Ec(request):
    return render(request,'EC_Faculty.html')

def Ce(request):
    return render(request,'CE_Faculty.html')

def Pharma(request):
    return render(request,'PHARMA_Faculty.html')

def Mba(request):
    return render(request,'MBA_Faculty.html')

def Bs(request):
    return render(request,'BS_Faculty.html')



# def Login(request):
#     form = LoginForm()
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             form = LoginForm(request.POST)
#             if form.is_valid():
#                 uname = form.cleaned_data['username']
#                 upass = form.cleaned_data['password']
#                 user = authenticate(username=uname, password=upass)
#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, 'Logged in Successfully !!')
#                     return HttpResponseRedirect('')
         
#         return render(request,'try.html' ,{'form': form})
#     else:
#         return HttpResponseRedirect('')
	
def Login(request):
    msg=''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully !!')
                msg='Logged in Successfully !!'
                return HttpResponseRedirect('/',{'msg':msg})
                        

    else:
        form = LoginForm()
        return render (request,'LoginPage.html',{'form':form})
        

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

