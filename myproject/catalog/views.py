from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Category, Product, MyModel

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

# Тема CBV
# class MyModelCreateView(CreateView):
#     model = MyModel
#     fields = ['name', 'description']
#     template_name = 'catalog/mymodel_form.html'
#     success_url = reverse_lazy('catalog:mymodel_list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         response = super().form_invalid(form)
#         response.context_data['error_message'] = "Please correct the errors"
#
#         return response
#
# class MyModelListView(ListView):
#     model = MyModel
#     template_name = 'catalog/mymodel_list.html'
#     context_object_name = 'mymodels'
#
#     def get_queryset(self):
#         return MyModel.jbjects.filter(is_active=True)
#
#
# class MyModelDetailView(DetailView):
#     model = MyModel
#     template_name = 'catalog/mymodel_detail.html'
#     context_object_name = 'mymodel'
#
#     def get_additional_data(self):
#         return "Это дополнительная информация"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['additional_data'] = self.get_additional_data
#
#         return context
#
#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset)
#         if not obj.is_active:
#             raise Http404("Object not found")
#         return obj
#
# class MyModelUpdateView(UpdateView):
#     model = MyModel
#     fields = ['name', 'description']
#     template_name = 'catalog/mymodel_form.html'
#     success_url = reverse_lazy('catalog:mymodel_list')
#
# class MyModelDeleteView(DeleteView):
#     model = MyModel
#     template_name = 'catalog/mymodel_confirm_delete.html'
#     success_url = reverse_lazy('catalog:mymodel_list')

class HomeView(TemplateView):
    template_name = 'catalog/home.html'

# def home(request):
#     return render(request,'catalog/home.html')

class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'


# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         message = request.POST.get("message")
#
#         return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
#     return render(request, 'catalog/contacts.html') # чтобы не упало в ошибку - возвращается рендер шаблона.

def example_view(request):
    return render(request, 'catalog/example.html')

def index(request):
    category = Category.objects.get(id=1)
    context ={
        'category_name': category.name,
        'category_description': category.description,
    }
    return render(request, 'catalog/index.html', context=context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# def product_detail(request, pk):
#     product = Product.objects.get(id=pk)
#     context ={
#         'product': product
# }
#     return render(request, 'catalog/product_detail.html', context=context)

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

# def product_list(request):
#     product = Product.objects.all()
#     context = {
#         "products" : product,
#     }
#     return render(request, 'catalog/product_list.html', context=context)