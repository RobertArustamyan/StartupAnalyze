import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from Functions.company_industry import IndustryAnalyzing

pd.set_option('future.no_silent_downcasting', True)


class SubscriptionBased:
    '''
    A class for analyzing Subscription Based bussiness companies.
    '''

    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the SubscriptionBased object by loading a dataset.
        :param df: A DataFrame of Data
        '''
        self.df = df

    @property
    def _no_info_industry(self):
        '''
        Returns unique industries with 'No Info' category for 'Subscription based business's column.
        '''
        industry_of_no_info = self.df[self.df['Subscription based business'] == 'No Info']['Industry of company']
        unique_industries = industry_of_no_info.unique()
        return unique_industries

    def _filling_na_values(self):
        '''
        Fills missing values in 'Subscription based business' column
        '''
        #All industries from self._no_info_industry are not based on subscription so it is replace with False value

        self.df['Subscription based business'] = self.df['Subscription based business'].replace('No Info', False)
        self.df['Subscription based business'] = self.df['Subscription based business'].replace('Yes', True)
        self.df['Subscription based business'] = self.df['Subscription based business'].replace('No', False)

    def plot_subscription_based(self):
        '''
        Plots a countplot to visualize differences based on whether the business is subscription-based or not.
        '''
        self._filling_na_values()

        plt.figure(figsize=(8,6))
        sns.countplot(data=self.df, x='Subscription based business', hue='Dependent-Company Status')
        plt.title('Success/Failure Distribution based on Subscription Based Business')
        plt.ylabel('Count')
        plt.legend(title='Company Status')
        plt.show()

if __name__ == "__main__":
    a = IndustryAnalyzing(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    a.industry_success_distribution()

    b = SubscriptionBased(a.df)
    b.plot_subscription_based()
