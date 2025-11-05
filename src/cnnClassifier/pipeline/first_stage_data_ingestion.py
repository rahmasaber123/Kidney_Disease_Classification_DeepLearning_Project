# first_stage_data_ingestion.py
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion  # <-- new import

class DataIngestionPipeline:
    def __init__(self):
        config_manager = ConfigurationManager()
        data_ingestion_config = config_manager.data_ingestion_config()
        self.data_ingestion = DataIngestion(config=data_ingestion_config)

    def main(self):
        self.data_ingestion.prepare_data()
