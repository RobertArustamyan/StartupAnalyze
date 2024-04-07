import numpy as np
import pandas as pd
from Functions.company_industry import IndustryAnalyzing


class AdvancedAnalyticBusiness:
    '''
    A class for analyzing 'Machine Learning', 'Predictive Analytics', 'Speech analytics' and 'Big Data'  methods using companies.
    '''

    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the AdvancedAnalyticBusiness object by loading a dataset.
        :param df: A DataFrame of Data
        '''
        self.df = df

    def _preparing_data(self):
        '''
        Prepares the data by replacing 'No Info', 'Yes', and 'No' values with appropriate boolean values,
        and removes rows with missing values in the 'Machine Learning based business' column.
        '''
        self.df['Machine Learning based business'] = self.df['Machine Learning based business'].replace('No Info',
                                                                                                        np.nan)
        self.df['Machine Learning based business'] = self.df['Machine Learning based business'].replace('Yes', True)
        self.df['Machine Learning based business'] = self.df['Machine Learning based business'].replace('No', False)

        self.df['Predictive Analytics business'] = self.df['Predictive Analytics business'].replace('Yes', True)
        self.df['Predictive Analytics business'] = self.df['Predictive Analytics business'].replace('No', False)

        self.df['Speech analytics business'] = self.df['Speech analytics business'].replace('Yes', True)
        self.df['Speech analytics business'] = self.df['Speech analytics business'].replace('No', False)

        self.df['Big Data Business'] = self.df['Big Data Business'].replace('Yes', True)
        self.df['Big Data Business'] = self.df['Big Data Business'].replace('No', False)

        self.df.dropna(subset=['Machine Learning based business'], inplace=True)

    def _new_advanced_business_column(self, treshold=1):
        '''
        Create a new column 'Advanced_Business' based on the presence of various advanced analytics features.

        :param threshold: The threshold value for considering a business as advanced.
        :return: None
        '''

        self.df['Advanced Business'] = 0

        self.df['Advanced Business'] += self.df['Machine Learning based business'].astype(int)
        self.df['Advanced Business'] += self.df['Predictive Analytics business'].astype(int)
        self.df['Advanced Business'] += self.df['Speech analytics business'].astype(int)
        self.df['Advanced Business'] += self.df['Big Data Business'].astype(int)

        self.df['Advanced Business'] = self.df['Advanced Business'] >= treshold
    def calculate_ml_percentage(self):
        '''
        Calculates and prints the success percentage for companies with and without Machine Learning based business.
        '''

        self._preparing_data()

        self._new_advanced_business_column()

        ml_true_df = self.df[self.df['Machine Learning based business'] == True]
        success_count_with_using = len(ml_true_df[ml_true_df['Dependent-Company Status'] == 'Success'])
        all_count_with_using = len(ml_true_df)
        success_percentage_with_using = success_count_with_using / all_count_with_using * 100

        ml_false_df = self.df[self.df['Machine Learning based business'] == False]
        success_count_without_using = len(ml_false_df[ml_false_df['Dependent-Company Status'] == 'Success'])
        all_count_without_using = len(ml_false_df)
        success_percentage_without_using = success_count_without_using / all_count_without_using * 100

        print('Success percentage for companies with Machine Learning based business: {:.2f}%'.format(
            success_percentage_with_using))
        print('Success percentage for companies without Machine Learning based business: {:.2f}%\n'.format(
            success_percentage_without_using))

    def calculate_pred_percentage(self):
        '''
        Calculates and prints the success percentage for companies with and without Predictive Analytics business.
        '''
        self._preparing_data()

        pred_true_df = self.df[self.df['Predictive Analytics business'] == True]
        success_count_with_using = len(pred_true_df[pred_true_df['Dependent-Company Status'] == 'Success'])
        all_count_with_using = len(pred_true_df)
        success_percentage_with_using = success_count_with_using / all_count_with_using * 100

        pred_false_df = self.df[self.df['Predictive Analytics business'] == False]
        success_count_without_using = len(pred_false_df[pred_false_df['Dependent-Company Status'] == 'Success'])
        all_count_without_using = len(pred_false_df)
        success_percentage_without_using = success_count_without_using / all_count_without_using * 100

        print('Success percentage for companies with Predictive Analytics business: {:.2f}%'.format(
            success_percentage_with_using))
        print('Success percentage for companies without Predictive Analytics business: {:.2f}%\n'.format(
            success_percentage_without_using))

    def calculate_speech_percentage(self):
        '''
        Calculates and prints the success percentage for companies with and without Speech analytics business.
        '''
        self._preparing_data()

        speech_true_df = self.df[self.df['Speech analytics business'] == True]
        success_count_with_using = len(speech_true_df[speech_true_df['Dependent-Company Status'] == 'Success'])
        all_count_with_using = len(speech_true_df)
        success_percentage_with_using = success_count_with_using / all_count_with_using * 100

        speech_false_df = self.df[self.df['Speech analytics business'] == False]
        success_count_without_using = len(speech_false_df[speech_false_df['Dependent-Company Status'] == 'Success'])
        all_count_without_using = len(speech_false_df)
        success_percentage_without_using = success_count_without_using / all_count_without_using * 100

        print('Success percentage for companies with Speech analytics business: {:.2f}%'.format(
            success_percentage_with_using))
        print('Success percentage for companies without Speech analytics business: {:.2f}%\n'.format(
            success_percentage_without_using))

    def calculate_bigd_percentage(self):
        '''
        Calculates and prints the success percentage for companies with and without Big Data business.
        '''
        self._preparing_data()

        pred_true_df = self.df[self.df['Big Data Business'] == True]
        success_count_with_using = len(pred_true_df[pred_true_df['Dependent-Company Status'] == 'Success'])
        all_count_with_using = len(pred_true_df)
        success_percentage_with_using = success_count_with_using / all_count_with_using * 100

        pred_false_df = self.df[self.df['Big Data Business'] == False]
        success_count_without_using = len(pred_false_df[pred_false_df['Dependent-Company Status'] == 'Success'])
        all_count_without_using = len(pred_false_df)
        success_percentage_without_using = success_count_without_using / all_count_without_using * 100

        print('Success percentage for companies with Big Data Business: {:.2f}%'.format(
            success_percentage_with_using))
        print('Success percentage for companies without Big Data Business: {:.2f}%\n'.format(
            success_percentage_without_using))

    def full_statistic(self):
        '''
        Calculates and prints the success percentage for companies with and without each advanced analytics feature.
        '''
        self.calculate_ml_percentage()
        self.calculate_pred_percentage()
        self.calculate_speech_percentage()
        self.calculate_bigd_percentage()

