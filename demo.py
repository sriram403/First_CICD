from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.config.configuration import MyConfigurationInfo

from housing.component.data_transformation import DataTransformation
import sys
def test():
    try : 
        pipeline = Pipeline()
        pipeline.run_pipeline()
        # i = MyConfigurationInfo()
        # v = i.get_datatransformation_config()
        # file_path = r"B:\jupyternotebook\mlboot\mlprojectpipelines\tutorial1\tutorial_project\housing\artifact\data_ingestion\2022-41-03_13-41-11\ingested_data\train\housing.csv"
        # schema_path = r"B:\jupyternotebook\mlboot\mlprojectpipelines\tutorial1\tutorial_project\config\schema.yaml"
        # i = DataTransformation().load_data(file_path,schema_path)
        # return i
    #     print(v)
    except Exception as e:
        raise HousingException(e,sys) from e

if __name__ == '__main__':
    test()

