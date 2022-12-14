from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.config.configuration import MyConfigurationInfo


from housing.component.data_transformation import DataTransformation
import sys,os
def test():
    try : 
        path = r"B:\jupyternotebook\mlboot\mlprojectpipelines\tutorial1\tutorial_project\config\config.yaml"
        config_file_path = path
        config_file_path
        config = MyConfigurationInfo(config_file_path)
        pipeline = Pipeline(config)
        pipeline.run_pipeline()
        pipeline.start()
        pipeline.experiment
        print(pipeline.get_experiments_status())
        # pipeline = Pipeline(config)
        # pipeline.run()
        # pipeline.experiment
        # pipeline.save_experiment()
        # print(pipeline.get_experiments_status())

    except Exception as e:
        raise HousingException(e,sys) from e

if __name__ == '__main__':
    test()

