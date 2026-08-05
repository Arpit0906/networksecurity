from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validtion import DataValidation
from networksecurity.components.data_transformation import DataTransformation
import sys
from networksecurity.exception.exception import Networksecurityexception
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try:
        trainingpipelineobj=TrainingPipelineConfig()
        dataingestionconfigobj=DataIngestionConfig(training_pipeline_config=trainingpipelineobj)
        dataingestionobj=DataIngestion(data_ingestion_config=dataingestionconfigobj)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifact=dataingestionobj.initiate_data_ingestion()
        logging.info("Data Ingestion completed!")
        print( data_ingestion_artifact)

        data_validation_config_obj = DataValidationConfig(
            training_pipeline_config=trainingpipelineobj
        )
        data_validation_obj=DataValidation(data_validation_config=data_validation_config_obj,data_ingestion_artifact=data_ingestion_artifact)
        logging.info("Initiate the data validation")
        data_validation_artifact=data_validation_obj.initiate_data_validation()
        logging.info("Data Validation completed")
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(training_pipeline_config=trainingpipelineobj)
        logging.info("data Transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
    except Exception as e:
        raise Networksecurityexception(e,sys)
