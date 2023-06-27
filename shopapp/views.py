from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category

from cart.forms import CartAddProductForm



class ListProductsView(generic.ListView):
    template_name = 'shopapp/product/list.html'
    queryset = Category.objects.all()
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        print('****************************************')
        print(context)
        print('****************************************')
        category = None
        products = Product.objects.filter(available=True)
        category_slug = kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category,
                                         slug=category_slug)
            products = products.filter(category=category)
        context['category'] = category
        context['products'] = products
        print(context)
        return context

    

# def list_products(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)  # this will return all the products
#     if category_slug:
#         category = get_object_or_404(Category,
#                                      slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'shopapp/product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})


class ProductDetailView(generic.FormView):
    template_name = 'shopapp/product/detail.html'
    form_class = CartAddProductForm
        
    def get_queryset(self):
        product = get_object_or_404(Product,
                                id=self.kwargs['id'],
                                slug=self.kwargs['slug'],
                                available=True)
        return product
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        product = self.get_queryset()
        context['cart_product_form'] = self.get_form()
        context['product'] = product
        return context


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request,
#                   'shopapp/product/detail.html',
#                   {'product': product,
#                    'cart_product_form': cart_product_form})
