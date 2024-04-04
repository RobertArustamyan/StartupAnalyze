import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
class AgeDataAnalyzing:
    def __init__(self):
        self.df = pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv",encoding='latin-1')

    @property
    def columns(self):
        return self.df.columns.tolist()

    def _changing_column_type(self):
        self.df['Age of company in years'] = pd.to_numeric(self.df['Age of company in years'], errors='coerce')


    def company_age_boxplot(self):
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='Dependent-Company Status', y='Age of company in years', data=self.df[self.df['Age of company in years'] >= 0])
        plt.title('Distribution of Company Age by Success Status')
        plt.xlabel('Success Status')
        plt.ylabel('Age of company in years')

        plt.show()

    def _adding_company_stage(self):
        def categorize(age):
            if age < 5:
                return 'Early Stage'
            elif age > 5 and age < 10:
                return 'Established'
            else:
                return 'Mature'

        self.df['Company Stage'] = self.df['Age of company in years'].apply(categorize)

    def _replace_no_info_none(self):
        self.df['Age of company in years'] = self.df['Age of company in years'].replace('No Info', np.nan)

    @property
    def _average_year_per_worker(self):
        df_cleaned = self.df.dropna(subset=['Age of company in years'])
        df_cleaned.loc[:, 'Age of company in years'] = df_cleaned['Age of company in years'].astype(int)

        total_company_age = df_cleaned['Age of company in years'].sum()
        total_workers = df_cleaned['Employee Count'].sum()

        average_age_per_worker = total_company_age / total_workers
        return average_age_per_worker

    def _getting_value(self, employee_count):
        if pd.isnull(employee_count):
            return np.nan
        if int(self._average_year_per_worker * employee_count) == 0:
            return 1
        elif int(self._average_year_per_worker * employee_count) > 12:
            return 12
        else:
            return int(self._average_year_per_worker * employee_count)


    def _adding_average_company_age(self):
        self._replace_no_info_none()
        self.df['Age of company in years'].fillna(self.df['Employee Count'].apply(self._getting_value), inplace=True)

    def _fill_missing_age_values_by_mean(self):
        df_cleared = self.df.dropna(subset=['Age of company in years'])
        mean_age =  int(df_cleared['Age of company in years'].mean())
        self.df['Age of company in years'].fillna(mean_age, inplace=True)

    def filling_age_missing_values(self):
        self._adding_average_company_age()
        self._fill_missing_age_values_by_mean()


if __name__ == "__main__":
    analyze = AgeDataAnalyzing()
    analyze._changing_column_type()
    analyze.filling_age_missing_values()

