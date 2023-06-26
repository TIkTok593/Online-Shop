from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shopapp.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    print(request)
    cart = Cart(request)
    print(cart.cart)
    product = get_object_or_404(Product, id=product_id)
    print(product)
    form = CartAddProductForm(request.POST)
    print(request.POST)
    print(form)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    print(f'******************'
          f'\ncart_detail_method\n'
          f'cart: {cart.cart} \n'
          f'******************')
    print('Printing items in cart_detail')
    print(f'******************')
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
        print(item)
    print(f'******************')
    return render(request, 'cart/detail.html', {'cart': cart})
