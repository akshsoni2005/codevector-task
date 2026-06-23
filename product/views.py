from django.shortcuts import render
from django.core.paginator import Paginator

from rest_framework.generics import ListAPIView

from .models import Product
from .serializers import ProductSerializer
from .pagination import ProductCursorPagination


class ProductListView(ListAPIView):

    serializer_class = ProductSerializer
    pagination_class = ProductCursorPagination

    def get_queryset(self):

        queryset = Product.objects.all().order_by("-id")

        category = self.request.query_params.get("category")

        if category:
            queryset = queryset.filter(category=category)

        return queryset


def product_ui(request):

    category = request.GET.get("category")

    products = Product.objects.all().order_by("-id")

    if category:
        products = products.filter(category=category)

    paginator = Paginator(products, 50)

    page_number = request.GET.get("page")

    products = paginator.get_page(page_number)

    return render(
        request,
        "products/product_list.html",
        {"products": products}
    )