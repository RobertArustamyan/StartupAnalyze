import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

class TeamGrown:
    def __init__(self, dataframe: pd.DataFrame):
        '''
        Initializes the TeamGrown object by loading a dataset.
        :param dataframe: A DataFrame of Data
        '''
        self.df = dataframe

    def _preparing_data(self):
        mapping_dict = {
            'Yes': True,
            'yes': True,
            'YES': True,
            'No': False,
            'No Info': np.nan,
            None: np.nan,
        }
        self.df['Has the team size grown'] = self.df['Has the team size grown'].map(mapping_dict)

    def plot_team_growth_success(self):
        '''
        Plots  the impact of team growth on company success.
        '''

        self._preparing_data()
        plt.figure(figsize=(8, 6))
        sns.countplot(data=self.df, x='Has the team size grown', hue='Dependent-Company Status')
        plt.title('Impact of Team Growth on Company Success')
        plt.xlabel('Team Size Growth')
        plt.ylabel('Count')
        plt.legend(title='Company Status')
        plt.show()

if __name__ == '__main__':
    team = TeamGrown(pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1'))
    team.analyze_team_growth_success()