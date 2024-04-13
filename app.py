import pandas as pd
from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# After button push works function below
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Loading models
        rf_model = load('Models/rf_model.joblib')
        dr_model = load('Models/dt_model.joblib')
        # For integer value fields
        internet_activity = float(request.form.get('IAS', 0))
        founder_exp = int(request.form.get('FE', 0))

        # For checkbox fields
        team_size_grown = 1 if 'HTTSG' in request.form else 0
        worked_in_top = 1 if 'WITC' in request.form else 0
        consumer_data = 1 if 'FOCD' in request.form else 0
        sub_based = 1 if 'SBB' in request.form else 0
        ml_based = 1 if 'MLBB' in request.form else 0
        pred_based = 1 if 'PAB' in request.form else 0
        speech_based = 1 if 'SAB' in request.form else 0
        bid_data_based = 1 if 'BDB' in request.form else 0
        company_awards = 1 if 'CA' in request.form else 0
        # For category type fields
        ventrue_type = int(request.form['VentureType'])
        cloud_or_platform = int(request.form['COPB'])
        focus = int(request.form['FocusFonction'])
        # For Checkboxes from page
        data = pd.DataFrame({
            'Internet Activity Score': [internet_activity],
            'Has the team size grown': [team_size_grown],
            'Worked in top companies': [worked_in_top],
            'Founder Experience': [founder_exp],
            'Focus on consumer data?': [consumer_data],
            'Subscription based business': [sub_based],
            'Cloud or platform based serive/product?': [cloud_or_platform],
            'Machine Learning based business': [ml_based],
            'Predictive Analytics business': [pred_based],
            'Speech analytics business': [speech_based],
            'Big Data Business': [bid_data_based],
            'B2C or B2B venture?': [ventrue_type],
            'Company awards': [company_awards],
            'Focus functions of company': [focus]
        })
        data['Founder Experience'] = data['Founder Experience'].astype('int32')
        # Prdiction
        prediction_one = rf_model.predict(data)
        prediction_two = dr_model.predict(data)

        if prediction_one[0] == 'Success' and prediction_two[0] == 'Success':
            return_text = 'Congratulations! Your startup will be successful.'
        elif prediction_one[0] == 'Success':
            return_text = 'Algorithm 1 succeeded, but Algorithm 2 failed.'
        elif prediction_two[0] == 'Success':
            return_text = 'Algorithm 2 succeeded, but Algorithm 1 failed.'
        else:
            return_text = 'Neither algorithm was successful. You may need to make changes to your startup.'

        return render_template('index.html', prediction=return_text)


if __name__ == '__main__':
    app.run(debug=False)
