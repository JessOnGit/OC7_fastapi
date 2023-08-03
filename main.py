"""
API REST for model serving
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
import lightgbm
import sklearn

app = FastAPI()
model = pickle.load(open('model/model.pkl', 'rb'))


# Input definition
class InputData(BaseModel):
    data: list


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict/")
async def predict(data: InputData):
    input_df = pd.DataFrame(data.data)
    predict = float(model.predict(input_df)[0])
    proba = float(model.predict_proba(input_df)[0][1])
    return {'pred': predict, "proba": proba}

