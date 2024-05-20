from django.db import models


class Prediction(models.Model):
    """
    Модель предсказания.
    """

    text = models.TextField(default="Предсказания", verbose_name="Текст предсказания")
    data_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.text[:25]}"

    class Meta:
        verbose_name = 'Предсказание'
        verbose_name_plural = 'Предсказания'
        ordering = ('-data_create', 'text',)
