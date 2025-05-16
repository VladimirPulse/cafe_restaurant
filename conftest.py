import pytest


@pytest.fixture
def form_data():
    return {
        'title': 'Новое меню',
        'slug': 'new-slug'
    } 

@pytest.fixture
def form_data_2():
    return {
        "title": "Винная карта",
        "slug": "wine",
        "menu": 1
    }

@pytest.fixture
def form_data_3():
    return {
        "title": "Красное вино",
        "parent": 1,
        "slug": "wine_red",
        "menu": 1
    }


@pytest.fixture
def authenticated_client(client, django_user_model):
    user = django_user_model.objects.create(username='user')
    client.force_login(user)
    return client
