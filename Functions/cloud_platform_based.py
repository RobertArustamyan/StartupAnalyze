import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from Functions.company_industry import IndustryAnalyzing


class CloudPlatformBased:
    '''
    A class for analyzing Cloud or Platform Based bussiness companies.
    '''

    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the CloudPlatformBased  object by loading a dataset.
        :param df: A DataFrame of Data
        '''
        self.df = df

    @property
    def _no_info_industry(self):
        '''
        Returns unique industries with 'No Info' category for 'Cloud or platform based serive/product?'s column.
        '''
        industry_of_no_info = self.df[self.df['Cloud or platform based serive/product?'] == 'No Info'][
            'Industry of company']
        unique_industries = industry_of_no_info.unique()
        return unique_industries

    def _matching_values_from_industry(self, industry: str) -> str:
        '''
        Matches industries to their corresponding cloud or platform categories.
        :param industry: The industry of the company
        :return: The cloud or platform category
        '''
        # This values are generated with CHATGPT in order to replace np.nan values!!
        industry_categories = {
            'security': 'Cloud',
            'Advertising|Marketing': 'Platform',
            'Network / Hosting / Infrastructure|Marketing': 'Platform',
            'E-Commerce': 'Both',
            'Transportation': 'None',
            'Entertainment|Media': 'Platform'
        }
        return industry_categories[industry]

    def _filling_na_values(self) -> None:
        '''
        Fills np.nan values based on industry of company
        '''
        self.df['Cloud or platform based serive/product?'] = (
            self.df['Cloud or platform based serive/product?'].replace('No Info', np.nan))
        self.df['Cloud or platform based serive/product?'] = (
            self.df['Cloud or platform based serive/product?'].replace('cloud', 'Cloud'))
        self.df['Cloud or platform based serive/product?'] = (
            self.df['Cloud or platform based serive/product?'].replace('none', 'None'))

        na_indices = self.df[self.df['Cloud or platform based serive/product?'].isna()].index
        for index in na_indices:
            industry = self.df.loc[index, 'Industry of company']
            cl_pt_info = self._matching_values_from_industry(industry)
            self.df.loc[index, 'Cloud or platform based serive/product?'] = cl_pt_info

    def plot_dependence(self) -> None:
        '''
        Plots the distribution of Cloud or Platform Based Services/Products.
        '''
        self._filling_na_values()

        plt.figure(figsize=(8, 6))
        sns.countplot(data=self.df, x='Cloud or platform based serive/product?', hue='Dependent-Company Status')
        plt.title('Distribution of Cloud or Platform Based Services/Products')
        plt.xlabel('Service/Product/None/Both')
        plt.ylabel('Count')
        plt.show()


if __name__ == "__main__":
    a = IndustryAnalyzing(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    a.industry_success_distribution(plot=False)

    b = CloudPlatformBased(a.df)
    b.plot_dependence()
