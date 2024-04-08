import pandas as pd
from sklearn.preprocessing import LabelEncoder


class MlDataPrepare:
    def __init__(self, df: pd.DataFrame, columns_for_model: list):
        """
        Initialize the MlDataPrepare object.

        Parameters:
        - df (pd.DataFrame): The DataFrame containing the data.
         - columns_for_model (list): List of column names to be used for the model.
        """
        self.df = df
        self.le = LabelEncoder()
        self.model_columns = columns_for_model
        self._prepare_ml_data()

    def _prepare_ml_data(self):
        """
        Prepare the data for machine learning by converting columns to appropriate data types.
        """
        # Convert specific columns to integer and boolean types
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
        # Filter the DataFrame to include only the specified model columns
        self.df = self.df[self.model_columns]

    def transform_bool_values(self, value):
        """
        Transform boolean values to binary integers (0 or 1).

        Parameters:
        - value (bool): The boolean value to be transformed.

        Returns:
        - int: The transformed binary integer value.
        """
        transformator = {
            True: 1,
            False: 0
        }
        return transformator[value]

    def transform_cloud_platform_based(self, value):
        """
        Transform cloud platform-based services to categorical integers.

        Parameters:
        - value (str): The value indicating cloud platform-based services.

        Returns:
        - int: The transformed categorical integer value.
        """
        tranformator = {
            'None': 0,
            'Cloud': 1,
            'Platform': 2,
            'Both': 3
        }
        return tranformator[value]

    def transform_business_type(self, value):
        """
        Transform business type to categorical integers.

        Parameters:
        - value (str): The value indicating business type.

        Returns:
        - int: The transformed categorical integer value.
        """
        tranformator = {
            'B2C': 0,
            'B2B': 1
        }
        return tranformator[value]

    @property
    def transform_dict(self):
        """
        Get the transformation dictionary for focus functions of the company.

        Returns:
        - dict: The transformation dictionary.
        """
        dictionary = {
            'operation': 0,
            'marketing & sales': 1,
            'analytics': 2,
            'research': 3,
            'computing': 4,
            'marketing': 5,
            'technology': 6,
            'database management': 7,
            'solution providing': 8,
            'social media': 9,
            'targeted marketing': 10,
            'community betterment': 11,
            'strategy': 12,
            'software': 13,
            'data integration': 14,
            'security': 15,
            'sales': 16,
            'risk': 17,
            'marketing, web analytics': 18,
            'strategy, operations, finacial planning': 19,
            'data collection': 20,
            'education': 21,
            'application': 22,
            'analytic': 23,
            'consumer behaviour': 24,
            'customer service': 25,
            'retail': 26,
            'data visualization': 27,
            'service': 28,
            'marketing, technology, finance & accounting, customer service': 29,
            'computing, training': 30,
            'operations, marketing': 31,
            'social advertising': 32,
            'development, marketing, and administration': 33,
            'information technology': 34,
            'web': 35,
            'web development': 36,
            'content creation': 37,
            'recommendation system': 38,
            'marketing,sales,risk,operations': 39,
            'development tool': 40,
            'tool': 41,
            'management': 42,
            'energy management': 43,
            'multiple': 44,
            'games': 45,
            'marketing, customer targeting': 46,
            'entertainment': 47,
            'search engine optimization': 48,
            'marketing, strategy': 49,
            'customer relationship management': 50,
            'travel': 51,
            'media': 52,
            'mobile technology': 53,
            'behavioral analysis': 54,
            'finance': 55,
            'network technology': 56,
            'gaming': 57,
            'search engine': 58,
            'music': 59,
            'cloud technology': 60,
            'ecommerce': 61,
            'globalization': 62,
            'location-based services': 63,
            'mobile applications': 64,
            'network optimization': 65,
            'targeted advertising': 66,
            'reporting': 67,
            'big data': 68,
            'pricing strategy': 69,
            'application development': 70,
            'revenue optimization': 71,
            'enterprise solutions': 72,
            'billing management': 73,
            'server management': 74,
            'production & sales': 75
        }
        return dictionary
    def transform_focus_type(self, value):
        """
        Transform focus functions of the company to numerical representations.

        Parameters:
        - value (str): The value indicating focus functions of the company.

        Returns:
        - int: The transformed numerical representation.
        """
        transformator = self.transform_dict
        return transformator[value.strip()]
    def prepare_data(self):
        """
        Prepare the data for machine learning by applying transformations to specific columns.

        Returns:
        - pd.DataFrame: The prepared DataFrame for machine learning.
        """
        self.df['Has the team size grown'] = self.df['Has the team size grown'].apply(self.transform_bool_values)
        self.df['Worked in top companies'] = self.df['Worked in top companies'].apply(self.transform_bool_values)
        self.df['Focus on consumer data?'] = self.df['Focus on consumer data?'].apply(self.transform_bool_values)
        self.df['Subscription based business'] = self.df['Subscription based business'].apply(
            self.transform_bool_values)
        self.df['Machine Learning based business'] = self.df['Machine Learning based business'].apply(
            self.transform_bool_values)
        self.df['Predictive Analytics business'] = self.df['Predictive Analytics business'].apply(
            self.transform_bool_values)
        self.df['Speech analytics business'] = self.df['Speech analytics business'].apply(self.transform_bool_values)
        self.df['Big Data Business'] = self.df['Big Data Business'].apply(self.transform_bool_values)
        self.df['Company awards'] = self.df['Company awards'].apply(self.transform_bool_values)

        # Apply transformations to categorical columns
        self.df['Cloud or platform based serive/product?'] = self.df['Cloud or platform based serive/product?'].apply(
            self.transform_cloud_platform_based)
        self.df['B2C or B2B venture?'] = self.df['B2C or B2B venture?'].apply(self.transform_business_type)
        self.df['Focus functions of company'] = self.df['Focus functions of company'].apply(self.transform_focus_type)

        return self.df

if __name__ == '__main__':
    columns = ['Internet Activity Score', 'Has the team size grown', 'Worked in top companies', 'Founder Experience',
               'Focus on consumer data?', 'Subscription based business', 'Cloud or platform based serive/product?',
               'Machine Learning based business', 'Predictive Analytics business', 'Speech analytics business',
               'Big Data Business', 'B2C or B2B venture?', 'Company awards', 'Focus functions of company']

    mldata = MlDataPrepare(pd.read_csv('../Data/data-to-work.csv', encoding='latin-1'), columns)
    print(mldata.transform_dict)
