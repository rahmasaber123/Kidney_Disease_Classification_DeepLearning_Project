# data_ingestion.py
import os
import zipfile
from pathlib import Path
from cnnClassifier.utils.common import get_size
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def prepare_data(self) -> Path:
        logger.info("Entered the prepare_data method of DataIngestion class")
        
        zip_path = Path(self.config.local_data_file)
        extract_to = Path(self.config.unzipped_data_dir)

        if not zip_path.exists():
            raise FileNotFoundError(f"ZIP file not found at {zip_path}. Make sure it exists!")

        logger.info(f"ZIP file found: {zip_path} ({get_size(zip_path)})")

        extract_to.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        logger.info(f"Files extracted to: {extract_to}")
        return extract_to
