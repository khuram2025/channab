from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.productlist, name='product_list'),
    path('grid/', views.productgrid, name='product_grid'),
    path('add', views.uploadanimal, name='uploadanimal'),
    path('<slug:category_slug>/', views.home, name='product_list_category'),
    path('<int:id>', views.productdetail, name='product_detail'),
    path('', views.home, name='home'),
    path('list/', views.productlist, name='product_list'),
    path('grid/', views.productgrid, name='product_grid'),
    path('add', views.uploadanimal, name='uploadanimal'),
    path('<slug:category_slug>/', views.home, name='product_list_category'),
    path('<int:id>', views.productdetail, name='product_detail'),
]
