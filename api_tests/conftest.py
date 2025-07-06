import pytest
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def base_url():
    return "URL"

@pytest.fixture(scope="session")
def api_client(base_url):
    return APIClient(base_url)

@pytest.fixture(scope="function")
def registered_user(api_client):
    """Фикстура для регистрации тестового пользователя"""
    email = "EMAIL"
    password = "PASSWORD"
    response = api_client.register_user(email, password)
    assert response.status_code == 200, "Пользователь не зарегистрирован"
    return {"email": email, "password": password}

@pytest.fixture(scope="function")
def auth_token(api_client, registered_user):
    """Фикстура для получения токена авторизации"""
    response = api_client.login_user(registered_user["email"], registered_user["password"])
    assert response.status_code == 200, "Не удалось авторизоваться"
    return response.json()["token"]