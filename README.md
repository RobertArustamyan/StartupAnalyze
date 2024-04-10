# Startup Success Predictor

---

## Overview
The Startup Success Predictor is a tool that predicts whether a startup will be successful or not based on machine learning models trained on various features of the startup data. It utilizes Random Forest and Decision Tree models to provide predictions. View Project Documentation [Here!](https://startupanalyze.onrender.com)

---
## Features
- Predicts startup success based on various factors such as founder experience, industry focus, business model, and more.
- Provides accurate predictions using machine learning algorithms.
- Easy-to-use interface for users to input startup data and receive predictions.

---
## Installation

---
1. Clone the repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:

    ```bash
    python app.py
    ```

2. Access the application through your web browser at `http://localhost:5000`.

3. Enter the required information about your startup and click on the "Predict" button to get the prediction result.

## Project Structure

---
The project structure is organized as follows:

- `app.py`: Contains the main Flask application.
- `templates/`: Directory containing HTML templates used by Flask to render web pages.
- `Functions/`: Directory containing Python modules for data analysis, machine learning, and preprocessing.
- `models/`: Directory containing trained machine learning models (`rf_model.joblib`, `decision_tree_model.joblib`).
- `analysis.ipynb`: Data analyzing part
- `README.md`: This file, providing an overview of the project and instructions for installation and usage.

## Requirements

---
- Python 3.x
- Flask
- Pandas
- Numpy
- Scikit-learn
- Joblib

## License

---
This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.txt) License. See the [LICENSE](LICENSE) file for details.

## Contact

---
If you have any questions or feedback, feel free to reach out to me at [robertarustamyan2@gmail.com](https://mail.google.com/mail/u/0/?fs=1&to=robertarustamyan2@gmail.com).
