from django.db import models
from pytils.translit import slugify


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название меню"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Mеню"
        verbose_name_plural = "Список меню"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        related_name="items",
        on_delete=models.CASCADE,
        verbose_name="Меню"
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
        verbose_name="Родительский пункт",
    )
    title = models.CharField(max_length=100, verbose_name="Название пункта")
    url = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="URL (явный)"
    )
    named_url = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name="Named URL (name из urls.py)",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.named_url:
            max_named_url_length = self._meta.get_field("named_url").max_length
            self.named_url = slugify(self.title)[:max_named_url_length]
        super().save(*args, **kwargs)
