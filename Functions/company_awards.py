import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class CompanyAwards:
    '''
    A class for analyzing CompanyAwards data of companies.
    '''
    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the CompanyAwards object by loading a dataset.
        :param df: A DataFrame of Data
        '''
        self.df = df

    def _prepare_data(self):
        '''
        Prepares the data by replacing 'No Info' values in the 'Company awards' column with the most frequent value.
        '''
        # Before filling NONE values were 90.78% and 74.02%
        # After this operation, values are 90.79% and 74.03%, so filling with the most frequent value was the correct decision
        self.df['Company awards'] = self.df['Company awards'].replace('No Info', np.nan)
        most_frequent_award = self.df['Company awards'].mode()[0]
        self.df['Company awards'] = self.df['Company awards'].fillna(most_frequent_award)

    def award_dependence(self):
        '''
        Calculates and prints the percentage of successful companies with and without awards.
        '''
        awards_yes_success = len(
            self.df[(self.df['Company awards'] == 'Yes') & (self.df['Dependent-Company Status'] == 'Success')])
        awards_yes_total = len(self.df[self.df['Company awards'] == 'Yes'])
        awards_no_success = len(
            self.df[(self.df['Company awards'] == 'No') & (self.df['Dependent-Company Status'] == 'Success')])
        awards_no_total = len(self.df[self.df['Company awards'] == 'No'])

        percent_awards_yes_success = (awards_yes_success / awards_yes_total) * 100 if awards_yes_total > 0 else 0
        percent_awards_no_success = (awards_no_success / awards_no_total) * 100 if awards_no_total > 0 else 0

        print("Percentage of successful companies with awards: {:.2f}%".format(percent_awards_yes_success))
        print("Percentage of successful companies without awards: {:.2f}%".format(percent_awards_no_success))


