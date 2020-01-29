import datetime
from Accounts.decorators import manager_required
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from Accounts.models import User
from .forms import Facility_form
from .models import Facility
from django.http import HttpResponse, HttpResponseRedirect
from Member_Console.models import Auditorium

# Create your views here.


@login_required(login_url='/')
@manager_required(login_url='/Accounts/goback')
def user_view(request):
    userobj = User.objects.all().filter(is_member=True)
    return render(request, 'Manager_Console/user.html', {'userobj': userobj})


@login_required(login_url='/')
@manager_required(login_url='/Accounts/goback')
def add_facility(request):
    if request.method == 'POST':
        form = Facility_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Manager:delf')
    else:
        form = Facility_form()
        return render(request, 'Manager_Console/add_facility.html', {'forms': form})


@login_required(login_url='/')
@manager_required(login_url='/Accounts/goback')
def del_facility(request):
    args = Facility.objects.all()
    return render(request, 'Manager_Console/del_facility.html', {'args': args})


def remove_Facility(request, slug):
    Facility.objects.get(name=slug).delete()
    return redirect('Manager:delf')


@login_required(login_url='/')
@manager_required(login_url='/Accounts/goback')
def audi(request):
    now = datetime.datetime.now()
    Auditorium.objects.filter(Q(booking_date__lt=now.date())).delete()
    userobj = User.objects.all().filter(is_member=True)
    audiobj = Auditorium.objects.all()
    return render(request, 'Manager_Console/audi.html', {'userobj': userobj, 'audiobj': audiobj})
