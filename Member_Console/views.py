from django.shortcuts import render, redirect
from .forms import Updateform
from .forms import Audi_form
from datetime import timedelta, date
from Manager_Console.models import Facility
from .models import FacilityChosen, Auditorium, Membership
from Accounts.models import User
from django.db.models import Q
from Accounts.decorators import member_required
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def mem_details(request):
    return render(request, 'Member_Console/mem_details.html')


@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def joinF(request):
    facilities = Facility.objects.all() #return the facilties provided by the club no matter what
    user = User(request.user)
    user = user.id
    li = []
    if FacilityChosen.objects.filter(user=user.id).exists(): #To check if Facility chosen instance is existing with user
        fc = FacilityChosen.objects.get(user=user)     #to get the data of the facilties chosen that particular user
        jf = Membership.objects.all().filter(choice=fc).values('facility')

        for i in [*jf]:
            li.append(i['facility'])
        print(li)#list of joined facilties
    print(facilities)
    return render(request, 'Member_Console/joinF.html', {'facilities': facilities, 'jf': li})


@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def join(request, slugid, slugdays):
    user = User(request.user)
    if FacilityChosen.objects.filter(user=user.id).exists():
        end = date.today() + timedelta(days=slugdays)
        fc = FacilityChosen.objects.get(user=user.id)
        facil = Facility.objects.get(id=slugid)
        print("hi")
        m = Membership.objects.create(facility=facil, choice=fc, start_date=date.today(), end_date=end)
        print(m)
    else:
        a = FacilityChosen.objects.create(user=user.id)
        end = date.today() + timedelta(days=slugdays)
        Membership(choice=a, facility=slugid, start_date=date.today(), end_date=end)
    return redirect('Member:joinF')


@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def removeF(request):
    facilities = Facility.objects.all()
    user = User(request.user)
    user = user.id
    li = []
    if FacilityChosen.objects.filter(user=user.id).exists():  # To check if Facility chosen instance is existing with user
        fc = FacilityChosen.objects.get(user=user)
        jf = Membership.objects.all().filter(choice=fc).values('facility') #facility name user na

        for i in [*jf]:
            li.append(i['facility'])
        print(li)
    else:
        fc = FacilityChosen.objects.create(user=user)
        jf = Membership.objects.all().filter(choice=fc).values('facility')
        for i in [*jf]:
            li.append(i['facility'])
        print(li)
    return render(request, 'Member_Console/removeF.html', {'facilities': facilities, 'li': li,
                                                           'jstart': date.today(),
                                                           'jend': Membership.objects.all().filter(choice=fc).values('end_date')})


@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def remove(request, slug):
    user = User(request.user)
    fc = FacilityChosen.objects.get(user=user.id)
    facil = Facility.objects.get(id=slug)
    Membership.objects.all().filter(facility=facil, choice=fc).delete()
    return redirect('Member:removeF')


@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def audi(request):
    args = Auditorium.objects.filter(user=request.user)
    return render(request, 'Member_Console/audi.html', {'args': args})


@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def audi_booking(request):
    if request.method == "POST":
        form = Audi_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('Member:audi_booking')
    else:
        now = date.today()
        args = Auditorium.objects.filter(Q(booking_date=now) | Q(booking_date__gt=now))
        form = Audi_form()
        return render(request, 'Member_Console/audi_booking.html', {'form': form, 'args': args})


@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def remove_audi(request, slug):
    Auditorium.objects.get(id=slug).delete()
    return redirect('Member:audi')


@login_required(login_url='/')
@member_required(login_url='/Accounts/goback')
def user_update(request):
    if request.method == 'POST':
        form = Updateform(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('Member:Mdetails')
        else:
            return render(request, 'Member_Console/edit.html', {'form': form})
    else:
        form = Updateform(instance=request.user)
        return render(request, 'Member_Console/edit.html', {'form': form})
