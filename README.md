# Delivery Prediction Model  

A **Streamlit web application** that predicts whether a delivery will be **On-time** or **Late** based on user inputs such as agent rating, traffic, area, weather, and more.  

The app uses a **Logistic Regression model** trained and saved as `log_model.pkl`.  

---

## Features  

-  **Agent Rating** – Rating of the delivery agent (1–6).  
-  **Pick-Up Hour** – Time of the day when the parcel is picked up (0–13).  
-  **Traffic** – Categorical traffic condition (High, Jam, Low, Medium).  
-  **Area** – Categorical area type (Metropolitan, Semi-Urban, Urban, Other).  
- ☁ **Weather** – Categorical weather condition (Cloudy, Fog, Sandstorms, Stormy, Sunny, Windy).  
-  **Agent Age** – Age of the delivery agent (15–50).  

The model then predicts:  
-  **On-time**  
-  **Late**  

---

## Tech Stack  

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [NumPy](https://numpy.org/)  
- [Joblib](https://joblib.readthedocs.io/)  
- Logistic Regression (Scikit-learn)  

---

##  Getting Started  

### 1️ Clone the Repository  
```bash
git clone https://github.com/your-username/delivery-prediction-model.git
cd delivery-prediction-model
```
### 2 Install Dependencies
```
pip install -r requirements.txt
```
### Run the App
```
streamlit run app.py
```
### Project Structure  
delivery-prediction-model/  
│── app.py               # Streamlit app script  
│── log_model.pkl        # Trained Logistic Regression model  
│── requirements.txt     # Required dependencies  
│── README.md   
