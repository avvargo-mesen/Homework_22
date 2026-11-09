from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
     # path('', views.HomeView.as_view(), name='home'),
     # path('contacts/', views.ContactView.as_view(), name='contact'),
     # path('example/', views.ExampleView.as_view(), name='example'),
     # path('index/<int:pk>/', views.IndexView.as_view(), name='index'),
     # path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
     path('', views.BlogListView.as_view(), name='blog_list'),
     path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
     path('create/', views.BlogCreateView.as_view(), name='blog_create'),
     path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='blog_update'),
     path('confirm_delete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog_delete'),
]