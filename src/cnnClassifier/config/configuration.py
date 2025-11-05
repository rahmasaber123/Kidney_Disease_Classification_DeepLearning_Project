# src/cnnClassifier/config/configuration.py

from pathlib import Path
from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath: Path = CONFIG_FILE_PATH,
                 params_filepath: Path = PARAMS_FILE_PATH):
        """
        Initializes ConfigurationManager by reading config and params YAML files
        and creating the artifacts root directory.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Ensure artifacts root directory exists
        create_directories([Path(self.config.artifacts_root)])

    def data_ingestion_config(self) -> DataIngestionConfig:
        """
        Returns a DataIngestionConfig object based on config.yaml settings.
        Ensures the data ingestion root directory exists.
        """
        ingestion_cfg = self.config.data_ingestion

        # Create root directory for data ingestion
        create_directories([Path(ingestion_cfg.root_dir)])

        return DataIngestionConfig(
            root_dir=Path(ingestion_cfg.root_dir),
            source_URL=str(ingestion_cfg.source_URL),
            local_data_file=Path(ingestion_cfg.local_data_file),
            unzipped_data_dir=Path(ingestion_cfg.unzipped_data_dir)
        )

