from django.contrib import admin

from menu_app.models import Menu, MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "menu", "parent")
    list_filter = ("menu", "parent")
    search_fields = ("title",)
    fieldsets = (
        (
            "Добавить новый элемент",
            {
                "description": "Родительским элементом "
                "должно быть меню или элемент",
                "fields": (("menu", "parent"), "title", "url", "named_url"),
            },
        ),
    )
    # Автоматическое заполнение поля URL
    prepopulated_fields = {"named_url": ("title",)}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
