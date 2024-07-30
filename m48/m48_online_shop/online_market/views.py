
from django.shortcuts import render
from .models import Product
from online_market.models import Category, Product
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'online_market/home.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
        comments = product.comments.all()
        categories = Category.objects.all()
        return render(request, 'products/product_detail.html', {
            'product': product,
            'comments': comments,
            'categories': categories
        })


def categories(request):
    category_list = Category.objects.all()
    context = {
        'categories': category_list
    }
    return render(request, 'online_market/home.html', context)

