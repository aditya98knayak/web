from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def homepage(request):
    return render(request, 'initial.html')


def SignUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password2'])
            login(request, user)
            if user.is_member:
                return redirect('Member:Mdetails')
            elif user.is_manager:
                return redirect('Manager:user')
            else:
                return render(request, 'initial.html')
        else:
            print(form.errors)
            print(type(form.errors))
            return render(request, 'initial.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'Accounts/SignUp.html', {'form': form})


def Login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if user.is_member:
                return redirect('Member:Mdetails')
            elif user.is_manager:
                print('Manager')
                return redirect('Manager:user')
            else:
                return render(request, 'initial.html')
        else:
            return render(request, 'initial.html')
    else:
        form = AuthenticationForm()
        return render(request, 'initial.html', {'form': form})


def Logout_view(request):
    logout(request)
    return render(request, 'initial.html')


def goback(request):
    return render(request, 'Accounts/goback.html')
