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

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir:Path
    data_path : Path
    tokenizer_name : Path