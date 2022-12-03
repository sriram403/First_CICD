import yaml
from housing.exception import HousingException
import os,sys



def get_yaml_file(file_dir:str)->dict:
    """read the yaml file"""
    config_info = None
    try:
        with open(file_dir,"rb") as yaml_file:
            config_info = yaml.safe_load(yaml_file)
        return config_info
    except Exception as e:
        raise HousingException(e,sys) from e
        






