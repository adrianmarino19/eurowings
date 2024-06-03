import pandas as pd
import numpy as np

class ModelPreProcessing:
    def __init__(self):
        file = "SkyScannerRedirrect_DataScienceBootCamp.csv"
        self.df = pd.read_csv(file)
        #Remove all the "calculator" columns that are now not needed (revenues, and amount of people col)


    def num_scaling(self):
        numeric_columns = self.df.dtypes[(self.df.dtypes == "int64") | (self.df.dtypes == "float64")].index


    def categorical_encoding(self):
        pass
