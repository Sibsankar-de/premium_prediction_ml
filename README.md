# 🏦 Insurance Premium Prediction

This project is a **Machine Learning application** built with **Python** and deployed using **Streamlit**.  
It predicts the **annual insurance premium** based on customer details such as age, dependants, BMI category, smoking habits, medical history, and more.

---

## 📌 Features
- Collects user details through a simple Streamlit form.
- Uses a trained **Machine Learning model** to predict insurance premium.
- Inputs include:
  - Age  
  - Gender  
  - Region  
  - Marital Status  
  - Number of Dependants  
  - BMI Category  
  - Smoking Status  
  - Employment Status  
  - Income Level  
  - Income (Lakhs)  
  - Medical History  
  - Insurance Plan  
  - Genetical Risk  
- Clean and interactive UI built with **Streamlit**.

---

## 🚀 Tech Stack
- **Python 3.11+**
- **Streamlit** – Web interface  
- **scikit-learn & XGBoost** – (depending on your implementation)  
- **pandas, numpy** – Data handling  
- **joblib** – Model saving and loading  

---

## ⚙️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Sibsankar-de/premium_prediction_ml.git
    cd insurance-premium-prediction
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run .\main.py
    ```

---

## 📂 Project Structure

```
├── main.py
├── prediction_helper.py
├── artifacts/
│   ├── model_rest.joblib
│   ├── model_young.joblib
│   ├── scaler_rest.joblib
│   └── scaler_young.joblib
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📝 Usage

- Fill in the customer details in the web form.
- Click **Predict** to view the estimated annual insurance premium.

---