from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    purchase_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'наименование'
        verbose_name_plural = 'наименования'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']
