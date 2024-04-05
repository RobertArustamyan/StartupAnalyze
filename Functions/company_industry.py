import matplotlib.pyplot as plt
import pandas as pd


class IndustryAnalyzing:
    def __init__(self, dataframe: pd.DataFrame):
        '''
        Initializes the IndustryAnalyzing object by loading a dataset.
        :param dataframe: A DataFrame of Data
        '''
        self.df = dataframe

    @property
    def _unique_industry_values(self):
        unique_values = set()
        filtered_df = self.df.dropna(subset=['Industry of company'])
        for cell in filtered_df['Industry of company']:
            industries = cell.split('|')
            industries = [industry.strip().lower() for industry in industries]
            unique_values.update(industries)
        return list(unique_values)

    def _matching_values_from_focus_column(self, focus):
        mapping_dict = {
            'many': 'e-commerce',
            'game': 'music',
            'targeted marketing': 'email',
            'enterprise': 'energy',
            'risk': 'career / job search',
            'travel planning': 'analytics',
            'marketing,sales': 'classifieds',
            'merchandising, marketing': 'transportation',
            'strategy': 'advertising',
            'solution providing': 'network / hosting / infrastructure',
            'information management': 'healthcare',
            'customer retention, customer feedback': 'finance',
            'conssumer web': 'telecommunications',
            'marketing, strategy': 'publishing',
            'crm, marketing, human resources': 'human resources (hr)',
            'development, marketing, and administration': 'search',
            'service': 'media',
            'research': 'space travel',
            'web': 'marketing',
            'server design': 'insurance',
            'software': 'security',
            'consumer web': 'cleantech',
            'curated web': 'software development',
            'operations': 'pharmaceuticals',
            'operation': 'deals',
            'database management': 'crowdfunding',
            'mobile app development': 'travel',
            'software service': 'cloud computing',
            'targeting': 'entertainment',
            'social media': 'retail',
            'sales & marketing': 'education',
            'news': 'gaming',
            'sales': 'market research',
            'crm': 'enterprise software',
            'social network': 'hospitality',
            'networking': 'mobile',
            'ecommerce': 'government',
            'technology': 'social networking',
            'games': 'food & beverages',
            'marketing,sales,risk,operations': 'real estate'
        }
        if focus in mapping_dict:
            return mapping_dict[focus]
        return

    def _filling_na_values(self):
        values_with_categorize_need = set()
        industry_names = self._unique_industry_values
        for index, row in self.df.iterrows():
            if pd.isna(row['Industry of company']):
                focus_function = row['Focus functions of company']
                if isinstance(focus_function, str):
                    focus_function = focus_function.strip().lower()

                    if focus_function in industry_names:
                        self.df.at[index, 'Industry of company'] = focus_function
                    else:
                        self.df.at[index, 'Industry of company'] = self._matching_values_from_focus_column(focus_function)


    def industry_success_distribution(self, pie_count=10, success=True):
        self._filling_na_values()
        industry_names = self._unique_industry_values
        industry_counts = {}

        filtered_df = self.df.dropna(subset=['Industry of company'])

        for industry in industry_names:
            industry_counts[industry] = {'Success': 0, 'Failed': 0}

        for index, row in filtered_df.iterrows():
            industries = row['Industry of company'].split('|')
            status = row['Dependent-Company Status']
            for industry in industries:
                industry = industry.strip().lower()
                industry_counts[industry][status] += 1

        industry_df = pd.DataFrame(industry_counts).T

        # Calculate proportions
        industry_df['Total'] = industry_df['Success'] + industry_df['Failed']
        industry_df['Success Rate'] = industry_df['Success'] / industry_df['Total']
        industry_df['Failed Rate'] = industry_df['Failed'] / industry_df['Total']


        industry_df = industry_df.sort_values(by='Total', ascending=False).head(pie_count)

        plt.figure(figsize=(8,6))

        if success:
            industry_df['Success Rate'].plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
            plt.title('Success Rate by Industry')
        else:
            industry_df['Failed Rate'].plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
            plt.title('Failed Rate by Industry')

        plt.axis('equal')
        plt.ylabel('')
        plt.show()


if __name__ == '__main__':
    a = IndustryAnalyzing(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    a.industry_success_distribution()
