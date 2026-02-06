from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def shop_home(request):
    categories = Category.objects.all()
    return render(
        request,
          'categories.html',
        {
            'categories': categories
        })

def category_list(request):
    categories = Category.objects.all()
    return render(
        request,
          'categories.html', 
        {
            'categories': categories
        })


def product_list(request):
    products = Product.objects.select_related('category')
    return render(
        request,
          'products.html',
        {
            'products': products
        })


def category_products(request,id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)

    return render(
        request,
          'category_products.html', 
        {
            'category': category,
            'products': products,
        })
