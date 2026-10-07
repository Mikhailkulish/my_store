from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Статья", help_text="Введите название статьи"
    )
    description = models.TextField()
    preview_image = models.ImageField(
        upload_to="blog/photo",
        verbose_name="Превью",
        help_text="Превью статьи для блога",
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата публикации статьи",
        help_text="Укажите дату публикации статьи",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        editable=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]
        permissions = [
            ('can_manage_blog', 'Can manage blog'),
        ]
