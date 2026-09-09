import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

JWT_USERNAME = os.getenv("JWT_USERNAME")
JWT_PASSWORD = os.getenv("JWT_PASSWORD")
TOKEN_URL = os.getenv("TOKEN_URL")

creds = base64.b64encode(f"{JWT_USERNAME}:{JWT_PASSWORD}".encode()).decode()


def Get_Jwt(credentials=creds, jwt_url=TOKEN_URL):
    try:
        response = requests.post(
            jwt_url,
            headers={"Authorization": f"Basic {credentials}"},
            verify="/etc/ssl/certs/ca-certificates.crt",
            timeout=30,
            )
        if response.status_code == 200:
            print("JWT Aquired")

            return response.text.strip()
    except RuntimeError as e:
        print(f"Error: {e}")