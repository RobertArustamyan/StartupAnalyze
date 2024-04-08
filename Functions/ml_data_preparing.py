import pandas as pd
from sklearn.preprocessing import LabelEncoder


class MlDataPrepare:
    def __init__(self, df: pd.DataFrame, columns_for_model: list):
        self.df = df
        self.le = LabelEncoder()
        self.model_columns = columns_for_model

    def _prepare_ml_data(self):
        self.df['Founder Experience'] = self.df['Founder Experience'].astype(int)
        self.df['Has the team size grown'] = self.df['Has the team size grown'].replace(
            {'True': True, 'False': False}).astype(bool)
        self.df['Worked in top companies'] = self.df['Worked in top companies'].replace(
            {'True': True, 'False': False}).astype(bool)
        self.df['Focus on consumer data?'] = self.df['Focus on consumer data?'].replace(
            {'True': True, 'False': False}).astype(bool)
        self.df['Subscription based business'] = self.df['Subscription based business'].replace(
            {'True': True, 'False': False}).astype(bool)
        self.df['Machine Learning based business'] = self.df['Machine Learning based business'].replace(
            {'True': True, 'False': False}).astype(bool)
        self.df['Predictive Analytics business'] = self.df['Predictive Analytics business'].replace(
            {'True': True, 'False': False}).astype(bool)
        self.df['Speech analytics business'] = self.df['Speech analytics business'].replace(
            {'True': True, 'False': False}).astype(bool)
        self.df['Big Data Business'] = self.df['Big Data Business'].replace({'True': True, 'False': False}).astype(bool)
        self.df['Company awards'] = self.df['Company awards'].replace({'Yes': True, 'No': False}).astype(bool)

        self.df = self.df[self.model_columns]

    def _transform_data(self):
        self._prepare_ml_data()
        for column in self.model_columns:
            if self.df[column].dtype == 'object':
                print(column, 'obj')
            elif self.df[column].dtype == 'bool':
                print(column, 'bool')


if __name__ == '__main__':
    columns = ['Internet Activity Score', 'Has the team size grown', 'Worked in top companies', 'Founder Experience',
               'Focus on consumer data?', 'Subscription based business', 'Cloud or platform based serive/product?',
               'Machine Learning based business', 'Predictive Analytics business', 'Speech analytics business',
               'Big Data Business', 'B2C or B2B venture?', 'Company awards', 'Focus functions of company']

    mldata = MlDataPrepare(pd.read_csv('../Data/data-to-work.csv', encoding='latin-1'), columns)
    mldata.df.head(10)
