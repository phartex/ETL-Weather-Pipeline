"""
Application configuration.
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# -------------------------------------------------
# Project Directories
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# Explicitly load .env from the project root
ENV_FILE = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_FILE)

# -------------------------------------------------
# Data Directories
# -------------------------------------------------

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

INPUT_FILE = DATA_DIR / "cities.csv"
OUTPUT_FILE = DATA_DIR / "weather_data.csv"
LOG_FILE = LOG_DIR / "pipeline.log"

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# -------------------------------------------------
# API Configuration
# -------------------------------------------------

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv(
    "BASE_URL",
    "https://api.openweathermap.org/data/2.5/weather",
)
UNITS = os.getenv("UNITS", "metric")

# -------------------------------------------------
# Debug (Temporary)
# -------------------------------------------------

print(f"BASE_DIR: {BASE_DIR}")
print(f"ENV FILE: {ENV_FILE}")
print(f"ENV EXISTS: {ENV_FILE.exists()}")
print(f"API_KEY: {API_KEY}")

# -------------------------------------------------
# Validation
# -------------------------------------------------

if not API_KEY:
    raise ValueError(
        "API_KEY not found. Please add it to your .env file."
    )