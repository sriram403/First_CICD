from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.config.configuration import MyConfigurationInfo
import sys
def test():
    try : 
        # pipeline = Pipeline()
        # pipeline.run_pipeline()
        i = MyConfigurationInfo()
        v = i.get_datavalidation_config()
        print(v)
    except Exception as e:
        raise HousingException(e,sys) from e

if __name__ == '__main__':
    test()

