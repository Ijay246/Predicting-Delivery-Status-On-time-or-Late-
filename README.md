Delivery Prediction Model

This is a Streamlit web application that predicts whether a delivery will be On-time or Late based on input features such as agent rating, pick-up hour, traffic, area, weather, and agent age.

The model behind this app is a Logistic Regression model trained and saved as log_model.pkl using Joblib.

Features

Users can input the following details through the interface:

Agent Rating – Rating of the delivery agent (scale 1–6).

Pick-Up Hour – Time of the day when the parcel is picked up (0–13).

Traffic – Categorical traffic condition (High, Jam, Low, Medium).

Area – Categorical area type (Metropolitan, Semi-Urban, Urban, Other).

Weather – Categorical weather condition (Cloudy, Fog, Sandstorms, Stormy, Sunny, Windy).

Agent Age – Age of the delivery agent (15–50).

The app then predicts if the delivery will be On-time or Late.

Technologies Used

Python

Streamlit

NumPy

Joblib

Machine Learning (Logistic Regression)

Installation & Usage
1. Clone the Repository
git clone https://github.com/your-username/delivery-prediction-model.git
cd delivery-prediction-model

2. Install Dependencies

Make sure you have Python 3.8+ installed. Then run:

pip install -r requirements.txt

3. Run the App
streamlit run app.py


This will open the app in your default web browser.

Project Structure
delivery-prediction-model/
│── app.py               # Streamlit app script
│── log_model.pkl        # Trained Logistic Regression model
│── requirements.txt     # Required dependencies
│── README.md            # Project documentation

Example Input & Output

Input:

Agent Rating: 5

Pick-Up Hour: 8

Traffic: Medium

Area: Urban

Weather: Sunny

Agent Age: 30

Output:

Prediction: On-time ✅
