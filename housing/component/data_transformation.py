#step -3 
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataTransformationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
import os,sys,pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.preprocessing import OneHotEncoder
from housing.constant import *
from housing.util.util import get_yaml_file,save_numpy_array_data,save_object,load_data
from sklearn.impute import SimpleImputer


class FeatureGenerator(BaseEstimator,TransformerMixin):

    def __init__(self,add_bedrooms_per_room=True,total_room_ix=3,population_ix = 5,households_ix = 6,total_bedrooms_ix=4,
    columns=None):
        try:
            self.columns = columns
            # if self.columns is not None:
            #     print(self.columns)
            #     total_room_ix = self.columns.index(COLUMN_TOTAL_ROOMS)
            #     population_ix = self.columns.index(COLUMN_POPULATION)
            #     households_ix = self.columns.index(COLUMN_HOUSEHOLDS)
            #     total_bedrooms_ix = self.columns.index(COLUMN_TOTAL_BEDROOM)

            self.add_bedrooms_per_room = add_bedrooms_per_room
            self.total_room_ix = total_room_ix
            self.population_ix = population_ix
            self.households_ix = households_ix
            self.total_bedrooms_ix = total_bedrooms_ix
        except Exception as e:
            raise e

    def fit(self,x,y=None):
        return self
    
    def transform(self,x,y=None):
        try:
            room_per_household = x[:,self.total_room_ix] / x[:,self.households_ix]
            population_per_household = x[:,self.population_ix]/x[:,self.households_ix]
            if self.add_bedrooms_per_room:
                bedrooms_per_room = x[:,self.total_bedrooms_ix]/x[:,self.total_room_ix]
                generated_feature = np.c_[x,room_per_household,population_per_household,bedrooms_per_room]
            else:
                generated_feature = np.c_[x,room_per_household,population_per_household]
            
            return generated_feature

        except Exception as e:
            raise e


class DataTransformation:

    def __init__(self,data_transformation_config:DataTransformationConfig,
                data_ingestion_artifact:DataIngestionArtifact,
                data_validation_artifact:DataValidationArtifact) -> None:
        try:
            logging.info(f"DataTransformation Started {'='*20}")
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_artifact = data_validation_artifact
            
        except Exception as e:
            raise HousingException(e,sys) from e
    

    def get_data_transformer_object(self)->ColumnTransformer:
        try:
            schema_file_path = self.data_validation_artifact.schema_file_path

            dataset_schema = get_yaml_file(schema_file_path)

            numerical_columns = dataset_schema[NUMERICAL_COLUMN_KEY]
            categorical_columns = dataset_schema[CATEGORICAL_COLUMN]

            logging.info("creating Pipelines for datatranforming purposes :-)")
            num_pipeline = Pipeline(steps=[('imputer',SimpleImputer(strategy="median")),
                                ("feature_generator",FeatureGenerator(
                                add_bedrooms_per_room = self.data_transformation_config.is_add_bedroom)),
                                ('scaling',StandardScaler())])

            cat_pipeline = Pipeline(steps=[('imputer',SimpleImputer(strategy="most_frequent")),
                                ('OnehotEncoder',OneHotEncoder()),
                                ('scaling',StandardScaler(with_mean=False))])
            
            logging.info(f"categorical columns: {categorical_columns}")
            logging.info(f"numerical columns are : {numerical_columns}")

            preprocessing = ColumnTransformer([('num_pipeline',num_pipeline,numerical_columns),
                                    ('cat_pipeline',cat_pipeline,categorical_columns)])

            return preprocessing

        except Exception as e:
            raise HousingException(e,sys) from e


    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info(f"{'='*20} initiating data transformation {'='*20}")
            preprocessing_obj  = self.get_data_transformer_object()

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            schema_file_path = self.data_validation_artifact.schema_file_path
            
            train_df = load_data(train_file_path,schema_file_path)
            
            test_df = load_data(test_file_path,schema_file_path)

            schema = get_yaml_file(schema_file_path)

            target_column_name = schema[TARGET_COLUMN_KEY]

            input_feature_train = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train = train_df[target_column_name]

            input_feature_test = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test = test_df[target_column_name]

            input_feature_train_array = preprocessing_obj.fit_transform(input_feature_train)
            input_feature_test_array = preprocessing_obj.transform(input_feature_test)

            train_arr = np.c_[input_feature_train_array,np.array(target_feature_train)]
            test_arr = np.c_[input_feature_test_array,np.array(target_feature_test)]

            transformed_train_dir = self.data_transformation_config.transformed_train_dataset_dir
            transformed_test_dir = self.data_transformation_config.transformed_test_dataset_dir

            train_file_name = os.path.basename(train_file_path).replace(".csv",".npz")
            test_file_name = os.path.basename(test_file_path).replace(".csv",".npz")

            transformed_train_file_path = os.path.join(transformed_train_dir,train_file_name)
            transformed_test_file_path = os.path.join(transformed_test_dir,test_file_name)

            save_numpy_array_data(file_path=transformed_train_file_path,array=train_arr)
            save_numpy_array_data(file_path=transformed_test_file_path,array=test_arr)

            preprocessing_obj_file_path = self.data_transformation_config.pickle_file_of_data_transformation_object

            save_object(file_path=preprocessing_obj_file_path,obj = preprocessing_obj)

            data_transformation_artifact = DataTransformationArtifact(True,"data transformation successfull",transformed_test_file_path,
            transformed_test_file_path,preprocessing_obj_file_path)

            logging.info(f"Data Transformation Artifact : {data_transformation_artifact}")
            return data_transformation_artifact


        except Exception as e:
            raise HousingException(e,sys) from e
















