# from django.core.management.base import BaseCommand
# from product.models import Product
# import random

# class Command(BaseCommand):

#     def handle(self, *args, **kwargs):
#         print("Seed command running...")

# categories = [
#     "Electronics",
#     "Books",
#     "Fashion",
#     "Sports",
#     "Gaming"
# ]


# products = []

# for i in range(100):

#     Product.objects.bulk_create(products)

#     print("Products created")

from django.core.management.base import BaseCommand
from product.models import Product
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        categories = [
            "Electronics",
            "Books",
            "Fashion",
            "Sports",
            "Gaming"
        ]

        TOTAL_PRODUCTS = 200000
        BATCH_SIZE = 5000

        for start in range(0, TOTAL_PRODUCTS, BATCH_SIZE):

            products = []

            for i in range(start, start + BATCH_SIZE):

                products.append(
                    Product(
                        name=f"Product {i}",
                        category=random.choice(categories),
                        price=random.randint(100, 10000)
                    )
                )

            Product.objects.bulk_create(products)

            print(f"Created {start + BATCH_SIZE} products")

        print("200000 Products Created Successfully!")