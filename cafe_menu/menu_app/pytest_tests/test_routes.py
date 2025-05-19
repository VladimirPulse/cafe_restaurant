from http import HTTPStatus

import pytest
from pytest_django.asserts import assertRedirects

from menu_app.models import Menu, MenuItem
from menu_app.pytest_tests.constans import REDIRECT_ADMIN, URL_ADMIN, URL_HOME


def test_users_access_to_the_urls(admin_client, client):
    """Проверка на доступ пользователя к url"""
    response = client.get(URL_ADMIN)
    assertRedirects(response, REDIRECT_ADMIN)
    response = admin_client.get(URL_ADMIN)
    assert response.status_code == HTTPStatus.OK
    response = client.get(URL_HOME)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_url_slug(client, create_model):
    """Проверка на доступ пользователя по named_url"""
    assert MenuItem.objects.count() == 1
    assert Menu.objects.count() == 1
    slug = create_model.named_url
    response = client.get(URL_HOME + f"{slug}/")
    assert response.status_code == HTTPStatus.OK
