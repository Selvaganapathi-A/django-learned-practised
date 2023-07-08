from django.db import models

"""
https://docs.djangoproject.com/en/4.2/ref/models/fields/
"""


class KoiModel(models.Model):
    # * - Auto Field
    # field_001 = models.AutoField()
    # field_005 = models.BigAutoField()
    field_077 = models.SmallAutoField(primary_key=True, editable=False)
    # * - Integer Field
    # ? widget = NumberInput
    field_006 = models.BigIntegerField()
    field_044 = models.IntegerField()
    field_063 = models.PositiveBigIntegerField()
    field_064 = models.PositiveIntegerField()
    field_065 = models.PositiveSmallIntegerField()
    field_078 = models.SmallIntegerField()
    field_034 = models.FloatField()

    # * - BinaryField
    field_007 = models.BinaryField()

    # * - BooleanField
    # ? widget = CheckboxInput
    field_008 = models.BooleanField()

    # * - Single line text
    # ? widget = TextInput
    field_011 = models.CharField(max_length=100)

    #  * Date and Datetime
    # ? widget = DateInput
    # ! default = `datetime.date.today`
    # ! auto_now_add = updated when instace is created
    # ! auto_now = updated every time instace is saved
    field_018 = models.DateField()

    # ? widget = DateTimeInput
    # ! default = `django.utils.timezone.now`
    field_019 = models.DateTimeField()

    # * Decimal
    # ? widget = 'NumberInput' when localize is False or 'TextInput' otherwise.
    field_020 = models.DecimalField(decimal_places=9, max_digits=30)

    # ! periods of time - modeled in Python by `timedelta`.
    field_022 = models.DurationField()
    field_023 = models.EmailField()
    field_030 = models.Field()
    field_031 = models.FileField()
    field_032 = models.FilePathField()

    # ? widget = 'TextInput'
    field_039 = models.GenericIPAddressField()

    # ? ClearableFileInput.
    field_041 = models.ImageField()

    field_045 = models.JSONField()
    field_076 = models.SlugField()

    # ? widget = 'TextArea'
    field_083 = models.TextField()

    # ? widget = 'TimeInput'
    field_084 = models.TimeField()

    # ? widget = 'UrlInput'
    field_086 = models.URLField()
    field_087 = models.UUIDField()

    # Relationship Fields

    # field_048 = models.ManyToManyField()
    # field_055 = models.NullBooleanField()
    # field_057 = models.OneToOneField()


# print("# -", flush=True)

# for i, field in enumerate(sorted(vars(models))):
#     if field.endswith("Field"):
#         print(f" field_{i:>03d} =  models.{field}()")

# print("# -")
