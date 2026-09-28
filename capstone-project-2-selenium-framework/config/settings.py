import os

BASE_URL = os.getenv("AE_BASE_URL", "https://automationexercise.com")
WAIT_SECONDS = int(os.getenv("AE_WAIT_SECONDS", "15"))