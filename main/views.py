from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
# --- tugas 4 ---
# import for register
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# import for login dan logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# ----------- tugas 2 ----------- 
# function untuk show app main
@login_required(login_url='main:login') # rugas 4: Restriksi halaman main
def show_main(request):
    products = Product.objects.all()
    context = {
        'products' : products,
        'total_amount' : sum(product.amount for product in products)
    }
    return render(request, "main/main.html", context)

# ----------- tugas 3 ----------- 
# function untuk create product dan data delivery
def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, 'main/create_product.html', context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# ----------- tugas 4 -----------
# function untuk register
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'main/register.html', context)
# function untuk login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'main/login.html', context)
# function untuk logout
def logout_user(request):
    logout(request)
    return redirect('main:login')