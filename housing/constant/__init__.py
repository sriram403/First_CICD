#Step - 2
import os
from datetime import datetime

ROOT_DIR = os.getcwd()#to get current root directory 

CONFIG_DIRECTORY = "config"
CONFIG_FILENAME = "config.yaml"

CONFIG_FILEPATH = os.path.join(ROOT_DIR,CONFIG_DIRECTORY,CONFIG_FILENAME)

CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"#add f string if got any error

#datatransformation related variables
COLUMN_TOTAL_ROOMS = "total_rooms"
COLUMN_POPULATION = "population"
COLUMN_HOUSEHOLDS = "households"
COLUMN_TOTAL_BEDROOM = "total_bedrooms"
DATASET_SCHEMA_COLUMNS_KEY = "columns"

NUMERICAL_COLUMN_KEY = "numerical_columns"
CATEGORICAL_COLUMN = "categorical_columns"
TARGET_COLUMN_KEY ="target_column"


#its info is on the config folder config.yaml
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
PIPELINE_NAME_KEY = "pipeline_name"
ARTIFACT_DIR_KEY  = "artifact_dir"

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_file_dir"
DATA_VALIDATION_ARTIFACT_DIR = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME = "schema_report_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME = "report_page_file_name"


DATA_TRANSFORMATION_ARTIFACT_DIR = "data_tranformation"
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY = "add_bedroom_per_room"
DATA_TRANSFORAMTION_DIR_NAME_KEY ="transformed_dir"
DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY="transformed_train_dir"
DATA_TRANSFORMATION_TEST_DIR_NAME_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY ="preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY ="preprocessed_object_file_name"


















