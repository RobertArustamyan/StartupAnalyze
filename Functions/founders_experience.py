import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('future.no_silent_downcasting', True)


class FoundersExperience:
    '''
    A class for analyzing Founders-related data of companies.
    '''
    def __init__(self, df: pd.DataFrame):
        '''
        Initializes the FoundersExperience object by loading a dataset.
        :param dataframe: A DataFrame of Data
        '''
        self.df = df

    def _prepare_data(self) -> None:
        '''
        Prepares data for future analysis by replacing 'Yes' with 1 and 'No' with 0
        '''
        experience_columns = [
            'Have been part of startups in the past?',
            'Have been part of successful startups in the past?',
            'Was he or she partner in Big 5 consulting?'
        ]
        replacements = {'Yes': 1, 'No': 0, 'No Info': np.nan}
        self.df[experience_columns] = self.df[experience_columns].replace(replacements)

        # Calculate proportion of 'Yes' / ALL
        proportions = self.df[experience_columns].apply(lambda col: col.value_counts(normalize=True).get(1, 0))

        # Replaces np.nan based on the proportion
        for col in proportions.index:
            if proportions[col] > 0.5:
                self.df[col] = self.df[col].fillna(1)
            else:
                self.df[col] = self.df[col].fillna(0)

    def _create_experience_column(self):
        '''
        Creating 'Founder Experience' column based on 3 coulumns of 'for founders & cofounders'
        '''
        experience_columns = [
            'Have been part of startups in the past?',
            'Have been part of successful startups in the past?',
            'Was he or she partner in Big 5 consulting?'
        ]
        self.df['Founder Experience'] = self.df[experience_columns].sum(axis=1)

    def plot_founder_experience_vs_success(self):
        self._prepare_data()
        self._create_experience_column()

        success_for_zero_experience = len(
            self.df[(self.df['Dependent-Company Status'] == 'Success') & (self.df['Founder Experience'] == 0)])
        total_for_zero_experience = len(self.df[(self.df['Founder Experience'] == 0)])

        success_for_one_experience = len(
            self.df[(self.df['Dependent-Company Status'] == 'Success') & (self.df['Founder Experience'] == 1)])
        total_for_one_experience = len(self.df[(self.df['Founder Experience'] == 1)])

        success_for_two_experience = len(
            self.df[(self.df['Dependent-Company Status'] == 'Success') & (self.df['Founder Experience'] == 2)])
        total_for_two_experience = len(self.df[(self.df['Founder Experience'] == 2)])

        success_for_three_experience = len(
            self.df[(self.df['Dependent-Company Status'] == 'Success') & (self.df['Founder Experience'] == 3)])
        total_for_three_experience = len(self.df[(self.df['Founder Experience'] == 3)])

        sns.countplot(data=self.df, x='Founder Experience', hue='Dependent-Company Status')
        plt.xlabel('Founder Experience')
        plt.ylabel('Count')
        plt.title('Founder Experience vs. Company Success/Failure')
        plt.legend(title='Company Status')
        plt.show()

        percent_success_zero_experience = (success_for_zero_experience / total_for_zero_experience) * 100
        percent_success_one_experience = (success_for_one_experience / total_for_one_experience) * 100
        percent_success_two_experience = (success_for_two_experience / total_for_two_experience) * 100
        percent_success_three_experience = (success_for_three_experience / total_for_three_experience) * 100

        print("Success Rate for Founder Experience 0: {:.2f}%".format(percent_success_zero_experience))
        print("Success Rate for Founder Experience 1: {:.2f}%".format(percent_success_one_experience))
        print("Success Rate for Founder Experience 2: {:.2f}%".format(percent_success_two_experience))
        print("Success Rate for Founder Experience 3: {:.2f}%".format(percent_success_three_experience))


if __name__ == "__main__":
    Founderexp = FoundersExperience(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    Founderexp.plot_founder_experience_vs_success()
