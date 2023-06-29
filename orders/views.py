from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print('*************************')
        print('*********request.POST*********')
        print(request.POST)
        print('&&&&&&&&&&&&&&&&&&&&&&&&&')
        print('*************************')
        print('*********request.form*********')
        print(form)
        print('&&&&&&&&&&&&&&&&&&&&&&&&&')
        if form.is_valid():
            order = form.save()
            print('*************************')
            print('*********After form.save()*********')
            print(order)
            print('&&&&&&&&&&&&&&&&&&&&&&&&&')
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            order_created.delay(order.id)
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
        print('*************************')
        print('*********empty form*********')
        print(form)
        print('&&&&&&&&&&&&&&&&&&&&&&&&&')
    
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart,
                   'form': form})
