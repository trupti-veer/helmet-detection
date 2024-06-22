import sys
from helmetdetection.datacomponents.data_ingestion import DataIngestion
from helmetdetection.configuration.s3_operations import S3Operation
from helmetdetection.entity.config_entity import DataIngestionConfig
from helmetdetection.entity.artifacts_entity import DataIngestionArtifacts
from helmetdetection.logger import logging
from helmetdetection.exception import HDException


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.s3_operations = S3Operation()

    def start_data_ingestion(self) -> DataIngestionArtifacts:          
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting the data from S3 bucket")
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config, s3_operations= S3Operation()
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train, test and valid from s3")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact

        except Exception as e:
            raise HDException(e, sys) from e
        
    def run_pipeline(self) -> None:
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise HDException(e, sys) from e