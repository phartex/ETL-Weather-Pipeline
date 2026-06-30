"""
Main ETL Pipeline

Responsible for:
- Coordinating Extract, Transform and Load
- Handling pipeline execution
- Logging pipeline status
"""

from src.extract import WeatherExtractor
from src.transform import WeatherTransformer
from src.load import WeatherLoader
from src.logger import get_logger

logger = get_logger(__name__)


class WeatherETLPipeline:
    """
    Coordinates the ETL process.
    """

    def __init__(self):
        self.extractor = WeatherExtractor()
        self.transformer = WeatherTransformer()
        self.loader = WeatherLoader()

    def run(self) -> None:
        """
        Execute the complete ETL pipeline.
        """

        logger.info("=" * 60)
        logger.info("Weather ETL Pipeline Started")
        logger.info("=" * 60)

        try:
            # -----------------------------
            # Extract
            # -----------------------------
            weather_data = self.extractor.extract()

            # -----------------------------
            # Transform
            # -----------------------------
            dataframe = self.transformer.transform(weather_data)

            # -----------------------------
            # Load
            # -----------------------------
            self.loader.save_to_csv(dataframe)

            logger.info("=" * 60)
            logger.info("Weather ETL Pipeline Completed Successfully")
            logger.info("=" * 60)

        except Exception as error:
            logger.exception(f"Pipeline failed: {error}")
            raise