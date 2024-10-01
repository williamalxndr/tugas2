import datetime
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required(login_url="/login")
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        "nama": request.user.username,
        "npm": "2306226914",
        "kelas": "PBP E",
        "product_entries": product_entries,
        "last_login": request.COOKIES["last_login"]
    }

    return render(request, "main.html", context)

def create_new_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect("main:show_main")
    
    context = {"form": form}
    return render(request, "create_new_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/xml")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response

def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:show_main"))

def edit_product(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("main:show_main"))
    
    context = {"form": form}
    return render(request, "edit_product.html", context)

def show_product(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        "category": "all",
        "product_entries": product_entries,
    }

    return render(request, "show_product.html", context)
 
def show_product_by_category(request, category):
    product_entries = Product.objects.filter(user=request.user)

    if category == "all":
        return HttpResponseRedirect(reverse("main:show_product"))
    
    product_entries = product_entries.filter(category=category)

    context = {
        "category": category,
        "product_entries": product_entries,
    }

    return render(request, "show_product.html", context)