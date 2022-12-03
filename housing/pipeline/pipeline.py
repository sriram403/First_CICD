from housing.config.configuration import MyConfigurationInfo
from housing.logger import logging
from housing.exception import HousingException

from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIntegrationConfig
from housing.component.data_ingestion import DataIngestion
import os,sys

class Pipeline:
    def __init__(self,config:MyConfigurationInfo = MyConfigurationInfo()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(self.config.get_dataingestion_config())

            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
            raise HousingException(e,sys) from e







