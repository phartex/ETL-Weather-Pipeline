"""
Transform Module

Responsible for:
- Cleaning raw weather API responses
- Converting timestamps
- Creating a DataFrame
"""

from datetime import datetime
from typing import Dict, List

import pandas as pd

from src.logger import get_logger

logger = get_logger(__name__)


class WeatherTransformer:
    """
    Handles transformation of raw weather data.
    """

    def clean_data(self, weather_data: List[Dict]) -> List[Dict]:
        """
        Extract only the required fields from the raw API response.

        Args:
            weather_data (List[Dict])

        Returns:
            List[Dict]
        """

        cleaned_records = []

        extraction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        logger.info("Cleaning weather data...")

        for record in weather_data:

            cleaned_record = {

                "City": record.get("name"),

                "Country": record.get("sys", {}).get("country"),

                "Temperature": record.get("main", {}).get("temp"),

                "FeelsLike": record.get("main", {}).get("feels_like"),

                "Humidity": record.get("main", {}).get("humidity"),

                "Pressure": record.get("main", {}).get("pressure"),

                "WindSpeed": record.get("wind", {}).get("speed"),

                "Weather": (
                    record.get("weather", [{}])[0].get("main")
                    if record.get("weather")
                    else None
                ),

                "Description": (
                    record.get("weather", [{}])[0].get("description")
                    if record.get("weather")
                    else None
                ),

                "ObservationTime": (
                    datetime.fromtimestamp(record["dt"]).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                    if record.get("dt")
                    else None
                ),

                "ExtractionTime": extraction_time,
            }

            cleaned_records.append(cleaned_record)

        logger.info(f"{len(cleaned_records)} records cleaned.")

        return cleaned_records

    def create_dataframe(self, cleaned_records: List[Dict]) -> pd.DataFrame:
        """
        Convert cleaned records into a Pandas DataFrame.

        Args:
            cleaned_records (List[Dict])

        Returns:
            pd.DataFrame
        """

        logger.info("Creating DataFrame...")

        dataframe = pd.DataFrame(cleaned_records)

        logger.info("DataFrame created successfully.")

        return dataframe

    def transform(self, weather_data: List[Dict]) -> pd.DataFrame:
        """
        Complete transformation process.

        Args:
            weather_data (List[Dict])

        Returns:
            pd.DataFrame
        """

        logger.info("Starting transformation...")

        cleaned_records = self.clean_data(weather_data)

        dataframe = self.create_dataframe(cleaned_records)

        logger.info("Transformation completed successfully.")

        return dataframe