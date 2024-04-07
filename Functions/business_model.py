import numpy as np
import pandas as pd


class BusinessModel:
    '''
    A class for analyzing Business model of companies.
    '''

    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the BusinessModel object by loading a dataset.
        :param df: A DataFrame of Data
        '''
        self.df = df

    def _prepare_data(self) -> None:
        '''
        Preparing data by replaceing 'No Info' values with np.nan
        '''
        self.df['Linear or Non-linear business model'] = self.df['Linear or Non-linear business model'].replace(
            'No Info', np.nan)

    def _filling_na_from_sub_advaned(self) -> None:
        '''
        Fill missing values in the 'Linear or Non-linear business model' column based on the majority class
        of 'Linear' or 'Non-Linear' within each group defined by combinations of 'Subscription based business'
        and 'Advanced Business'.

        This function calculates the mode ('Linear' or 'Non-Linear') for each group defined by combinations of
        'Subscription based business' and 'Advanced Business'. Then it fills the missing values in the
        'Linear or Non-linear business model' column based on the calculated mode for each group.
        '''
        self._prepare_data()

        sub_advanced = self.df[
            (self.df['Subscription based business'] == True) & (self.df['Advanced Business'] == True)]
        sub_nonadvanced = self.df[
            (self.df['Subscription based business'] == True) & (self.df['Advanced Business'] == False)]
        nonsub_advanced = self.df[
            (self.df['Subscription based business'] == False) & (self.df['Advanced Business'] == True)]
        nonsub_nonadvanced = self.df[
            (self.df['Subscription based business'] == False) & (self.df['Advanced Business'] == False)]

        # Finding values for each case
        if len(sub_advanced[sub_advanced['Linear or Non-linear business model'] == 'Linear']) > len(
                sub_advanced[sub_advanced['Linear or Non-linear business model'] == 'Non-Linear']):
            value_sub_advanced = 'Linear'
        else:
            value_sub_advanced = 'Non-Linear'

        if len(sub_nonadvanced[sub_nonadvanced['Linear or Non-linear business model'] == 'Linear']) > len(
                sub_nonadvanced[sub_nonadvanced['Linear or Non-linear business model'] == 'Non-Linear']):
            value_sub_nonadvanced = 'Linear'
        else:
            value_sub_nonadvanced = 'Non-Linear'

        if len(nonsub_advanced[nonsub_advanced['Linear or Non-linear business model'] == 'Linear']) > len(
                nonsub_advanced[nonsub_advanced['Linear or Non-linear business model'] == 'Non-Linear']):
            value_nonsub_advanced = 'Linear'
        else:
            value_nonsub_advanced = 'Non-Linear'

        if len(nonsub_nonadvanced[nonsub_nonadvanced['Linear or Non-linear business model'] == 'Linear']) > len(
                nonsub_nonadvanced[nonsub_nonadvanced['Linear or Non-linear business model'] == 'Non-Linear']):
            value_nonsub_nonadvanced = 'Linear'
        else:
            value_nonsub_nonadvanced = 'Non-Linear'

        # Filling np.nan values with values found in upper part
        self.df.loc[
            (self.df['Subscription based business'] == True) & (self.df['Advanced Business'] == True) & pd.isnull(
                self.df[
                    'Linear or Non-linear business model']), 'Linear or Non-linear business model'] = value_sub_advanced
        self.df.loc[
            (self.df['Subscription based business'] == True) & (self.df['Advanced Business'] == False) & pd.isnull(
                self.df[
                    'Linear or Non-linear business model']), 'Linear or Non-linear business model'] = value_sub_nonadvanced
        self.df.loc[
            (self.df['Subscription based business'] == False) & (self.df['Advanced Business'] == True) & pd.isnull(
                self.df[
                    'Linear or Non-linear business model']), 'Linear or Non-linear business model'] = value_nonsub_advanced
        self.df.loc[
            (self.df['Subscription based business'] == False) & (self.df['Advanced Business'] == False) & pd.isnull(
                self.df[
                    'Linear or Non-linear business model']), 'Linear or Non-linear business model'] = value_nonsub_nonadvanced

    def calculating_sucess_rate(self):
        '''
        Calculates and prints the success rate for companies with a linear business model and companies
        with a non-linear business model.
        :return:
        '''
        linear = self.df[self.df['Linear or Non-linear business model'] == 'Linear']
        non_linear = self.df[self.df['Linear or Non-linear business model'] == 'Non-Linear']

        linear_success_count = len(linear[linear['Dependent-Company Status'] == 'Success'])
        linear_all_count = len(linear)

        non_linear_success_count = len(non_linear[non_linear['Dependent-Company Status'] == 'Success'])
        non_linear_all_count = len(non_linear)

        print('Success rate for companies with a linear business model: {:.2f}%'.format(
            (linear_success_count / linear_all_count) * 100))
        print('Success rate for companies with a non-linear business model: {:.2f}%'.format(
            (non_linear_success_count / non_linear_all_count) * 100))


if __name__ == "__main__":
    model = BusinessModel(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    model._prepare_data()
