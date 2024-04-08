import pandas as pd
import numpy as np


class CompanyFocus:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def _drop_na_values(self):
        self.df['Focus functions of company'] = self.df['Focus functions of company'].replace('N', np.nan)
        self.df['Focus functions of company'] = self.df['Focus functions of company'].replace('\\', np.nan)
        self.df = self.df.dropna(subset=['Focus functions of company'])

    def _normalize_value(self, value):
        return value.lower().strip()

    def _standartize_value(self, value):
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
        self._drop_na_values()
        self.df['Focus functions of company'] = self.df['Focus functions of company'].apply(self._normalize_value)
        self.df['Focus functions of company'] = self.df['Focus functions of company'].apply(self._standartize_value)
        print(self.df['Focus functions of company'].unique())

if __name__ == '__main__':
    focus = CompanyFocus(pd.read_csv('../Data/ml_code_data.csv', encoding='latin-1'))
    focus._modifing_data()