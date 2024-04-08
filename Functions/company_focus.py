import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class CompanyFocus:
    def __init__(self, df: pd.DataFrame):
        """
        Constructor method for the CompanyFocus class.

        Parameters:
        - df: A pandas DataFrame containing the company data.
        """
        self.df = df
        self.df = df

    def _drop_na_values(self):
        """
        Method to replace 'N' and '\\' with NaN in the 'Focus functions of company' column
        and drop rows with NaN values in that column.
        """

        self.df['Focus functions of company'] = self.df['Focus functions of company'].replace('N', np.nan)
        self.df['Focus functions of company'] = self.df['Focus functions of company'].replace('\\', np.nan)
        self.df = self.df.dropna(subset=['Focus functions of company'])

    def _normalize_value(self, value):
        """
        Method to normalize a string value by converting it to lowercase and stripping
        leading and trailing whitespaces.

        Parameters:
        - value: A string value to be normalized.
        """
        return value.lower().strip()

    def _standartize_value(self, value):
        """
        Method to standardize the values in the 'Focus functions of company' column using predefined variations.

        Parameters:
        - value: A string value to be standardized.

        Returns:
        The standardized value based on the predefined variations.
        """
        variations = {
            'operations': 'operation',
            'marketing, sales': 'marketing & sales',
            'sales, marketing': 'marketing & sales',
            'marketing \r\nsales': 'marketing & sales',
            'data management': 'database management',
            'software service': 'software',
            'customer servce': 'customer service',
            'operations, sales, marketing': 'marketing & sales',
            'sales & marketing': 'marketing & sales',
            'bug fix': 'software',
            'malware protection': 'security',
            'social media optimization': 'social media',
            'e-learning': 'education',
            'mobile app': 'application',
            'social media management': 'social media',
            'personal apps': 'application',
            'app revenue': 'application',
            'intellectual property analysis and visualisation': 'analytics',
            'marketiing': 'marketing',
            'it & sales': 'information technology',
            'social news': 'social media',
            'sale': 'sales',
            'social network': 'social media',
            'consumer web': 'web development',
            'writing blog': 'content creation',
            'curated web': 'web development',
            'recommendation': 'recommendation system',
            'customer retention, customer feedback': 'customer service',
            'inventory management': 'management',
            'energy saving': 'energy management',
            'optimization, crm, pricing': 'management',
            'many': 'multiple',
            'search enginenoptimization': 'search engine optimization',
            'information management': 'management',
            'social media analytics': 'analytics',
            'customer engagement': 'customer service',
            'marketing, procurement, human resources': 'marketing',
            'crm, marketing, human resources': 'marketing',
            'crm': 'customer relationship management',
            'merchandising, marketing': 'marketing',
            'travel planning': 'travel',
            'data visualization, content marketing, presentations': 'analytics',
            'news': 'media',
            'analtics': 'analytics',
            'elearning': 'education',
            'phone intelligence': 'mobile technology',
            'social branding': 'marketing',
            'reporting': 'analytics',
            'dashboards': 'analytics',
            'localized behaviour': 'behavioral analysis',
            'video streaming': 'media',
            'payment': 'finance',
            'networking': 'network technology',
            'wireless': 'network technology',
            'advertising': 'marketing',
            'game': 'gaming',
            'search': 'search engine',
            'conssumer web': 'web development',
            'online music': 'music',
            'media': 'media',
            'cloud computing': 'cloud technology',
            'social commerce': 'ecommerce',
            'finance': 'finance',
            'social media marketing': 'marketing',
            'publishing': 'media',
            'global': 'globalization',
            'music intelligece': 'music',
            'location based service': 'location-based services',
            'social tv analytics': 'analytics',
            'data driven applications': 'application',
            'iphone apps': 'mobile applications',
            'sales,marketing': 'marketing & sales',
            'network optimization': 'network optimization',
            'privacy': 'security',
            'targeting optimize': 'targeted advertising',
            'mail reports': 'reporting',
            'big data analytics': 'big data',
            'metrics': 'analytics',
            'pricing': 'pricing strategy',
            'mobile app development': 'application development',
            'mrkting': 'marketing',
            'revenue maximization': 'revenue optimization',
            'analytics crowdsourcing': 'analytics',
            'app': 'application',
            'social': 'social media',
            'enterprise': 'enterprise solutions',
            'billing': 'billing management',
            'server design': 'server management',
            'marketing,sales': 'marketing & sales',
            'production,sales': 'production & sales',
            'targeting': 'targeted advertising',
            'mobile technology': 'technology',
            'mobile applications': 'application',
            'web analytics': 'analytics'
        }

        return variations.get(value, value)

    def _modifing_data(self):
        """
        Method to modify the company data by applying data cleaning and standardization.
        """
        self._drop_na_values()
        self.df['Focus functions of company'] = self.df['Focus functions of company'].apply(self._normalize_value)
        self.df['Focus functions of company'] = self.df['Focus functions of company'].apply(self._standartize_value)

    def plot_dependence(self, pie_count=10, success=True):
        """
         Method to plot the dependence of successful or failed companies on their focus functions.

         Parameters:
         - pie_count: Number of top focus functions to be displayed in the plot.
         - success: Boolean indicating whether to plot for successful companies (True) or failed companies (False).
         """
        self._modifing_data()
        focus_counts = {}
        focuses = self.df['Focus functions of company'].unique()
        for focus in focuses:
            focus_counts[focus] = {'Success' : 0, 'Failed': 0}
        for index,row in self.df.iterrows():
            focus = row['Focus functions of company']
            status = row['Dependent-Company Status']
            focus_counts[focus][status] += 1

        focus_df = pd.DataFrame(focus_counts).T

        if success:
            data = focus_df['Success'].sort_values(ascending=False)[:pie_count]
            sns.barplot(x=data.values, y=data.index)
            plt.title('Top {} Focus Functions of Successful Companies'.format(pie_count))
        else:
            data = focus_df['Failed'].sort_values(ascending=False)[:pie_count]
            sns.barplot(x=data.values, y=data.index)
            plt.title('Top {} Focus Functions of Failed Companies'.format(pie_count))
        plt.xlabel('Count')
        plt.ylabel('Focus Functions')
        plt.show()



if __name__ == '__main__':
    focus = CompanyFocus(pd.read_csv('../Data/ml_code_data.csv', encoding='latin-1'))
    focus.plot_dependence(success=False)