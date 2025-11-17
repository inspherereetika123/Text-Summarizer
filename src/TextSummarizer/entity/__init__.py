from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_url: str
    local_data_file: str
    unzip_dir: str

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: str
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list