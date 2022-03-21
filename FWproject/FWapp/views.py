from django.shortcuts import render, get_object_or_404
from .models import Category, Products
from django. core . paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.


def procat(request,catslug=None):
    cat = None
    pro_list = None
    if catslug!= None:
        cat = get_object_or_404(Category, slug=catslug)
        pro_list = Products.objects.all().filter(category=cat, available=True)
    else:
        pro_list = Products.objects.all().filter(available=True)
    pagin=Paginator(pro_list,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=pagin.page(page)
    except(EmptyPage,InvalidPage):
        pro = pagin.page(pagin.num_pages)

    return render(request, "category.html", {'category': cat, 'products': pro})


def prodeta(request, catslug, proslug):
    try:
        product = Products.objects.get(category__slug=catslug, slug=proslug)
    except Exception as b:
        raise b
    return render(request, 'product.html', {'product': product})


