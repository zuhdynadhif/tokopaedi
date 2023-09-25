from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
# --- tugas 3: import untuk register ---
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# tugas 2: function untuk show app main
def show_main(request):
    products = Product.objects.all()
    context = {
        'products' : products,
        'total_amount' : sum(product.amount for product in products)
    }
    return render(request, "main/main.html", context)

# tugas 3: function untuk create product dan data delivery
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

# tugas 4: function untuk register
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