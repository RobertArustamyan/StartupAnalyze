import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from Functions.company_industry import IndustryAnalyzing

pd.set_option('future.no_silent_downcasting', True)

class ConsumerDataFocus:
    '''
    A class for analyzing Consumer data focus of companies.
    '''
    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the ConsumerDataFocus object by loading a dataset.
        :param df: A DataFrame of Data
        '''
        self.df = df

    @property
    def _no_info_industry(self):
        '''
        Returns unique industries with 'No Info' category for 'Focus on consumer data?' column.
        '''
        industry_of_no_info = self.df[self.df['Focus on consumer data?'] == 'No Info']['Industry of company']
        unique_industries = industry_of_no_info.unique()
        return unique_industries

    def _getting_cosumer_info_for_missings(self, industry: str) -> str:
        '''
        Returns (Yes or No) based on the industry.
        :param industry: The industry of the company
        :return: industry_dict value
        '''

        # This list is generated using CHAT GPT
        industry_dict = {
            'insurance': 'No',
            'Email|Marketing': 'Yes',
            'Mobile': 'Yes',
            'Advertising|Analytics': 'Yes',
            'E-Commerce': 'Yes',
            'Transportation': 'Yes'
        }
        return industry_dict[industry]

    def _filling_na_values(self):
        '''
        Fills missing values in 'Focus on consumer data?' column based on the industry
        '''
        self.df['Focus on consumer data?'] = self.df['Focus on consumer data?'].replace('No Info', np.nan)
        na_indices = self.df[self.df['Focus on consumer data?'].isna()].index
        for index in na_indices:
            industry = self.df.loc[index, 'Industry of company']
            consumer_info = self._getting_cosumer_info_for_missings(industry)
            self.df.loc[index, 'Focus on consumer data?'] = consumer_info
        self.df['Focus on consumer data?'] = self.df['Focus on consumer data?'].replace('Yes', True)
        self.df['Focus on consumer data?'] = self.df['Focus on consumer data?'].replace('No', False)

    def plot_success_dependence(self):
        '''
        Plots success dependence based on consumer data focus.
        '''
        self._filling_na_values()

        success_by_category = self.df.groupby('Focus on consumer data?')['Dependent-Company Status']. \
            apply(lambda x: (x == 'Success').mean()).reset_index()

        plt.figure(figsize=(8, 6))
        sns.barplot(data=success_by_category, x='Focus on consumer data?', y='Dependent-Company Status',
                    hue='Dependent-Company Status', palette='viridis', legend=False)
        plt.title('Success Rate by Consumer Data Focus')
        plt.xlabel('Focus on Consumer Data')
        plt.ylabel('Success Rate')
        plt.ylim(0, 1)
        plt.show()


if __name__ == "__main__":
    a = IndustryAnalyzing(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    a.industry_success_distribution()

    b = ConsumerDataFocus(a.df)
    b.plot_success_dependence()
