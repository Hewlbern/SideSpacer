from django.shortcuts import render, redirect

from product.models import Product
from .models import Cart
from product.views import ProductListView

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    queryset = Product.objects.all()
    context = {
        'object_list': queryset,
        "cart": cart_obj,
    }
    return render(request, "carts/home.html", context)

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("home")
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    request.session['cart_items'] = cart_obj.products.count()
    #return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")