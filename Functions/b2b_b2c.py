import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class B2bOrB2cAnalytics:
    '''
    A class for analyzing B2B or B2C success dependence.
    '''

    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the B2bOrB2cAnalytics object by loading a dataset.
        :param df: A DataFrame of Data
        '''
        self.df = df

    def __droping_na(self)->None:
        '''
        Function for testing (In analysis.ipynb there is no need to clear data because it is already cleaned)
        '''
        self.df['B2C or B2B venture?'] = self.df['B2C or B2B venture?'].replace('No Info', np.nan)
        self.df = self.df.dropna(subset=['B2C or B2B venture?'])

    def success_dependence(self):
        '''
        Calculates the success percentages for B2B and B2C ventures.
        '''
        # Commented func because it is used only in test mode!
        #self.__droping_na()

        b2c_data = self.df[self.df['B2C or B2B venture?'] == 'B2C']
        b2c_data_success = len(b2c_data[b2c_data['Dependent-Company Status'] == 'Success'])
        all_b2c = len(b2c_data)

        b2b_data = self.df[self.df['B2C or B2B venture?'] == 'B2B']
        b2b_data_success = len(b2b_data[b2b_data['Dependent-Company Status'] == 'Success'])
        all_b2b = len(b2b_data)

        print('Success percentage for B2C ventures:', b2c_data_success / all_b2c * 100)
        print('Success percentage for B2B ventures:', b2b_data_success / all_b2b * 100)


if __name__ == "__main__":
    analyse = B2bOrB2cAnalytics(pd.read_csv(r'C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv', encoding='latin-1'))
    analyse.plot_dependence()