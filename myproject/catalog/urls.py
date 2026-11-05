from django.urls import path
from . import views

# urlpatterns = [
#     path('show_data/', views.show_data, name='show_data'),
#     path('submit_data/', views.submit_data, name='submit_data'),
#     path('item/<int:item_id>/', views.show_item, name='show_item'),
# ]

app_name = 'catalog'

urlpatterns = [
     path('', views.home, name='home'),
     path('contacts/', views.contact, name='contact'),
     path('example/', views.example_view, name='example'),
     path('index/', views.index, name='index'),
     path('products/<int:pk>/', views.product_detail, name='product_detail'),
     path('product_list/', views.product_list, name='product_list')
]