# step - 0
from collections import namedtuple

#using to store the path for all the information nessasary to download the data,unziping the data,and so on... 
DataIntegrationConfig = namedtuple("DataIntegrationConfig",["download_url","zip_folder","extract_folder","train_dataset_folder","test_dataset_folder"])

#using to store the path of the "file" which shows how much data columns and its data types are contained in the dataset
DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path","schema_report_path","report_page_file_path"])

#using to store the path for all the transformed dataset and it's requirement like can we add bedroom
DataTransformationConfig = namedtuple("DataTransformationConfig",["is_add_bedroom",
                                                                "transformed_train_dataset_dir",
                                                                "transformed_test_dataset_dir",
                                                                "pickle_file_of_data_transformation_object"])

#you know it now common you stupid idiot :)
ModelTrainerConfig = namedtuple("ModelTrainerConfig",["trained_model_file_path","base_accuracy","model_config_file_path"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir"])
#artifact == function or model ->returning thing 
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])




