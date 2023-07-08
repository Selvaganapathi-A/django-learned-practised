from django.db import models
from django.urls import reverse_lazy

import decimal


class char_field_choices(models.Choices):
    literate = "india"
    morans = "america"
    timid = "russia"
    mental = "syria"
    ghost = "england"


class ExampleModel(models.Model):
    # CharField
    char_field = models.CharField(
        max_length=100, choices=char_field_choices.choices
    )
    # TextField
    text_field = models.TextField()
    # IntegerField
    integer_field = models.IntegerField()
    # FloatField
    float_field = models.FloatField()
    # DecimalField
    decimal_field = models.DecimalField(
        max_digits=5, decimal_places=2, default=decimal.Decimal(102.5)
    )
    # BooleanField
    boolean_field = models.BooleanField(default=False)
    # DateField
    date_field = models.DateField()
    # DateTimeField
    datetime_field = models.DateTimeField()
    # TimeField
    time_field = models.TimeField()
    # EmailField
    email_field = models.EmailField()
    # URLField
    url_field = models.URLField()
    # FileField
    file_field = models.FileField(upload_to="files/")
    # ImageField
    image_field = models.ImageField(upload_to="images/")
    # ForeignKey
    foreign_key = models.ForeignKey("AnotherModel", on_delete=models.CASCADE)
    # ManyToManyField
    many_to_many = models.ManyToManyField("YetAnotherModel")
    # OneToOneField
    one_to_one = models.OneToOneField("OneToOneModel", on_delete=models.CASCADE)
    # AutoField
    auto_field = models.AutoField(primary_key=True)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Product Name")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=decimal.Decimal(0)
    )
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # indicate when object creeated
    updated_at = models.DateTimeField(
        auto_now=True
    )  # indicate when last time this object modified
    discount_start_date = models.DateField(null=True, blank=True)
    discount_end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(
        upload_to="product_images/", null=True, blank=True
    )
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("app03:product-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("app03:category-detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("app03:tag-detail", kwargs={"pk": self.pk})
