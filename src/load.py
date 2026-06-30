"""
Load Module

Responsible for:
- Saving transformed data
- Appending new records
- Loading data into storage
"""


from pathlib import Path

import pandas as pd

from src.config import OUTPUT_FILE
from src.logger import get_logger

logger = get_logger(__name__)


class WeatherLoader:
     """
        Save DataFrame to CSV.
        Creates a new file if one does not exist.

        Args:
            dataframe (pd.DataFrame)
        """
     
     def save_to_csv(self, dataframe: pd.DataFrame) -> None:
        """
        Save DataFrame to CSV.
        Creates a new file if one does not exist.

        Args:
            dataframe (pd.DataFrame)
        """

        if dataframe.empty:
            logger.warning("DataFrame is empty. No data to save.")
            return
        
        logger.info(f"Saving DataFrame to {OUTPUT_FILE}...")

        dataframe.to_csv(OUTPUT_FILE, index=False)

        logger.info(f"DataFrame saved successfully to {OUTPUT_FILE}.")

     def append_to_csv(self, dataframe: pd.DataFrame) -> None:
        """
        Append data to an existing CSV.

        If the CSV doesn't exist, create it.

        Args:
            dataframe (pd.DataFrame)
        """

        if dataframe.empty:
            logger.warning("DataFrame is empty. No data to append.")
            return
        
        file_exists = Path(OUTPUT_FILE).exists()

        logger.info(f"{'Appending to' if file_exists else 'Creating'} {OUTPUT_FILE}...")

        dataframe.to_csv(OUTPUT_FILE, mode='a', header=not file_exists, index=False)

        logger.info(f"Data {'appended' if file_exists else 'saved'} successfully to {OUTPUT_FILE}.")
        
