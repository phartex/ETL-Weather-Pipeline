from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

print("Current directory:", BASE_DIR)
print("Looking for:", ENV_FILE)
print("Exists?", ENV_FILE.exists())

loaded = load_dotenv(ENV_FILE)
print("Loaded:", loaded)

print("API_KEY:", os.getenv("API_KEY"))
print("BASE_URL:", os.getenv("BASE_URL"))
print("UNITS:", os.getenv("UNITS"))