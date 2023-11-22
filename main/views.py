import json
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
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
# cookies
import datetime
# --- tugas 6 ---
from django.views.decorators.csrf import csrf_exempt

# ----------- tugas 2 ----------- 
# function untuk show app main
@login_required(login_url='main:login') # rugas 4: Restriksi halaman main
def show_main(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'products' : products,
        'total_amount' : sum(product.amount for product in products),
        'total_product' : products.count,
        # kirim cookies
        'last_login' : request.COOKIES['last_login'],
        # tugas 4: kirim user
        'name' : request.user.username,
    }
    return render(request, "main/main.html", context)

# ----------- tugas 3 ----------- 
# function untuk create product dan data delivery
def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == 'POST':
        # Tugas 4: set user
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {
        'form': form,
        # kirim cookies
        'last_login' : request.COOKIES['last_login'],
        # tugas 4: kirim user
        'name' : request.user.username,
    }
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
            # set cookies
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'main/login.html', context)
# function untuk logout
def logout_user(request):
    logout(request)
    # hapus cookies
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
# function untuk increase or decrease amount sebanyak 1
def update_amount(request, product_id, action):
    product = Product.objects.get(pk = product_id)
    if action == 'increase':
        product.amount += 1
    elif action == 'decrease':
        if (product.amount > 1):
            product.amount -= 1
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))
# function untuk delete product
def delete_product(request, product_id):
    if request.GET.get('confirm') == 'true':
        product = Product.objects.get(pk = product_id)
        product.delete()
        messages.success(request, 'Your product has been successfully deleted!')
    return HttpResponseRedirect(reverse('main:show_main'))
# function untuk edit product
def edit_product(request, product_id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = product_id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'form': form,
        # kirim cookies
        'last_login' : request.COOKIES['last_login'],
        # tugas 4: kirim user
        'name' : request.user.username,
    }
    return render(request, "main/edit_product.html", context)

# ----------- tugas 6 -----------
# fungsi get product json
def get_product_json(request):
    product = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product))
# fungsi add product ajax
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        user = request.user

        new_product = Product(name=name, price=price, description=description, amount=amount, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

# ----------- tugas 9 -----------
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"],
            amount = int(data["amount"])
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)