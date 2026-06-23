from django.urls import path
from .views import ProductListView, product_ui

urlpatterns = [
    path("", product_ui, name="product-ui"),
    path("products/", ProductListView.as_view()),
]


