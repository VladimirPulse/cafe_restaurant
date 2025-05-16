from http import HTTPStatus

from menu_app.models import Item, Menu
from menu_app.pytest_tests.constans import URL_ITEM_ADD, URL_MENU_ADD


def test_creat_menu_admin(admin_client, form_data, form_data_2, form_data_3):
    '''Проверка на создание меню и его пунктов админом'''
    # Убедимся, что в БД пуста
    assert Item.objects.count() == 0
    assert Menu.objects.count() == 0
    # Попробуем добавить меню
    response = admin_client.post(URL_MENU_ADD, data=form_data)
    assert response.status_code == HTTPStatus.FOUND
    assert Menu.objects.count() == 1
    # проверим, что добавилось меню с заданными параметрами
    new_menu = Menu.objects.get()
    assert new_menu.title == form_data['title']
    assert new_menu.slug == form_data['slug']
    # Попробуем добавить подменю
    response_1 = admin_client.post(URL_ITEM_ADD, data=form_data_2)
    assert response_1.status_code == HTTPStatus.FOUND
    assert Item.objects.count() == 1
    new_item_1 = Item.objects.get()
    assert new_item_1.title == form_data_2['title']
    assert new_item_1.slug == form_data_2['slug']
    assert new_item_1.menu.id == form_data_2['menu']
    # Попробуем добавить пункт подменю
    response_2 = admin_client.post(URL_ITEM_ADD, data=form_data_3)
    assert response_2.status_code == HTTPStatus.FOUND
    assert Item.objects.count() == 2
    # Извлечем именно созданный пункт и проверим,
    # что он с заданными параметрами
    new_item_2 = Item.objects.exclude(id=new_item_1.id).get()
    assert new_item_2.title == form_data_3['title']
    assert new_item_2.slug == form_data_3['slug']
    assert new_item_2.parent.id == form_data_3['parent']
    assert new_item_2.menu.id == form_data_3['menu']


def test_creat_menu(authenticated_client, form_data, form_data_2):
    '''Проверка, что только админ может создавать меню и его пункты'''
    # Убедимся, что в БД пуста
    assert Item.objects.count() == 0
    assert Menu.objects.count() == 0
    # Попробуем добавить меню
    authenticated_client.post(URL_MENU_ADD, data=form_data)
    assert Menu.objects.count() == 0
    # Попробуем добавить подменю
    authenticated_client.post(URL_ITEM_ADD, data=form_data_2)
    assert Item.objects.count() == 0
