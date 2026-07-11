import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if API_KEY is None:
    raise ValueError("OPENAI_API_KEY is missing.")

MODEL_NAME = os.getenv("MODEL_NAME", "mock-llm")
BASE_URL = os.getenv("BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT", 30))