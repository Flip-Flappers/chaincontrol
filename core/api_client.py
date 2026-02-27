import requests

class APIClient:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url.rstrip("/")

    def send_command(self, command, user_id="user-001"):
        r = requests.post(
            f"{self.base_url}/control",
            json={"command": command, "user_id": user_id},
            timeout=20,
        )
        r.raise_for_status()
        return r.json()