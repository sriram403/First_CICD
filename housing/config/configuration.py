#step -3
from housing.entity.config_entity import DataIntegrationConfig,DataValidationConfig,DataTransformationConfig \
    ,ModelTrainerConfig,ModelEvaluationConfig,ModelPusherConfig,TrainingPipelineConfig
from housing.util.util import *
from housing.constant import *
from housing.exception import HousingException
from housing.logger import logging
import os,sys


class MyConfigurationInfo:
    def __init__(self,config_file_path:str = CONFIG_FILEPATH,current_time_stamp:str = CURRENT_TIMESTAMP) -> None:
        self.config_info = read_yaml_file(config_file_path)
        self.training_pipeline_config = self.get_modeltrainingpipeline_config()
        self.time_stamp = current_time_stamp
    
    def get_dataingestion_config(self)->DataIntegrationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            stored_time_stamp = self.time_stamp
            data_ingestion_artifact_dir = os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,stored_time_stamp)
            
            data_ingestion = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            dataset_download_url = data_ingestion[DATA_INGESTION_DOWNLOAD_URL_KEY]
            
            dataset_rawdata_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion[DATA_INGESTION_RAW_DATA_DIR_KEY])
            dataset_extracting_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            
            ingested_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion[DATA_INGESTION_DIR_NAME_KEY])
            dataset_train_dir = os.path.join(ingested_data_dir,data_ingestion[DATA_INGESTION_TRAIN_DIR_KEY])
            dataset_test_dir = os.path.join(ingested_data_dir,data_ingestion[DATA_INGESTION_TEST_DIR_KEY])
            
            data_ingestion_config = DataIntegrationConfig(download_url=dataset_download_url,
                                                        zip_folder=dataset_extracting_dir,
                                                        extract_folder=dataset_rawdata_dir,
                                                        train_dataset_folder=dataset_train_dir,
                                                        test_dataset_folder=dataset_test_dir,
                                                        stored_time_var = stored_time_stamp)
            
            logging.info(f"Data Ingestion Created from Configuration:{data_ingestion_config}")
            
            return data_ingestion_config

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_datavalidation_config(self)->DataValidationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_validation_artifact_dir = os.path.join(artifact_dir,DATA_VALIDATION_ARTIFACT_DIR,self.time_stamp)

            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]


            schema_file_path = os.path.join(ROOT_DIR,data_validation_config[DATA_VALIDATION_SCHEMA_DIR_KEY],data_validation_config[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY])

            report_file_path = os.path.join(data_validation_artifact_dir,data_validation_config[DATA_VALIDATION_REPORT_FILE_NAME])

            report_page_file_path = os.path.join(data_validation_artifact_dir,data_validation_config[DATA_VALIDATION_REPORT_PAGE_FILE_NAME])

            data_validation_config = DataValidationConfig(schema_file_path,report_page_file_path=report_page_file_path,\
                                                    schema_report_path=report_file_path)

            
            return data_validation_config
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_datatransformation_config(self)->DataTransformationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_transformation_artifact_dir= os.path.join(artifact_dir,DATA_TRANSFORMATION_ARTIFACT_DIR,CURRENT_TIMESTAMP)

            data_tranformation_config_info = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]

            bedroom_per_room = data_tranformation_config_info[DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY]
            
            preprocessed_object_file_path = os.path.join(
                data_transformation_artifact_dir,
                data_tranformation_config_info[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY],
                data_tranformation_config_info[DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY],
            )
            tranformed_train_dir = os.path.join(
                data_transformation_artifact_dir,
                data_tranformation_config_info[DATA_TRANSFORAMTION_DIR_NAME_KEY],
                data_tranformation_config_info[DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY]
            )
            tranformed_test_dir =os.path.join(
                data_transformation_artifact_dir,
                data_tranformation_config_info[DATA_TRANSFORAMTION_DIR_NAME_KEY],
                data_tranformation_config_info[DATA_TRANSFORMATION_TEST_DIR_NAME_KEY]
            )

            data_transformation_config = DataTransformationConfig(
                bedroom_per_room,
                tranformed_train_dir,
                tranformed_test_dir,
                preprocessed_object_file_path)
            logging.info(f"created data_transformation_config {data_transformation_config}")
            
            return data_transformation_config

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_modeltrainer_config(self)->ModelTrainerConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            model_training_artifact_dir = os.path.join(artifact_dir,MODEL_TRAINER_ARTIFACT_DIR,self.time_stamp)
            
            model_training_config_info = self.config_info[MODEL_TRAINER_CONFIG_KEY]

            trained_model_file_path = os.path.join(model_training_artifact_dir,
                                                model_training_config_info[MODEL_TRAINER_TRAINED_MODEL_DIR_KEY],
                                                model_training_config_info[MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY])

            model_config_file_path = os.path.join(model_training_config_info[MODEL_TRAINER_MODEL_CONFIG_DIR_KEY],
                                                model_training_config_info[MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY])

            base_accuracy = model_training_config_info[MODEL_TRAINER_BASE_ACCURACY_KEY]

            model_trainer_config = ModelTrainerConfig(trained_model_file_path,base_accuracy,model_config_file_path)
            
            logging.info(f"Model Trainer Config: {model_trainer_config}")
            return model_trainer_config
            
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_modelevaluation_config(self)->ModelEvaluationConfig:
        try:
            model_evaluation_config = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            
            artifact_dir = os.path.join(self.training_pipeline_config.artifact_dir,MODEL_EVALUATION_ARTIFACT_DIR)

            model_evaluation_file_path = os.path.join(artifact_dir,model_evaluation_config[MODEL_EVALUATION_FILE_NAME_KEY])
            
            response = ModelEvaluationConfig(model_evaluation_file_path,self.time_stamp)

            logging.info(f"Model Evaluation Config :[{response}]")
            return response
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_modelpusher_config(self)->ModelPusherConfig:
        try:
            time_stamp = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
            model_pusher_config_info = self.config_info[MODEL_PUSHER_CONFIG_KEY]
            export_dir_path = os.path.join(ROOT_DIR, model_pusher_config_info[MODEL_PUSHER_MODEL_EXPORT_DIR_KEY],
                                           time_stamp)

            model_pusher_config = ModelPusherConfig(export_dir_path=export_dir_path)
            logging.info(f"Model pusher config {model_pusher_config}")
            return model_pusher_config

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_modeltrainingpipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,training_pipeline_config[PIPELINE_NAME_KEY],
                                        training_pipeline_config[ARTIFACT_DIR_KEY])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config:{training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e
















