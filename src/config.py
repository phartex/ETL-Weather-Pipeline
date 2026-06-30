from pathlib import Path
import os
from dotenv import load_dotenv

print("========== CONFIG FILE LOADED ==========")

BASE_DIR = Path(__file__).resolve().parent.parent
print("BASE_DIR:", BASE_DIR)

ENV_FILE = BASE_DIR / ".env"
print("ENV FILE:", ENV_FILE)
print("ENV EXISTS:", ENV_FILE.exists())

loaded = load_dotenv(dotenv_path=ENV_FILE)

print("LOADED:", loaded)

API_KEY = os.getenv("API_KEY")

print("API_KEY:", API_KEY)

BASE_URL = os.getenv(
    "BASE_URL",
    "https://api.openweathermap.org/data/2.5/weather",
)

UNITS = os.getenv("UNITS", "metric")

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

INPUT_FILE = DATA_DIR / "cities.csv"
OUTPUT_FILE = DATA_DIR / "weather_data.csv"
LOG_FILE = LOG_DIR / "pipeline.log"

if not API_KEY:
    raise ValueError("API_KEY not found.")

print("FINAL API_KEY =", repr(API_KEY))