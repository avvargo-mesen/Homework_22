from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category, Product

# Create your views here.

# def example_view(request):
#     return render(request, 'app/example.html')
#
# def show_data(request):
#     if request.method == 'GET':
#         return render(request,'app/show_data.html')
#
# def submit_data(request):
#     request.GET
#     request.POST
#     if request.method == 'POST':
#         return HttpResponse("Данные отправлены")
#
# def show_item(request, item_id):
#     return render(request,'app/item.html', {'item_id':item_id})

def home(request):
    return render(request,'catalog/home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, 'catalog/contacts.html') # чтобы не упало в ошибку - возвращается рендер шаблона.

def example_view(request):
    return render(request, 'catalog/example.html')

def index(request):
    category = Category.objects.get(id=1)
    context ={
        'category_name': category.name,
        'category_description': category.description,
    }
    return render(request, 'catalog/index.html', context=context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context ={
        'product': product
}
    return render(request, 'catalog/product_detail.html', context=context)

def product_list(request):
    product = Product.objects.all()
    context = {
        "products" : product,
    }
    return render(request, 'catalog/product_list.html', context=context)