from django.shortcuts import render
from book.models import Cart, CartItem
# Create your views here.

def cart(request):
    session_id = request.session.get('cart_id')
    cart = Cart.objects.get(session_id=session_id)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/cart.html', {'cart_items': cart_items})
