import pytest

from menu_app.models import Menu, MenuItem


@pytest.fixture
def authenticated_client(client, django_user_model):
    user = django_user_model.objects.create(username="user")
    client.force_login(user)
    return client


@pytest.fixture
def form_data():
    return {
        "name": "Новое меню",
    }


@pytest.fixture
def form_data_2():
    return {"title": "Винная карта", "named_url": "wine", "menu": 1}


@pytest.fixture
def form_data_3():
    return {
        "title": "Красное вино",
        "parent": 1,
        "named_url":
        "wine_red",
        "menu": 1
    }


@pytest.fixture
def create_model(form_data, form_data_3):
    model_menu = Menu.objects.create(name=form_data["name"])
    model_menuitem = MenuItem.objects.create(
        menu=model_menu,
        title=form_data_3["title"],
        named_url=form_data_3["named_url"],
    )
    return model_menuitem
