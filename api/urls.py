from django.urls import path

from .views import AddProducts, CategoriesView

urlpatterns = [
    path('add/', AddProducts.as_view(), name="Add products"),
    path('cat/', CategoriesView.as_view(), name="Get all categories"),
]
