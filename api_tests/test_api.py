from utils.validators import validate_json

def test_health_check(api_client):
    """Проверка на 'ШОКовость' на главной"""
    response = api_client.health_check()
    assert response.status_code == 200, "Сервис недоступен"

def test_user_login(api_client, registered_user):
    """Залогин юзером"""
    response = api_client.login_user(registered_user["email"], registered_user["password"])
    assert response.status_code == 200, "Не удалось авторизоваться"
    
    data = response.json()
    validate_json(data, "authResponse")  # Валидация по схеме authResponse

def test_update_user_name(api_client, auth_token):
    """Изменение имени юзера"""
    new_name = "NewTestName"
    response = api_client.update_user_name(auth_token, new_name)
    assert response.status_code == 200, "Не удалось обновить имя"
    
    data = response.json()
    validate_json(data, "authResponse")  # Валидация обновленного пользователя
    assert data["user"]["name"] == new_name, "Имя не обновилось"

def test_update_user_name_invalid_length(api_client, auth_token):
    """Негативный тест: недопустимая длина имени"""
    invalid_names = ["", "a" * 51]  # Пустое имя и превышение длины
    for name in invalid_names:
        response = api_client.update_user_name(auth_token, name)
        assert response.status_code == 422, f"Ожидается ошибка валидации для имени '{name}'"
        data = response.json()
        validate_json(data, "errorResponse")  # Валидация ошибки