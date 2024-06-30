from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login as login_process
from django.contrib.auth.decorators import login_required
from . import views

@login_required(login_url='/login/')
def home(request):
    context = {}    

    return render(
        request,
        'index.html',
        context        
    )


def login(request):
    state = 0
    message = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

       

        if user is not None:
            login_process(request, user)
            state = 1
            message = ""
            opType = "Log In"
            opDetail = "Login Successfull"
            return redirect('/home/')
        else:
            state = 2
            opType = "Log In"
            opDetail = "Login Failed, Username or password is incorrect - " + username + " -"

            

            message = "Username or password is incorrect"
    dic = {'state': state, 'message': message}
    return render(request, 'login.html', dic)

def prueba(request):
    status = 0

    return render(request, 'authentication/prueba.html')