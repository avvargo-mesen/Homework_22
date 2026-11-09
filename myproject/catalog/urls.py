from django.urls import path
from . import views

# urlpatterns = [
#     path('show_data/', views.show_data, name='show_data'),
#     path('submit_data/', views.submit_data, name='submit_data'),
#     path('item/<int:item_id>/', views.show_item, name='show_item'),
# ]

app_name = 'catalog'

urlpatterns = [
     path('', views.HomeView.as_view(), name='home'),
     path('contacts/', views.ContactView.as_view(), name='contact'),
     path('example/', views.ExampleView.as_view(), name='example'),
     path('index/<int:pk>/', views.IndexView.as_view(), name='index'),
     path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
     path('product_list/', views.ProductListView.as_view(), name='product_list'),

     # path('mymodel/list/', views.MyModelListView.as_view(), name='mymodel_list'),
     # path('mymodel/detail/<int:pk>/', views.MyModelDetailView.as_view(), name='mymodel_detail'),
     # path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
     # path('mymodel/delete/<int:pk>/', views.MyModelDeleteView.as_view(), name='mymodel_delete'),
     # path('mymodel/update/<int:pk>/', views.MyModelUpdateView.as_view(), name='mymodel_update'),
]