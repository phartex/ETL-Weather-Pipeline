"""
Extract Module

Responsible for:
- Reading city names from CSV
- Calling the OpenWeather API
- Returning raw weather data
"""

from typing import List, Dict

import pandas as pd
import requests

from src.config import (
    API_KEY,
    BASE_URL,
    INPUT_FILE,
    UNITS,
)

from src.logger import get_logger

logger = get_logger(__name__)


class WeatherExtractor:
    """
    Handles extraction of weather data from OpenWeather API.
    """

    def read_cities(self) -> List[str]:
        """
        Reads city names from cities.csv.

        Returns:
            List[str]
        """

        try:
            df = pd.read_csv(INPUT_FILE)

            if "City" not in df.columns:
                raise ValueError(
                    "cities.csv must contain a 'City' column."
                )

            cities = (
                df["City"]
                .dropna()
                .astype(str)
                .str.strip()
                .tolist()
            )

            logger.info(f"{len(cities)} cities loaded.")

            return cities

        except Exception as e:
            logger.exception("Failed to read cities.csv")
            raise e

    def fetch_weather(self, city: str) -> Dict:
        """
        Fetch weather data for a single city.

        Args:
            city (str)

        Returns:
            dict
        """

        params = {
            "q": city,
            "appid": API_KEY,
            "units": UNITS,
        }

        try:

            logger.info(f"Fetching weather for {city}")

            response = requests.get(
                BASE_URL,
                params=params,
                timeout=20,
            )

            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as e:

            logger.error(
                f"HTTP Error for {city}: {e}"
            )

        except requests.exceptions.Timeout:

            logger.error(
                f"Timeout while requesting {city}"
            )

        except requests.exceptions.ConnectionError:

            logger.error(
                f"Connection error for {city}"
            )

        except Exception as e:

            logger.exception(
                f"Unexpected error while requesting {city}"
            )

        return {}

    def extract(self) -> List[Dict]:
        """
        Executes the Extract phase.

        Returns:
            List of JSON responses.
        """

        weather_data = []

        cities = self.read_cities()

        for city in cities:

            result = self.fetch_weather(city)

            if result:
                weather_data.append(result)

        logger.info(
            f"{len(weather_data)} weather records extracted."
        )

        return weather_data