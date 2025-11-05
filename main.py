
import sys
from pathlib import Path
# Add 'src' folder to Python path
sys.path.append(str(Path(__file__).parent / "src"))
# main.py
from cnnClassifier import logger
from cnnClassifier.pipeline.first_stage_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    pipeline = DataIngestionPipeline()
    pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e



