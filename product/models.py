from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=225)
    category = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["category"]),
            models.Index(fields=["-id"]),
        ]

    def __str__(self):
        return self.name