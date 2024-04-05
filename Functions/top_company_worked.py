import pandas as pd
import numpy as np
import seaborn as sns

class TopCompanyAnalyze:
    def __init__(self, dataframe: pd.DataFrame):
        '''
        Initializes the TopCompanyAnalyze object by loading a dataset.
        :param dataframe: A DataFrame of Data
        '''
        self.df = dataframe




if __name__ == "__main__":
    analyze = TopCompanyAnalyze(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))

    print(analyze.df[''])
