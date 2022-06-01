from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name='description',
        blank=True,
    )

    def __str__(self):
        return self.name or f"category with id - {self.pk}"


class Meta:
    verbose_name = 'category'
    verbose_name_plural = 'categories'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='category',
    )

    name = models.CharField(
        verbose_name='product name',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='product_images',
        blank=True,
        verbose_name='image',
    )

    short_desc = models.CharField(
        verbose_name='short description',
        max_length=128,

    )

    description = models.TextField(
        verbose_name='description',
        blank=True,
    )

    price = models.DecimalField(
        verbose_name="price",
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='quantity of products',
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name or f"product with id - {self.pk}"


class Meta:
    verbose_name = 'product'
    verbose_name_plural = 'products'