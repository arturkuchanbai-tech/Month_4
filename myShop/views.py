from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Category, Product


class ShopHomeView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'


class CategoryListView(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category')
    
class CategoryProductsView(ListView):
    model = Product
    template_name = 'category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
