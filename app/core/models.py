from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="nome")
    slug = models.SlugField(max_length=255, verbose_name="slug")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "categoria"
        verbose_name_plural = "categorias"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="nome")
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="categoria",
    )
    photo = models.ImageField(upload_to="products", verbose_name="foto")
    active = models.BooleanField(default=True, verbose_name="ativo")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "produto"
        verbose_name_plural = "produtos"


class Background(models.Model):
    photo = models.ImageField(upload_to="backgrounds", verbose_name="foto")
    active = models.BooleanField(default=False, verbose_name="ativo")

    class Meta:
        db_table = "background"
        verbose_name = "background"
        verbose_name_plural = "backgrounds"
