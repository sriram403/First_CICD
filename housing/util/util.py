import yaml
from housing.exception import HousingException
import os,sys,dill,numpy as np,pandas as pd
from housing.constant import *

def write_yaml_file(dir,data:dict = None):
    try:
        os.makedirs(os.path.dirname(dir),exist_ok=True)
        with open(dir,"w") as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e



def read_yaml_file(file_dir:str)->dict:
    """read the yaml file"""
    config_info = None
    try:
        with open(file_dir,"rb") as yaml_file:
            config_info = yaml.safe_load(yaml_file)
        return config_info
    except Exception as e:
        raise HousingException(e,sys) from e
        

def save_numpy_array_data(file_path:str,array : np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            np.save(file_obj,array)
    except Exception as e:
        raise HousingException(e,sys) from e

def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path,"rb") as file_obj:
            return np.load(file_obj)
        
    except Exception as e:
        raise HousingException(e,sys) from e

def save_object(file_path:str,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e

def load_object(file_path:str):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise HousingException(e,sys) from e



#becoz there is no self or we are not using self we can say that it's a static method now
#we can call it whenever we want 
#this was inside a class but we moved it here (data_transformation.py)
# @staticmethod
def load_data(file_path:str,schema_file_path:str)->pd.DataFrame:
    try:
        dataset_schema = read_yaml_file(schema_file_path)

        scheme = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]

        dataframe = pd.read_csv(file_path)

        error_message = ""

        for columns in dataframe.columns:
            if columns in list(scheme.keys()):
                dataframe[columns].astype(scheme[columns])
            else:
                error_message = f"{error_message} \n column : {columns} is not in the schema"
        if len(error_message)>0:
            raise Exception(error_message)
        return dataframe

    except Exception as e:
        raise HousingException(e,sys)










