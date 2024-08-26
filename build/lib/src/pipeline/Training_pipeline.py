import os
import sys
from src.exception import CustomException
import pandas as pd
from src.component.data_ingestion import DataIngestion
from src.component.Data_Transformation import DataTransformation
from src.component.Model_Trainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)

    data_transformation=DataTransformation()

    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)

