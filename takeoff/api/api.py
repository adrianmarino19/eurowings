from fastapi import FastAPI
from takeoff.predict import predict_api

app = FastAPI()


@app.get('/')
def index():
    return {'ok': True}


@app.get('/predict')
def predict():
    price = predict_api()
    return {'price': price}
