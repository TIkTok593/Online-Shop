from django.urls import path
from . import views

app_name = 'shopapp'
urlpatterns = [
    path('', views.ListProductsView.as_view(), name='product_list'),
    path('<slug:category_slug>/', views.ListProductsView.as_view(), name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
