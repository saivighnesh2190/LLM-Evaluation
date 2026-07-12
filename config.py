import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY is missing.")

MODEL_NAME = os.getenv("MODEL_NAME")
if not MODEL_NAME:
    raise ValueError("MODEL_NAME is missing.")

BASE_URL = os.getenv("BASE_URL")
if not BASE_URL:
    raise ValueError("BASE_URL is missing.")

try:
    TIMEOUT = int(os.getenv("TIMEOUT", 30))
except ValueError as exc:
    raise ValueError("TIMEOUT must be an integer.") from exc
