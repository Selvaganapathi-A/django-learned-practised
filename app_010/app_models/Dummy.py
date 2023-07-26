from django.db import models

import decimal


class DummyModelM2M(models.Model):
    m2mfield = models.CharField(max_length=10)
    pass


class DummyModelFK(models.Model):
    fkfield = models.CharField(max_length=10)
    pass


class DummyModelO2O(models.Model):
    o2ofield = models.CharField(max_length=10)
    pass


class country_choices(models.Choices):
    literate = "india"
    morans = "america"
    timid = "russia"
    mental = "syria"
    ghost = "england"


class DummyModel(models.Model):
    # CharField
    char_field = models.CharField(
        max_length=100, choices=country_choices.choices
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
    foreign_key = models.ForeignKey(DummyModelFK, on_delete=models.CASCADE)
    # ManyToManyField
    many_to_many = models.ManyToManyField(DummyModelM2M)
    # OneToOneField
    one_to_one = models.OneToOneField(DummyModelO2O, on_delete=models.CASCADE)
    # AutoField
    auto_field = models.AutoField(primary_key=True)
