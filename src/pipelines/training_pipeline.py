import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
import pandas as pd
from src.components.data_transformation import DataTransformation


if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
    train_arr,test_arr,obkj_path=data_transformation=DataTransformation.initiate_data_transformation(train_data_path,test_data_path)

