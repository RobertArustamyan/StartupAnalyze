from typing import List
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class AgeDataAnalyzing:
    '''
    A class for analyzing age-related data of companies.
    '''

    def __init__(self):
        """
        Initializes the AgeDataAnalyzing object by loading a dataset containing company age information.
        """
        self.df = pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1')

    @property
    def columns(self) -> List[str]:
        '''
        Returns a list of column names present in the dataset.
        :return:List[str]: A list of column names.
        '''
        return self.df.columns.tolist()

    def _changing_column_type(self) -> None:
        '''
        Changes the data type of the 'Age of company in years' column to numeric
        '''
        self.df['Age of company in years'] = pd.to_numeric(self.df['Age of company in years'], errors='coerce')

    def company_age_boxplot(self) -> None:
        '''
        Generates a boxplot to visualize the distribution of company ages based on the success status of companies
        '''
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='Dependent-Company Status', y='Age of company in years',
                    data=self.df[self.df['Age of company in years'] >= 0])
        plt.title('Distribution of Company Age by Success Status')
        plt.xlabel('Success Status')
        plt.ylabel('Age of company in years')

        plt.show()

    def _adding_company_stage(self) -> None:
        '''
        Adds new column named 'Early Stage' to the df based on the age of companies.
        '''

        def categorize(age):
            if age < 5:
                return 'Early Stage'
            elif age > 5 and age < 10:
                return 'Established'
            else:
                return 'Mature'

        self.df['Company Stage'] = self.df['Age of company in years'].apply(categorize)

    def _replace_no_info_none(self) -> None:
        '''
        Replaces 'No Info' from 'Age of company in years' column to np.nan value
        :return:
        '''
        self.df['Age of company in years'] = self.df['Age of company in years'].replace('No Info', np.nan)

    @property
    def _average_year_per_worker(self) -> float:
        '''
        Computes the average age per worker in the dataset( age / worker)
        :return: the average age per worker.
        '''
        df_cleaned = self.df.dropna(subset=['Age of company in years'])
        df_cleaned.loc[:, 'Age of company in years'] = df_cleaned['Age of company in years'].astype(int)

        total_company_age = df_cleaned['Age of company in years'].sum()
        total_workers = df_cleaned['Employee Count'].sum()

        average_age_per_worker = total_company_age / total_workers
        return average_age_per_worker

    def _getting_value(self, employee_count: float) -> float:
        '''
        Computes the age value for missing entries in the 'Age of company in years' column.
        :param employee_count: the number of employees in a company.
        :return: returns computed company age
        '''
        if pd.isnull(employee_count):
            return np.nan
        if int(self._average_year_per_worker * employee_count) == 0:
            return 1
        elif int(self._average_year_per_worker * employee_count) > 12:
            return 12
        else:
            return int(self._average_year_per_worker * employee_count)

    def _adding_average_company_age(self) -> None:
        """
        Fills missing values in the 'Age of company in years' column by computing average age values.
        """
        self._replace_no_info_none()
        self.df['Age of company in years'] = self.df['Age of company in years'].fillna(self.df['Employee Count'].apply(self._getting_value))

    def _fill_missing_age_values_by_mean(self) -> None:
        """
        Fills missing values in the 'Age of company in years' column by using the mean age.
        """
        df_cleared = self.df.dropna(subset=['Age of company in years'])
        mean_age = int(df_cleared['Age of company in years'].mean())
        self.df['Age of company in years'] = self.df['Age of company in years'].fillna(mean_age)

    def filling_age_missing_values(self) -> None:
        """
        Fills missing age values in the dataset using a combination of methods.
        """
        self._changing_column_type()
        # Firstly it tries to add company age by Employee count
        self._adding_average_company_age()
        # If there is any missing Employee count and Age of company it fills age with mean value
        self._fill_missing_age_values_by_mean()


if __name__ == "__main__":
    analyze = AgeDataAnalyzing()
    analyze.filling_age_missing_values()
