from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
import sys
def test():
    try : 
        pipeline = Pipeline()
        pipeline.run_pipeline()
    except Exception as e:
        raise HousingException(e,sys) from e

if __name__ == '__main__':
    test()

