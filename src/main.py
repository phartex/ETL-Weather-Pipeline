"""
Main ETL Pipeline

Responsible for:
- Coordinating Extract, Transform and Load
- Exposing each ETL stage for Airflow tasks
"""

from pathlib import Path
import json

import pandas as pd

from src.extract import WeatherExtractor
from src.transform import WeatherTransformer
from src.load import WeatherLoader
from src.logger import get_logger

logger = get_logger(__name__)


class WeatherETLPipeline:

    def __init__(self):
        self.extractor = WeatherExtractor()
        self.transformer = WeatherTransformer()
        self.loader = WeatherLoader()

    # -------------------------------------------------
    # EXTRACT
    # -------------------------------------------------
    def extract(self) -> str:
        """
        Extract weather data and save it as JSON.

        Returns
        -------
        str
            Path to raw_weather.json
        """

        logger.info("Starting Extract Phase...")

        weather_data = self.extractor.extract()

        output_path = Path("data/raw_weather.json")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(weather_data, file, indent=4)

        logger.info(f"Raw weather saved to {output_path}")

        return str(output_path)

    # -------------------------------------------------
    # TRANSFORM
    # -------------------------------------------------
    def transform(self, raw_file: str) -> str:
        """
        Read raw JSON file and transform it.

        Parameters
        ----------
        raw_file : str
            Path returned from extract()

        Returns
        -------
        str
            Path to transformed CSV
        """

        logger.info("Starting Transform Phase...")

        with open(raw_file, "r", encoding="utf-8") as file:
            weather_data = json.load(file)

        dataframe = self.transformer.transform(weather_data)

        transformed_path = Path("data/transformed_weather.csv")

        dataframe.to_csv(transformed_path, index=False)

        logger.info(f"Transformed data saved to {transformed_path}")

        return str(transformed_path)

    # -------------------------------------------------
    # LOAD
    # -------------------------------------------------
    def load(self, transformed_file: str) -> None:
        """
        Load transformed CSV into the final destination.
        """

        logger.info("Starting Load Phase...")

        dataframe = pd.read_csv(transformed_file)

        self.loader.append_to_csv(dataframe)

        logger.info("Load completed successfully.")

    # -------------------------------------------------
    # COMPLETE PIPELINE
    # -------------------------------------------------
    def run(self) -> None:
        """
        Execute the full ETL pipeline.
        """

        logger.info("=" * 60)
        logger.info("Weather ETL Pipeline Started")
        logger.info("=" * 60)

        try:

            raw_file = self.extract()

            transformed_file = self.transform(raw_file)

            self.load(transformed_file)

            logger.info("=" * 60)
            logger.info("Weather ETL Pipeline Completed Successfully")
            logger.info("=" * 60)

        except Exception as error:
            logger.exception(f"Pipeline failed: {error}")
            raise