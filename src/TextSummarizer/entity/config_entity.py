from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen = True)
class DataValidationConfig:
    root_dir:Path
    source_url: str
    local_data_file : Path
    unzip_dir : Path

class DataValidationConfig:
    def __init__(self, root_dir, STATUS_FILE, ALL_REQUIRED_FILES):
        self.root_dir = root_dir
        self.STATUS_FILE = STATUS_FILE
        self.ALL_REQUIRED_FILES = ALL_REQUIRED_FILES


