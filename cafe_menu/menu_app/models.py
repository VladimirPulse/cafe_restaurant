from django.db import models


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Уникальное название меню'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Список меню'
        ordering = ('name',)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Реализация древовидной вложенности меню
    """
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название подменю'
    )
    url = models.CharField(max_length=200, blank=True, verbose_name='Cсылка')
    named_url = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Именованная ссылка'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Список подменю'
        ordering = ('title',)

    def __str__(self):
        return self.title
