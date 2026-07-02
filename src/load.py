"""
Load Module

Responsible for:
- Loading transformed data into PostgreSQL
"""

from sqlalchemy import create_engine
import pandas as pd

from src.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)

from src.logger import get_logger

logger = get_logger(__name__)


class WeatherLoader:

    def __init__(self):

        self.engine = create_engine(
            f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

    def load_to_database(self, dataframe: pd.DataFrame):

        if dataframe.empty:
            logger.warning("No data to load.")
            return

        logger.info("Loading data into PostgreSQL...")

        dataframe.to_sql(
            "weather_data",
            self.engine,
            if_exists="append",
            index=False,
        )

        logger.info("Data loaded successfully.")