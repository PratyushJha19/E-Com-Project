from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404

def store(request):
    all_products = Product.objects.all()
    context = {'all_products':all_products}
    return render(request, 'store/store.html', context=context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories':all_categories}

def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product':product}
    return render(request, 'store/product_info.html', context=context)

def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = { 'category':category, 'products':products, }
    return render(request, 'store/list_category.html', context=context)