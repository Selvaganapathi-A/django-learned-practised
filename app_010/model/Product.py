from django.db import models
from django.urls import reverse_lazy

import decimal

from .Category import CategoryModel
from .Tag import TagModel


class ProductModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Product Name")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=decimal.Decimal(0)
    )
    is_available = models.BooleanField(default=True)
    # indicate when object creeated
    created_at = models.DateTimeField(auto_now_add=True)
    # indicate when last time this object modified
    updated_at = models.DateTimeField(auto_now=True)
    discount_start_date = models.DateField(null=True, blank=True)
    discount_end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(
        upload_to="product_images/", null=True, blank=True
    )
    category = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(TagModel)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("app03:product-read", kwargs={"pk": self.pk})
