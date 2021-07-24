import sys
import os #debug

import joblib
import pandas as pd
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

sys.path.insert(0, "../")


app = FastAPI()
templates = Jinja2Templates(directory="templates")


def make_prediction(sl, sw, pl, pw):
    target = ["setosa", "versicolor", "virginica"]
    target_dict = {i: t for i, t in enumerate(target)}

    [sl, sw, pl, pw] = [float(var) for var in [sl, sw, pl, pw]]

    data = pd.DataFrame(
        {
            "sepal_length": [sl],
            "sepal_width": [sw],
            "petal_length": [pl],
            "petal_width": [pw],
        }
    )

    #debug
    print(os.getcwd())
    print(os.listdir("../"))
    print(os.listdir("../trained_models"))
    model = joblib.load("../trained_models/model_output.joblib")
    prediction_ = model.predict(data)[0]
    output = target_dict.get(prediction_, "None")
    print(f"Prediction is {output}")
    return output


@app.get("/", response_class=HTMLResponse)
def p1(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/predict/")
async def predict_func(
    sepal_length: str = Form(...),
    sepal_width: str = Form(...),
    petal_length: str = Form(...),
    petal_width: str = Form(...),
):

    prediction = make_prediction(sepal_length, sepal_width, petal_length, petal_width)
    return {"Prediction": prediction}
