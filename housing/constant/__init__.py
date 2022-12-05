import os
from datetime import datetime

ROOT_DIR = os.getcwd()#to get current root directory 

CONFIG_DIRECTORY = "config"
CONFIG_FILENAME = "config.yaml"

CONFIG_FILEPATH = os.path.join(ROOT_DIR,CONFIG_DIRECTORY,CONFIG_FILENAME)

CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"#add f string if got any error

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
















