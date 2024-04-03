import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AnalyzingData:
    def __init__(self):
        self.df = pd.read_csv(r"C:\Users\Mikayel\PycharmProjects\InternshipTask\Data\data.csv",encoding='latin-1')

    @property
    def columns(self):
        return self.df.columns.tolist()

    def company_age_boxplot(self):
        self.df['Age of company in years'] = pd.to_numeric(self.df['Age of company in years'].replace('No Info', -1),errors='coerce')
        self.df['Age of company in years'].fillna(-1, inplace=True)
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='Dependent-Company Status', y='Age of company in years', data=self.df[self.df['Age of company in years'] >= 0])
        plt.title('Distribution of Company Age by Success Status')
        plt.xlabel('Success Status')
        plt.ylabel('Age of company in years')

        plt.show()

    def adding_company_stage(self):
        def categorize(age):
            if age < 5:
                return 'Early Stage'
            elif age > 5 and age < 10:
                return 'Established'
            else:
                return 'Mature'


if __name__ == "__main__":
    a = AnalyzingData()
    a.company_age_boxplot()