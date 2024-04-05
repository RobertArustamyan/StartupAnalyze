import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class InternetActivity:
    '''
    A class for analyzing Internet activity of companies.
    '''

    def __init__(self):
        """
        Initializes the AgeDataAnalyzing object by loading a dataset containing company age information.
        """
        self.df = pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv", encoding='latin-1')

    def _seperate_data(self) -> None:
        '''
        Seperates data to success and faild parts
        '''
        self.success_data = self.df[self.df['Dependent-Company Status'] == 'Success']
        self.failed_data = self.df[self.df['Dependent-Company Status'] == 'Failed']

    def analyze_internet_activity(self, plot=False):
        '''
        Analyzes the internet activity scores of success and failed companies
        :param plot:A flag indicating whether to plot the distribution of internet activity scores. Default is False
        :return:A tuple containing the descriptive statistics of internet activity scores for success and failed companies
               The tuple format is (success_stats, failed_stats), where each element is a Series containing descriptive statistics
        '''
        self._seperate_data()
        success_stats = self.success_data['Internet Activity Score'].describe()
        failed_stats = self.failed_data['Internet Activity Score'].describe()
        if plot:
            plt.figure(figsize=(10, 6))
            sns.histplot(self.success_data['Internet Activity Score'], color='green', kde=True, label='Success')
            sns.histplot(self.failed_data['Internet Activity Score'], color='red', kde=True, label='Failed')

            plt.title('Distribution of Internet Activity Scores')
            plt.xlabel('Internet Activity Score')
            plt.ylabel('Frequency')
            plt.legend()
            plt.show()

        return success_stats, failed_stats


if __name__ == "__main__":
    internet = InternetActivity()
    print(internet.analyze_internet_activity(plot=True))
