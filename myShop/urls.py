from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopHomeView.as_view(), name='shop_home'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('categories_products/<int:category_id>/', views.CategoryProductsView.as_view(), name='category_products'),
]
