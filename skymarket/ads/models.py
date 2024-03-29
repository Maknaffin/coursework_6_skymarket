from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}

class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара")
    description = models.TextField(verbose_name="Описание товара")
    image = models.ImageField(upload_to='media', **NULLABLE, verbose_name="Фото")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь",
                               **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "объявление"
        verbose_name_plural = "объявления"
        ordering = ["-created_at"]

class Comment(models.Model):
    text = models.TextField(verbose_name="Текст отзыва", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь",
                               **NULLABLE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
