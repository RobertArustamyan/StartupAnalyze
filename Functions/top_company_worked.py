import numpy as np
import pandas as pd


class TopCompanyAnalyze:
    def __init__(self, dataframe: pd.DataFrame):
        '''
        Initializes the TopCompanyAnalyze object by loading a dataset.
        :param dataframe: A DataFrame of Data
        '''
        self.df = dataframe

    def _preparing_data(self):
        self.df['Worked in top companies'] = self.df['Worked in top companies'].replace('No Info', np.nan)
        self.df['Worked in top companies'] = self.df['Worked in top companies'].replace('Yes', True)
        self.df['Worked in top companies'] = self.df['Worked in top companies'].replace('No', False)
        self.df.dropna(subset=['Worked in top companies'], inplace=True)

    def analyze_data(self):
        self._preparing_data()

        success_in_big_company = len(self.df[
                                         (self.df['Worked in top companies'] == True) & (
                                                 self.df['Dependent-Company Status'] == 'Success')])
        total_in_big_company = len(self.df[
                                       self.df['Worked in top companies'] == True])

        success_without_big_company = len(self.df[
                                              (self.df['Worked in top companies'] == False) & (
                                                      self.df['Dependent-Company Status'] == 'Success')])
        total_without_big_company = len(self.df[
                                            self.df['Worked in top companies'] == False])

        print("Success rate in a top company -", success_in_big_company / total_in_big_company * 100)
        print("Success rate out of a top comapny -", success_without_big_company / total_without_big_company * 100)


if __name__ == "__main__":
    analyze = TopCompanyAnalyze(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))

    analyze.analyze_data()
