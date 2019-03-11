from django.shortcuts import render
from .models import Product, Product_detail_type ,Product_type
# Create your views here.
def main(request):
    product_detail_types = Product_detail_type.objects.all()
    product_types = Product_type.objects.all()
    product = Product.objects.all
    context = {"product_detail_types": product_detail_types,
               "product_types": product_types, "product": product}
    return render(request, 'product/index.html', context)

def detail(request, pk):
    product_detail_types = Product_detail_type.objects.all()
    product_types = Product_type.objects.all()
    product = Product.objects.filter(product_detail_type__pk=pk)
    print("***********")
    context = {'product': product, "product_detail_types": product_detail_types,
               "product_types": product_types}
    return render(request, 'product/index.html', context)