import os
from pathlib import Path
from TextSummarizer.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from TextSummarizer.utils.common import read_yaml, create_directories
from TextSummarizer.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig
)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH
    ):
        # Load YAML files
        self.config = read_yaml(Path(config_filepath))
        self.params = read_yaml(Path(params_filepath))

        # Create artifacts root folder
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
