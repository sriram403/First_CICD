from housing.entity.config_entity import DataIntegrationConfig
import sys,os
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit
from six.moves import urllib

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIntegrationConfig) -> None:
        try:
            logging.info(f"{'='*20}data_ingestion log started{'='*20}\n\n")
            self.data_ingestion_config = data_ingestion_config
        
        except Exception as e:
            raise HousingException(e,sys)
    
    def download_housing_data(self)->str:
        try:
            my_download_url = self.data_ingestion_config.download_url
            
            download_folder = self.data_ingestion_config.zip_folder
            # if os.path.exists(download_folder):
            #     os.remove(download_folder)
            os.makedirs(download_folder,exist_ok=True)

            file_name = os.path.basename(my_download_url)
            
            tgz_file_path = os.path.join(download_folder,file_name)
            
            logging.info(f"downloading file from my_download_url into [{tgz_file_path}]")
            urllib.request.urlretrieve(my_download_url,tgz_file_path)
            logging.info("data download completed successfully :) [happy face]")
            
            return tgz_file_path

        except Exception as e:
            raise HousingException(e,sys) from e
    
    def extract_tgz_file(self,tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.extract_folder

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"starting extraction process in [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as f:
                f.extractall(path = raw_data_dir)
            logging.info(f"extraction completed :) ")

        except Exception as e:
            raise HousingException(e,sys) from e

    def split_data_as_train_test(self)->DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.extract_folder
            file_name = os.listdir(raw_data_dir)[0]
            full_file_path = os.path.join(raw_data_dir,file_name)

            logging.info(f"reading csv file from [{full_file_path}]")
            housing_data_frame = pd.read_csv(full_file_path)
            housing_data_frame["income_categorical"] = pd.cut(housing_data_frame["median_income"],
            bins=[0.0,1.5,3.0,4.5,6.0,np.inf],labels=[1,2,3,4,5])
            
            strat_train_split = None
            strat_test_split = None

            
            splitfunc = StratifiedShuffleSplit(n_splits=1,test_size=0.2)
            logging.info(f"splitting the data into train and test split")
            for train_index,test_index in splitfunc.split(housing_data_frame,housing_data_frame['income_categorical']):
                strat_train_split = housing_data_frame.loc[train_index].drop(["income_categorical"],axis=1)
                strat_test_split = housing_data_frame.loc[test_index].drop(["income_categorical"],axis=1)

            train_data_dir = os.path.join(self.data_ingestion_config.train_dataset_folder,file_name)
            test_data_dir = os.path.join(self.data_ingestion_config.test_dataset_folder,file_name)

            logging.info(f"storing the train_data in [{train_data_dir}] \n and testing data in [{test_data_dir}]")
            if strat_train_split is not None:
                os.makedirs(self.data_ingestion_config.train_dataset_folder,exist_ok=True)
                strat_train_split.to_csv(train_data_dir,index=False)
            if strat_test_split is not None:
                os.makedirs(self.data_ingestion_config.test_dataset_folder,exist_ok=True)
                strat_test_split.to_csv(test_data_dir,index=False)

            data_ingestion_artifact = DataIngestionArtifact(train_data_dir,test_data_dir,True,"data split successfull :) ")
            logging.info(f"stored all the outputs of the splitting into [{data_ingestion_artifact}]")
            return data_ingestion_artifact



        except Exception as e:
            raise HousingException(e,sys) from e

        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path = self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise HousingException(e,sys) from e #it's for routing the exception to its original place :)



    def __del__(self):
        logging.info(f"{'='*20}data_ingestion log closed{'='*20} :) ! ")