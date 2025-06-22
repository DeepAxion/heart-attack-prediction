from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

# load the model
filename = 'heartattack_predictor.sav'
model = pickle.load(open(filename, 'rb'))

# define fastapi app
app = FastAPI()

class InputData(BaseModel):
    features: list[float]  # list of floats, adjust length as needed
    
@app.get("/")
def read_root():
    return {"message": "Model Deployment"}

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_array)
    label_mapping = {0: "low chance", 1: "HIGH CHANCE"}
    return {"prediction": label_mapping[prediction[0]]}
    