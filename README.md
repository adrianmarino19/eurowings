# ✈️ Takeoff — Flight Price Prediction for Eurowings Digital

**🏆 Awarded Best Project @ Le Wagon Data Science**  
**🚀 Deployed on Google Cloud Run | FastAPI Backend | Streamlit Frontend**

Takeoff is a flight price prediction system built for **Eurowings Digital** (€2B airline group) to forecast competitor pricing strategies.  
The solution combines **machine learning**, **automated ETL pipelines**, and **cloud deployment** to deliver real-time price predictions via a web application.

It empowers airlines to proactively monitor market dynamics and adjust pricing strategies with data-driven insights.

:boom:<a href='https://takeoff.streamlit.app/'>Takeoff Web App</a>

<br>

## 📚 Project Overview

- **Goal:** Help Eurowings Digital anticipate competitor pricing trends to optimize strategic decision-making.
- **Data:** Aggregated flight booking data sourced from Skyscanner and other providers.
- **Model:** Gradient Boosted Trees (XGBoost), trained on engineered features including:
  - Distance between airports
  - Destination GDP per capita
  - Cabin class
  - Flight type (Return / One-way)
  - Connecting vs. direct flights
  - Booking horizon and trip length
  - Carrier-specific behavior

<br>

## 🛠 Tech Stack

| Component        | Technology            |
|------------------|------------------------|
| **Modeling**     | XGBoost, Random Forest, Scikit-learn |
| **API**          | FastAPI |
| **Deployment**   | Docker + Google Cloud Run |
| **Frontend**     | Streamlit |
| **Data Handling**| Pandas, Numpy |
| **Environment**  | Python 3.11 |

<br>

## 🛤️ Architecture

- **Backend (FastAPI):**  
  Exposes a `/predict` endpoint which receives flight search parameters and returns a predicted flight price.

- **Model Training:**  
  `train.py` processes the historical flight data, engineers features, trains the model, and exports it as `pipeline2.pkl`.

- **Preprocessing Pipeline:**  
  `utils.py` and `model_pre_processing.py` handle dynamic feature engineering including:
  - Geographical distance computation
  - GDP enrichment
  - Categorical encoding and feature filtering

- **Deployment:**  
  - Dockerized using the provided `Dockerfile`.
  - Built and pushed to Google Artifact Registry.
  - Deployed with Google Cloud Run for serverless scalability.

- **Frontend (Streamlit):**  
  User-facing interface to select flight parameters and visualize predicted prices.

<br>

## 🚀 Quickstart

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/takeoff.git
cd takeoff
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```


### 3. Train the model
```bash
python train.py
```

### 4. Launch API locally
```bash
uvicorn takeoff.api:app --reload
```
Access the API at: http://localhost:8000/predict

<br>

## 📈 Results
* Achieved robust model performance on test data (high R²).
* Designed modular pipelines for feature engineering and model training.
* Streamlined continuous deployment to the cloud for live API access.
* **Winner** across all Le Wagon Spain and Portugal cohorts.

<br>

## 🤝 Contributors
* **Adrián Marino** — LinkedIn
* Project mentored at Le Wagon Data Science Bootcamp.

---


<p align="center">
    <img src="https://github.com/adrianmarino19/eurowings-frontend/blob/9f1ac2f139b44ca42d1b69f00a039452688b2f8d/images/1.png" title="Takeoff Symbol" style="background-color: white; width: 375px; height: auto;">
</p>

# Takeoff: Flight Price Predictor AI with Eurowings

Partnered with Eurowings Digital, this project aims to predict flight prices based on several parameters. Among the tools used are: Python, pandas, scikit-learn, streamlit, Docker, and more. The output is the **<u>predicted flight price</u>** depending on the following parameters:

- Origin Airport
- Destination Airport
- Cabin Class
- Trip Type
- Direct Flight
- Trip Length
- Flight Date
- Booking Date
- Airline

Important to note that one of the most important parameters for airlines is booking date, in other words, when a client books a flight in relation to the actual flight date. Therefore, think of this tool as almost a time traveller.

:boom:<a href='https://takeoff.streamlit.app/'>Takeoff Web App</a>

## Table of Contents


## <a name='key'></a>**Key Features**


## <a name='arch'></a>**Architecture**


## <a name='hiw'></a>**How it works?**


## <a name='set'></a>**Setup & Installation**

### <a name='ins'></a>**Installation**

## <a name='dep'></a>**Deployment on Cloud**

### <a name='step'></a>**Steps to deploy**












