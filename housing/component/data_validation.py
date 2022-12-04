from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import sys,os,yaml,pandas as pd

class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,data_ingestion_artifact:DataIngestionArtifact) -> None:
        try:
            pass
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def is_train_test_file_exists(self)->bool:
        try:
            logging.info(f"checking whether train and test file exists : )\n {'='*20}\n")
            is_train_file_exist = False
            is_test_file_exist = False
            
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            if os.path.exists(train_file_path):
                is_train_file_exist = True
            if os.path.exists(test_file_path):
                is_test_file_exist = True
            
            logging.info(f"exists ? -> {os.path.exists(train_file_path) and os.path.exists(test_file_path)} :) good for you dumbass")
            is_available = is_train_file_exist and is_test_file_exist
            
            if not is_available:
                
                training_path = self.data_ingestion_artifact.train_file_path
                testing_path = self.data_ingestion_artifact.test_file_path
                message = f"Training File :{training_path} Testing File :{testing_path}"
                logging.info(f"{message} is not available")
                
                raise Exception(f"training and testing file is not available :( bitch!!\n{message}\n")        
            
            
            return is_available
        except Exception as e:
            raise HousingException(e,sys) from e
    
    
    def validation_dataset_schema(self)->bool:
        try:
            validation_status = False
            
            url = "B:\\jupyternotebook\\mlboot\\mlprojectpipelines\\tutorial1\\tutorial_project\\config\\schema.yaml"
            with open(url,"r") as f:
                file = yaml.safe_load(f)
            
            def checking_values(data)->bool:
                link = f"B:\\jupyternotebook\\mlboot\\mlprojectpipelines\\tutorial1\\tutorial_project\\housing\\artifact\\data_ingestion\\2022-19-03_14-19-15\\ingested_data\\{data}\\housing.csv"
                df = pd.read_csv(url)
                
                is_columns_name_equal = list(file["columns"].keys()) == df.columns
                is_columns_length_equal = len(list(file["columns"].keys())) == len(df.columns)
                i = file["domain_value"]["ocean_proximity"]
                v = df.ocean_proximity.value_counts().index
                is_domain_values_are_equal = i==v
                
                return is_columns_length_equal and is_columns_name_equal and is_domain_values_are_equal
            
            is_train_data_same = checking_values("train")
            is_test_data_same = checking_values("test")
            if is_train_data_same == is_test_data_same:
                validation_status = True
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e
    
    
    
    
    
    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exists()
            self.validation_dataset_schema()

        except Exception as e:
            raise HousingException(e,sys) from e
    