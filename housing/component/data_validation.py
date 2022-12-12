from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import sys,os,yaml,json,pandas as pd
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab



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
                df = pd.read_csv(link)
                
                is_columns_name_equal = list(file["columns"].keys()) == df.columns
                is_columns_length_equal = len(list(file["columns"].keys())) == len(df.columns)
                i = file["domain_value"]["ocean_proximity"]
                v = df.ocean_proximity.value_counts().index
                is_domain_values_are_equal = i==v
                z = is_columns_length_equal and set(is_columns_name_equal) and set(is_domain_values_are_equal)
                if False not in z:             
                    return True
            
            is_train_data_same = checking_values("train")
            is_test_data_same = checking_values("test")
            if is_train_data_same == is_test_data_same:
                validation_status = True
            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])
            
            train_df,test_df = self.get_train_and_test_df()
            
            profile.calculate(train_df,test_df)

            report = json.loads(profile.json())
            report_file_path = self.data_validation_config.schema_report_path

            report_dir = os.path.dirname(report_file_path)

            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path,"w") as report_file_path:
                json.dump(report,report_file_path,indent=6)
            
            return report

        except Exception as e:
            raise HousingException(e,sys) from e
    def save_data_drift_report_page(self):
        try:
            
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df,test_df = self.get_train_and_test_df()
            dashboard.calculate(train_df,test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path

            report_dir = os.path.dirname(report_page_file_path)

            os.makedirs(report_dir,exist_ok=True)
          
            dashboard.save(self.data_validation_config.report_page_file_path)

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def is_data_drift_found(self)->bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            
            return True
        except Exception as e:
            raise HousingException(e,sys) from e
    
    
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validation_dataset_schema()
            self.is_data_drift_found()
            url = "B:\\jupyternotebook\\mlboot\\mlprojectpipelines\\tutorial1\\tutorial_project\\config\\schema.yaml"
            data_validation_artifact = DataValidationArtifact(schema_file_path=url,
            report_file_path = self.data_validation_config.schema_report_path,
            report_page_file_path=self.data_validation_config.report_page_file_path,
            is_validated=True,
            message="Data Validation performed successfully")
            logging.info(f"Data Validation artifact : {data_validation_artifact}")
            return data_validation_artifact

        except Exception as e:
            raise HousingException(e,sys) from e
    