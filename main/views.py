import datetime
import json
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from main.forms import ProductForm
from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        filter_type = request.GET.get("filter", "all")

        if filter_type == "all":
            products = Product.objects.all()
        else:
            products = Product.objects.filter(user=request.user)

        product_data = []
        for product in products:
            product_data.append({
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'thumbnail': product.thumbnail,
                'category': product.category,
                'category_display': product.get_category_display(),
                'is_featured': product.is_featured,
                'user_id': product.user.id if product.user else None,
            })

        return JsonResponse({'products': product_data})

    context = {
        'npm' : '2406413104',
        'name': 'Elliot Randy Panggabean',
        'class': 'PBP C',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST
        form = ProductForm(data)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            if request.content_type == 'application/json':
                return JsonResponse({
                    'success': True,
                    'product': {
                        'id': str(product.id),
                        'name': product.name,
                        'price': product.price,
                        'description': product.description,
                        'thumbnail': product.thumbnail,
                        'category': product.category,
                        'category_display': product.get_category_display(),
                        'is_featured': product.is_featured,
                        'user_id': product.user.id,
                    }
                })
            else:
                messages.success(request, 'Product created successfully!')
                return redirect('main:show_main')
        else:
            if request.content_type == 'application/json':
                return JsonResponse({'success': False, 'errors': form.errors})

    form = ProductForm()
    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    # product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def register(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST
        form = UserCreationForm(data)
        if form.is_valid():
            form.save()
            if request.content_type == 'application/json':
                return JsonResponse({'success': True, 'message': 'Account created successfully'})
            else:
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        else:
            if request.content_type == 'application/json':
                return JsonResponse({'success': False, 'errors': form.errors})

    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST
        form = AuthenticationForm(data=data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.content_type == 'application/json':
                response = JsonResponse({'success': True, 'message': 'Login successful'})
                response.set_cookie('last_login', str(timezone.now()))
                return response
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(timezone.now()))
                return response
        else:
            if request.content_type == 'application/json':
                return JsonResponse({'success': False, 'errors': form.errors})

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        logout(request)
        return JsonResponse({'success': True, 'message': 'Logout successful'})
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return HttpResponseForbidden("You do not have permission to edit this product.")
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST
        form = ProductForm(data, instance=product)
        if form.is_valid():
            product = form.save()
            if request.content_type == 'application/json':
                return JsonResponse({
                    'success': True,
                    'product': {
                        'id': str(product.id),
                        'name': product.name,
                        'price': product.price,
                        'description': product.description,
                        'thumbnail': product.thumbnail,
                        'category': product.category,
                        'category_display': product.get_category_display(),
                        'is_featured': product.is_featured,
                        'user_id': product.user.id,
                    }
                })
            else:
                return redirect('main:show_main')
        else:
            if request.content_type == 'application/json':
                return JsonResponse({'success': False, 'errors': form.errors})

    form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return HttpResponseForbidden("You do not have permission to delete this product.")
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        product.delete()
        return JsonResponse({'success': True})
    return HttpResponseRedirect(reverse('main:show_main'))