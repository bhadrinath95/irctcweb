# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, UserRegisterForm, BookingForm, CreateNewList
from django.contrib.auth.decorators import login_required
from .models import Booking, Person, get_irctcpay_strings, get_multiplepay_strings, get_netbanking_strings, get_debitbanking_strings, get_walletsbanking_strings, get_podbanking_strings, get_gatewaybanking_strings
from django.contrib import messages
from automation import irctcautomation
from django.contrib.auth.models import User
from django.http import HttpResponse
import json

# Create your views here.
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        try:
            user = authenticate(username= username,password=password)
            login(request, user)
            return redirect("/")
        except:
            return render(request, "unauthenticate.html", {})
            
    return render(request, "login.html", {"form":form,"title":title})

def index(request):
    irctcpay_strings = get_irctcpay_strings()
    multiplepay_strings = get_multiplepay_strings()
    debitbanking_strings = get_debitbanking_strings()
    netbanking_strings = get_netbanking_strings()
    walletsbanking_strings = get_walletsbanking_strings()
    podbanking_strings = get_podbanking_strings()
    gatewaybanking_strings = get_gatewaybanking_strings()
    
    json_irctcpay_strings = json.dumps(irctcpay_strings)
    json_multiplepay_strings = json.dumps(multiplepay_strings)
    json_debitbanking_strings = json.dumps(debitbanking_strings)
    json_netbanking_strings = json.dumps(netbanking_strings)
    json_walletsbanking_strings = json.dumps(walletsbanking_strings)
    json_podbanking_strings = json.dumps(podbanking_strings)
    json_gatewaybanking_strings = json.dumps(gatewaybanking_strings)
    
    title = "Travel Details"
    form = BookingForm(request.POST or None)
    if request.user.is_authenticated and request.user.is_active:
        request.session.modified = True
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Successfully created")
            return redirect("/create/%s" %(instance.id))
        
        context = {
            "form": form,
            "title":title,
            "json_irctcpay_strings": json_irctcpay_strings,
            "json_multiplepay_strings": json_multiplepay_strings,
            "json_debitbanking_strings": json_debitbanking_strings,
            "json_netbanking_strings": json_netbanking_strings,
            "json_walletsbanking_strings": json_walletsbanking_strings,
            "json_podbanking_strings": json_podbanking_strings,
            "json_gatewaybanking_strings": json_gatewaybanking_strings,
            }
        return render(request, "travel.html", context)  
    return render(request, "unauthenticate.html", {})

def create(request,id):
    booking = Booking.objects.get(id=id)
    if request.user.is_authenticated and request.user.is_active and request.user == booking.user:
        request.session.modified = True
        title = 'Passenger Details'
        form = CreateNewList(request.POST or None)
        person = booking.person_set.all()
        print(person)
        print(booking.destination)
        print()
        if request.user.is_authenticated:
            if request.POST.get("newItem") and form.is_valid():
                try:
                    instance = form.save(commit = False)
                    instance.booking = booking
                    instance.save()
                    messages.success(request, "Successfully created")
                except:
                    pass
            elif request.POST.get("selRun"):
                status = irctcautomation.irctc(booking, person)
                return render(request, "completed.html", {"status": status,})
            elif request.POST.get("resetItem"):
                booking.person_set.all().delete()
            elif request.POST.get("back"):
                return redirect("/")
            elif request.POST.get("EditItem"):
                editperson = Person.objects.get(id= request.POST.get("EditItem", ""))
                Person.objects.get(id= request.POST.get("EditItem", "")).delete()
                form = CreateNewList(instance = editperson)
            elif request.POST.get("DropItem"):
                Person.objects.get(id= request.POST.get("DropItem", "")).delete()
                 
        return render(request, "passenger.html", {"title":title, "form":form, "person":person})
    else:
        return render(request, "unauthenticate.html", {})

def register_view(request):
    title = "Register"
    if request.user.is_authenticated and request.user.is_superuser and request.user.is_active:
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect("/")
        context = {
            "form": form,
            "title":title,
            }
        return render(request, "register.html", context)
    else:
        return render(request, "unauthenticate.html", {})

def logout_view(request):
    logout(request)
    return redirect("/")