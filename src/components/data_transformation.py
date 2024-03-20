from sklearn.impute import SimpleImputer #For Handling missing values
from sklearn.preprocessing import OrdinalEncoder #For ccategorical columns encoding
from sklearn.preprocessing import StandardScaler #Feature scaling 

#Pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import numpy as np
import pandas as pd

from src.exception import CustomException
import sys,os
from src.utils import save_object
from dataclasses_1 import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation_obj(self):
        try:
           #Divide Categorical and Numerical columns
            categorical_cols=['cut','color','clarity']
            numerical_cols=['carats','depth','table','x','y','z']

            #Define custom ranking for ordinal varaibles cut,color,clarity
            cut_rank=['Fair','Good','Very Good','Premium','Ideal']
            color_rank=['D','E','F','G','H','I']
            clarity_rank=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            #Categorical pipeline creation
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinal encoder',OrdinalEncoder(categories=[cut_rank,color_rank,clarity_rank])),
                    ('scalar',StandardScaler())          
            ]
            #Numerical pipeline creation
            )
            num_pipeline=Pipeline(
                steps=[('imputer',SimpleImputer(strategy='median')),
                       ('scalar',StandardScaler())

                ]
            )
            #Combine categorical and numerical pipeline
            preprocessor=ColumnTransformer([('num_pipeline',num_pipeline,numerical_cols),
                                            ('cat_pipeline',cat_pipeline,categorical_cols)
                                            ]

            )
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_data_path,test_data_path):
            try:
                train_df=pd.read_csv(train_data_path)
                test_df=pd.read_csv(test_data_path)

                preprocessing_obj=self.get_data_transformation_obj()
                target_col=['price']
                drop_col=['target_col','id']
                
                 #  Train data
                
                input_feature_train_df=train_df.drop(columns=drop_col,axis=1)
                target_feature_train_df=train_df[target_col]

                #Test Data
                input_feature_test_df=test_df.drop(columns=drop_col,axis=1)
                target_feature_test_df=test_df[target_col]

                #Data Transformation
                input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_test_df)
                input_feature_test_arr=preprocessing_obj.transform(target_feature_test_df)

                train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
                test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

                save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                            obj=preprocessing_obj)
                
                return(
                     train_arr,
                     test_arr,
                     self.data_transformation_config.preprocessor_obj_file_path
                     
                )



                
            except Exception as e:
                 raise CustomException(e,sys)
        








