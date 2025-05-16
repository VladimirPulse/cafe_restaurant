# from django.db import models

# class MenuItem(models.Model):
#     title = models.CharField(
#         max_length=255,
#         verbose_name='Название меню'
#     )
#     parent = models.ForeignKey(
#         'self',
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name='children',
#         verbose_name='Название меню'
#     )
#     url = models.CharField(
#         max_length=255,
#         verbose_name='Ссылка перехода по меню'
#     )  # URL для перехода по меню
#     menu_name = models.CharField(
#         max_length=100,
#         verbose_name='Меню для группировки'
#     )  # Для идентификации меню

#     class Meta:
#         verbose_name = 'Меню'
#         verbose_name_plural = 'Список меню'
#         ordering = ('title',)

#     def __str__(self):
#         return self.title

#     # def get_url(self):
#     #     return self.url or '#'


from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Menu title')
    slug = models.SlugField(max_length=255, verbose_name="Menu slug")

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Item title')
    slug = models.SlugField(max_length=255, verbose_name="Item slug")
    menu = models.ForeignKey(Menu, blank=True, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.title