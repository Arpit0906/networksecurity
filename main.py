from networksecurity.components.data_ingestion import DataIngestion
import sys
from networksecurity.exception.exception import Networksecurityexception
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipelineobj=TrainingPipelineConfig()
        dataingestionconfigobj=DataIngestionConfig(training_pipeline_config=trainingpipelineobj)
        dataingestionobj=DataIngestion(data_ingestion_config=dataingestionconfigobj)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact=dataingestionobj.initiate_data_ingestion()
        print( data_ingestion_artifact)
    except Exception as e:
        raise Networksecurityexception(e,sys)