import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
    def health_check(self):
        """Проверка состояния сервиса"""
        return self.session.get(f"{self.base_url}/health")
    
    def register_user(self, email, password, age=None):
        """Регистрация нового пользователя"""
        payload = {"email": email, "password": password}
        if age is not None:
            payload["age"] = age
        return self.session.post(f"{self.base_url}/auth/register", json=payload)
    
    def login_user(self, email, password):
        """Авторизация пользователя"""
        return self.session.post(f"{self.base_url}/auth/login", json={"email": email, "password": password})
    
    def get_current_user(self, token):
        """Получение данных текущего пользователя"""
        headers = {"Authorization": f"Bearer {token}"}
        return self.session.get(f"{self.base_url}/user/me", headers=headers)
    
    def update_user_name(self, token, new_name):
        """Обновление имени пользователя"""
        headers = {"Authorization": f"Bearer {token}"}
        return self.session.patch(f"{self.base_url}/user/name", 
                                 json={"name": new_name}, 
                                 headers=headers)