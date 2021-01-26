from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from .tasks import discounts


def home(request):
    if request.method == 'GET':
        forms = ProductForm()
        products = Product.objects.all()
        context = {'forms': forms, 'products': products}
        return render(request, 'discount/home.html', context)

    if request.method == 'POST':
        name = request.POST['name']
        old_price = int(request.POST['old_price'])
        new_price = int(request.POST['new_price'])
        data = {'name': name, 'old_price': old_price, 'new_price': new_price}
        forms = ProductForm(data)
        context = {'forms': forms}
        if forms.is_valid():
            forms.save()
            discounts.delay(old_price, new_price)
            return redirect('/')
        return render(request, 'discount/home.html', context)
