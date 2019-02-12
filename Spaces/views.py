from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from Spaces.models import Category, Page
from Spaces.forms import CategoryForm, PageForm

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list}

    return render(request, 'Spaces/index.html', context_dict)

def pricing(request):
    return render(request, 'Spaces/pricing.html')

def howitworks(request):
    return render(request, 'Spaces/howitworks.html')

def carts(request):
    return render(request, 'cart/home.html')

def contact(request):
    return render(request, 'Spaces/contact.html')

def pre_signup(request):
    return render(request, 'Spaces/pre_signup.html')

def space(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list}

    return render(request, 'Spaces/space.html', context=context_dict)

def show_category(request, category_name_slug):

    context_dict = {}

    try:

        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'Spaces/category.html', context_dict)

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():

            category = form.save(commit=True)
            print(category, category.slug)

            return index(request)
        else:

            print(form.errors)

    return render(request, 'Spaces/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = Pageform()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
            else:
                print(form.errors)

        context_dict = {'form':form, 'category': category}
        return render(request, 'Spaces/add_page.html', context_dict)

    return render(request, 'Spaces/add_category.html', {'form': form})
