from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
from carts.models import Cart

# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

    return render(request, "products/list.html", context)

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not Found...")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance = qs.first()
        return instance

class ProductDetailView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance


def product_detail_view(request, pk):
    # instance = Product.objects.get(pk=pk)

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    #  qs = Product.objects.filter(id=pk)
    #  if qs.exists() and qs.count() == 1:
    #      instance = qs.first()
    #  else:
    #      raise Http404("Product doesn't exist")
    #  instance = get_object_or_404(Product, pk=pk)
    context = {
        'object_list': instance
    }

    return render(request, "products/detail.html", context)