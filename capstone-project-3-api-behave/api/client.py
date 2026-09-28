import requests

from config.settings import BASE_URL, TIMEOUT


class APIClient:
    def __init__(self):
        self.session = requests.Session()

    def verify_login(self, email, password):
        response = self.session.post(
            f"{BASE_URL}/api/verifyLogin",
            data={"email": email, "password": password},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        return response.json()

    def close(self):
        self.session.close()

    def create_user(self, details):
        response = self.session.post(
            f"{BASE_URL}/api/createAccount", data=details, timeout=TIMEOUT
        )
        response.raise_for_status()
        return response.json()

    def get_user(self, email):
        response = self.session.get(
            f"{BASE_URL}/api/getUserDetailByEmail",
            params={"email": email},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        return response.json()

    def update_user(self, details):
        response = self.session.put(
            f"{BASE_URL}/api/updateAccount", data=details, timeout=TIMEOUT
        )
        response.raise_for_status()
        return response.json()

    def delete_user(self, email, password):
        response = self.session.delete(
            f"{BASE_URL}/api/deleteAccount",
            data={"email": email, "password": password},
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        return response.json()