from django.urls import path
from . import views

app_name = 'shopapp'
urlpatterns = [
    path('', views.list_products, name='product_list'),
    path('<slug:category_slug>/', views.list_products, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
