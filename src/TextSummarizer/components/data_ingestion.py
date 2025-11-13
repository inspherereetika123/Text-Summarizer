import os
import urllib.request as request
import zipfile
from pathlib import Path
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """Downloads the dataset if it doesn't already exist."""
        if not os.path.exists(self.config.local_data_file):
            logger.info("Downloading file...")
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file successfully: {filename}")
            file_size = get_size(Path(self.config.local_data_file))
            logger.info(f"File size: {file_size}")
            logger.info(f"Download info:\n{headers}")
        else:
            file_size = get_size(Path(self.config.local_data_file))
            logger.info(f"File already exists: {self.config.local_data_file} | Size: {file_size}")

    def extract_zip_file(self):
        """Extracts the zip file into the specified directory."""
        if not os.path.exists(self.config.local_data_file):
            logger.error(f"ZIP file not found: {self.config.local_data_file}")
            raise FileNotFoundError(f"{self.config.local_data_file} not found.")

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        logger.info(f"Extracting {self.config.local_data_file} to {unzip_path}")

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Extraction completed! Files are available at: {unzip_path}")
