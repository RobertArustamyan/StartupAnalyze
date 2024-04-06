import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from Functions.company_industry import IndustryAnalyzing

class ProductService:
    '''
    A class for analyzing ProductService data of companies.
    '''
    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the ProductService object by loading a dataset.
        :param dataframe: A DataFrame of Data
        '''
        self.df = df

    @property
    def _no_info_industry(self):
        industry_of_no_info = self.df[self.df['Product or service company?'] == 'No Info']['Industry of company']
        unique_industries = industry_of_no_info.unique()
        return unique_industries

    def _getting_pr_sv_info_for_missings(self, industry):
        industry_dict = {
            'analytics': 'Service',
            'Advertising|Marketing': 'Both',
            'hospitality': 'Service',
            'government': 'Service',
            'Advertising|Analytics': 'Both',
            'E-Commerce': 'Product',
            'Transportation': 'Service',
            'Entertainment|Media': 'Both'
        }
        return industry_dict[industry]

    def _filling_na_values(self):
        self.df['Product or service company?'] = self.df['Product or service company?'].replace('No Info', np.nan)
        na_indices = self.df[self.df['Product or service company?'].isna()].index
        for index in na_indices:
            industry = self.df.loc[index, 'Industry of company']
            pr_sv_info = self._getting_pr_sv_info_for_missings(industry)
            self.df.loc[index, 'Product or service company?'] = pr_sv_info

    def plot_success_by_category(self):
        self._filling_na_values()

        success_by_category = self.df.groupby('Product or service company?')['Dependent-Company Status']. \
            apply(lambda x: (x == 'Success').mean()).reset_index()

        plt.figure(figsize=(8, 6))
        sns.barplot(data=success_by_category, x='Product or service company?', y='Dependent-Company Status',
                    hue='Dependent-Company Status', palette='viridis', legend=False)
        plt.title('Success Rate by Company Category')
        plt.xlabel('Company Category')
        plt.ylabel('Success Rate')
        plt.ylim(0, 1)
        plt.show()


if __name__ == "__main__":
    a = IndustryAnalyzing(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    a.industry_success_distribution()

    prd = ProductService(a.df)
    prd.plot_success_by_category()

