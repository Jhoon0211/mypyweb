from django.shortcuts import render, get_object_or_404, redirect
from cart.cart import Cart
from cart.forms import AddProductForm
from shop.models import Product


def detail(request):
    cart = Cart(request)   # 장바구니 객체 생성

    for product in cart:
        product['quantity_form'] = AddProductForm(
            initial={'quantity': product['quantity'],
                     'id_update': True}
        )
    context = {'cart': cart}
    return render(request, 'cart/detail.html', context)

# 장바구니에 제품 추가
def add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddProductForm(request.POST) # 입력된 수량
    if form.is_valid():
        cd = form.cleaned_data   # 유효성 검사가 끝난 데이터
        cart.add(product=product, quantity=cd['quantity'],
                 is_update=cd['is_update'])
    return redirect('cart:detail')

def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product)
    cart.remove(product)
    return redirect('cart:detail')