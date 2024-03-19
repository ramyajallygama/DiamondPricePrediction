import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split


from dataclasses import dataclass

#Initialize the Data Ingestion Configuration
@dataclass
class DataIngestionConfig:
     train_data_path:str=os.path.join('artifacts','train.csv')
     test_data_path:str=os.path.join('artifacts','test.csv')
     raw_data_path:str=os.path.join('artifacts','raw_data.csv')

#Create Data Ingestion class
class DataIngestion:
     def __init__(self):
          self.ingestion_config=DataIngestionConfig()
    
     def initiate_data_ingestion(self):
          logging.info('This is the start of data ingestion menthod')
        
          try:
              df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
              logging.info('Dataset read as pandas dataframe')
              os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
              df.to_csv(self.ingestion_config.raw_data_path,index=False)
              #Train test split
              train_set,test_set=train_test_split(data=df,test_size=0.30,random_state=42)
              df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
              df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

              logging.info('test train data created and ingetsion completed')

              return (
                   self.ingestion_config.test_data_path,
                   self.ingestion_config.train_data_path
              )


          except Exception as e:
             logging.info('exception raised inside data ingestion')
             raise CustomException(e,sys)
    


     
        
