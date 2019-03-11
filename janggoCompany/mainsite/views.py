from django.shortcuts import render, redirect
from django.utils import translation, timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from product.models import Product, Product_type
from .forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# This is main site 'index.html' view
def main(request):
    userLanguage = 'en'
    products = Product.objects.all().order_by('product_detail_type__product_type')
    
    print("**********")
    print(products)
    site="main"
    if translation.LANGUAGE_SESSION_KEY in request.session:
        userLanguage = request.session[translation.LANGUAGE_SESSION_KEY]
    
    context = {'site':site, 'products':products}
    translation.activate(userLanguage)
    return render(request, 'index.html', context)

def transEn(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    userLanguage = 'en'
    request.session[translation.LANGUAGE_SESSION_KEY] = userLanguage
    return redirect(reverse('home'))

def transKo(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    userLanguage = 'ko'
    request.session[translation.LANGUAGE_SESSION_KEY] = userLanguage
    return redirect(reverse('home'))

# file upload for Product
def model_form_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    
    products = Product.objects.all()
    context = {'form': form, 'products': products}
    print("**********")
    print(products)
    return render(request, 'mainsite/product_upload.html', context)


