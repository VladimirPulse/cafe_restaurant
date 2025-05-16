# from django.contrib import admin
# from .models import MenuItem

# class MenuItemInline(admin.TabularInline):
#     model = MenuItem
#     extra = 1

# # @admin.register(Menu)
# # class MenuAdmin(admin.ModelAdmin):
# #     inlines = [MenuItemInline]

# @admin.register(MenuItem)
# class MenuItemAdmin(admin.ModelAdmin):
#     inlines = [MenuItemInline]
#     list_display = ('title', 'url', 'parent')


from django.contrib import admin

from menu_app.models import Item, Menu


@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('menu',)
    fieldsets = (
        ('Add new item', {
            'description': "Родительским элементом должно быть меню или элемент",
            'fields': (('menu', 'parent'), 'title', 'slug')
            }),
            )


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')