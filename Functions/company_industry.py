import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
    def industry_success_distribution(self):
        industry_names = self._unique_industry_values
        industry_counts = {}

        filtered_df = self.df.dropna(subset=['Industry of company'])

        for industry in industry_names:
            industry_counts[industry] = {'Success': 0, 'Failed': 0}

        for index,row in filtered_df.iterrows():
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

        # Plot pie chart
        plt.figure(figsize=(10, 6))
        industry_df['Success Rate'].plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
        plt.title('Success Rate by Industry')
        plt.ylabel('')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.show()

if __name__ == '__main__':
    a = IndustryAnalyzing(
        pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    print(a.industry_success_distribution())
