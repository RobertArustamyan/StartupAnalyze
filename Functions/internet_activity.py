import pprint

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from Functions.startup_age import AgeDataAnalyzing


class InternetActivity:
    '''
    A class for analyzing Internet activity of companies.
    '''

    def __init__(self, dataframe: pd.DataFrame):
        '''
        Initializes the InternetActivity object by loading a dataset.
        :param dataframe: A DataFrame of Data
        '''
        self.df = dataframe

    def _seperate_data(self) -> None:
        '''
        Seperates data to success and faild parts
        '''
        self.success_data = self.df[
            self.df['Dependent-Company Status'] == 'Success']  # Descriptive statistics for success companies
        self.failed_data = self.df[
            self.df['Dependent-Company Status'] == 'Failed']  # Descriptive statistics for failed companies

    def _filling_na_values(self) -> None:
        self.df[self.df['']]

    def analyze_internet_activity(self, plot=False):
        '''
        Analyzes the internet activity scores of success and failed companies
        :param plot:A flag indicating whether to plot the distribution of internet activity scores. Default is False
        :return:A tuple containing the descriptive statistics of internet activity scores for success and failed companies
               The tuple format is (success_stats, failed_stats), where each element is a Series containing descriptive statistics
        '''
        self._seperate_data()
        self._fill_na_with_stage_mean()
        success_stats = self.success_data['Internet Activity Score'].describe()
        failed_stats = self.failed_data['Internet Activity Score'].describe()
        if plot:
            # Plotin data using histplot
            plt.figure(figsize=(10, 6))
            sns.histplot(self.success_data['Internet Activity Score'], color='green', kde=True, label='Success')
            sns.histplot(self.failed_data['Internet Activity Score'], color='red', kde=True, label='Failed')

            plt.title('Distribution of Internet Activity Scores')
            plt.xlabel('Internet Activity Score')
            plt.ylabel('Frequency')
            plt.legend()
            plt.show()

        pprint.pprint(self._mean_value_by_stage)

        return success_stats, failed_stats

    @property
    def _mean_value_by_stage(self) -> dict:
        '''
        Computes the mean Internet activity score for each company stage and success/fail category.
        :return: A dictionary containing the mean Internet activity score for each category.
        '''
        mean_values = {}

        # Mean for Early Stage companies
        mean_early_success = \
            self.df[(self.df['Company Stage'] == 'Early Stage') & (self.df['Dependent-Company Status'] == 'Success')][
                'Internet Activity Score'].mean()
        mean_early_fail = \
            self.df[(self.df['Company Stage'] == 'Early Stage') & (self.df['Dependent-Company Status'] == 'Failed')][
                'Internet Activity Score'].mean()
        mean_values['Early Stage'] = {'Success': mean_early_success, 'Failed': mean_early_fail}

        # Mean for Established companies
        mean_established_success = \
            self.df[(self.df['Company Stage'] == 'Established') & (self.df['Dependent-Company Status'] == 'Success')][
                'Internet Activity Score'].mean()
        mean_established_fail = \
            self.df[(self.df['Company Stage'] == 'Established') & (self.df['Dependent-Company Status'] == 'Failed')][
                'Internet Activity Score'].mean()
        mean_values['Established'] = {'Success': mean_established_success, 'Failed': mean_established_fail}

        # Mean for Mature companies
        mean_mature_success = \
            self.df[(self.df['Company Stage'] == 'Mature') & (self.df['Dependent-Company Status'] == 'Success')][
                'Internet Activity Score'].mean()
        mean_mature_fail = \
            self.df[(self.df['Company Stage'] == 'Mature') & (self.df['Dependent-Company Status'] == 'Failed')][
                'Internet Activity Score'].mean()
        mean_values['Mature'] = {'Success': mean_mature_success, 'Failed': mean_mature_fail}

        return mean_values

    def _fill_na_with_stage_mean(self):
        '''
        Fills the missing values in Internet activiyty based on Success or Fail of company and its stage.
        '''
        mean_values = self._mean_value_by_stage
        for stage in mean_values.keys():
            mean_success = mean_values[stage]['Success']  # Values from mean_values dict
            mean_fail = mean_values[stage]['Failed']  # Values from mean_values dict
            self.df.loc[(self.df['Company Stage'] == stage) & (self.df['Dependent-Company Status'] == 'Success') & (
                self.df['Internet Activity Score'].isna()), 'Internet Activity Score'] = mean_success
            self.df.loc[(self.df['Company Stage'] == stage) & (self.df['Dependent-Company Status'] == 'Failed') & (
                self.df['Internet Activity Score'].isna()), 'Internet Activity Score'] = mean_fail


if __name__ == "__main__":
    AgeAnalyze = AgeDataAnalyzing(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    AgeAnalyze.filling_age_missing_values()

    internet = InternetActivity(AgeAnalyze.df)
    internet.fill_na_with_stage_mean()
