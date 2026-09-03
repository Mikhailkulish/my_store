from django.db import models


class Product(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Товар", help_text="Введите наименование товара"
    )
    description = models.TextField()
    photo = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Фото товара",
        help_text="Загрузите фото товара",
    )
    category = models.ForeignKey(
        on_delete=models.SET_NULL,
        help_text="Введите категорию товара",
        blank=True,
        null=True,
        related_name="products",
    )
    purchase_price = models.IntegerField()
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата создания товара",
        help_text="Укажите дату создания товара",
    )
    updated_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата изменения товара",
        help_text="Укажите дату изменения товара",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["category", "title"]


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
