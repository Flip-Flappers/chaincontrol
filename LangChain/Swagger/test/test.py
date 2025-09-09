import requests

BASE_URL = "http://localhost:8086"
import requests

BASE_URL = "http://localhost:8086"

def get_token():
    url = f"{BASE_URL}/openapi/v1/getToken"
    headers = {"Content-Type": "application/json"}

    payload = {
        "requestId": "13",
        "data": {
            "appid": "admin",
            "password": "123456",
            "identifier": "fd4b1aacdf9a0b334c4b3f616812bb12",
            "timestamp": "20240901",
            "tenantId": "452748015218757"
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("✅ getToken 返回:", data)

        # 这里根据实际返回的 JSON 结构提取 token
        token = data.get("data", {}).get("requestId")
        print("✅ 解析出的 token:", token)
        return token
    except requests.RequestException as e:
        print(f"❌ 获取 token 失败: {e}")
        return None


def get_device_info(device_name, token):
    url = f"{BASE_URL}/device/getDeviceDetailByDeviceName"
    headers = {
        "Content-Type": "application/json",
        "token": f"{token}"  # 一般是这样传，具体要看你后端要求
    }
    payload = {
        "data": {
            "deviceName": device_name,
            "productKey": "None"
        },
        "requestId": 45
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        device_info = response.json()
        print("✅ 查询成功，返回：", device_info)
        if device_info.get("data") is None:
            return False
        return True
    except requests.RequestException as e:
        print(f"❌ 查询失败: {e}")
        return False


if __name__ == "__main__":
    token = get_token()
    if token:
        get_device_info("ddd", token)

    String tmp = ""