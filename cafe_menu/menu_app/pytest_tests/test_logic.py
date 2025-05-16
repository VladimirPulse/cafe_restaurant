from menu_app.models import Item, Menu
from menu_app.pytest_tests.constans import URL_ITEM_ADD, URL_MENU_ADD


def test_creat_tree_menu(admin_client, form_data, form_data_2, form_data_3):
    '''Проверка на наличие древовидной иерархии'''
    # Убедимся, что в БД пуста
    assert Item.objects.count() == 0
    assert Menu.objects.count() == 0
    url = URL_MENU_ADD
    admin_client.post(url, data=form_data)
    assert Menu.objects.count() == 1
    new_menu = Menu.objects.get()
    # Попробуем добавить подменю
    admin_client.post(URL_ITEM_ADD, data=form_data_2)
    assert Item.objects.count() == 1
    new_item_1 = Item.objects.get()
    assert new_menu.items.get().id == new_item_1.id
    # Попробуем добавить пункт подменю
    admin_client.post(URL_ITEM_ADD, data=form_data_3)
    assert Item.objects.count() == 2
    # Извлечем именно созданный пункт и проверим,
    # что это именно он
    new_item_2 = Item.objects.exclude(id=new_item_1.id).get()
    assert new_item_1.childrens.get().id == new_item_2.id
