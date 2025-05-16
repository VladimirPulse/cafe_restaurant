from http import HTTPStatus

from pytest_django.asserts import assertRedirects

from menu_app.pytest_tests.constans import REDIRECT_ADMIN, URL_ADMIN, URL_HOME


def test_users_access_to_the_urls(admin_client, client):
    '''Проверка на доступ пользователя к url'''
    response = client.get(URL_ADMIN)
    assertRedirects(response, REDIRECT_ADMIN)
    response = admin_client.get(URL_ADMIN)
    assert response.status_code == HTTPStatus.OK
    response = client.get(URL_HOME)
    assert response.status_code == HTTPStatus.OK
