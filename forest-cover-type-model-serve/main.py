from fastapi import FastAPI
import pandas as pd
import numpy as np
from data import InputData, AppConfig, cover_type, ensemble_classifier_top3_model, knn_model, decision_tree_model
from pydantic_settings import BaseSettings

# app = FastAPI()
appconfig = AppConfig()
app = FastAPI(title = appconfig.app_name, 
              version = appconfig.version,
              description="A demo backend app for Forest Cover Type model serving with FastApi.")

@app.get("/")
def index():
    return appconfig.app_name

@app.get("/version")
def version():
    return appconfig.version

@app.post("/predict1")
def predict1(data: InputData):
    
    data_df = organizeData(data)
    #save
    data_df.to_csv('data.csv', index=False)

    # Make a prediction using the model
    prediction = knn_model.predict(data_df)
    #prediction value
    prediction_value = prediction[0]

    returnResult = {
        'prediction': cover_type[prediction_value],
        'prediction_value': int(prediction_value),
        # 'parcentage': str(round(np.max(ensemble_classifier_top3_model.predict_proba(data_df))*100, 2))+'%'
    }
    return returnResult

@app.post("/predict2")
def predict2(data: InputData):

    data_df = organizeData(data)
    #save
    data_df.to_csv('data.csv', index=False)

    # Make a prediction using the model
    prediction = decision_tree_model.predict(data_df)
    #prediction value
    prediction_value = prediction[0]

    returnResult = {
        'prediction': cover_type[prediction_value],
        'prediction_value': int(prediction_value),
    }
    return returnResult

@app.post("/predict3")
def predict3(data: InputData):

    data_df = organizeData(data)
    #save
    data_df.to_csv('data.csv', index=False)

    # Make a prediction using the model
    prediction = ensemble_classifier_top3_model.predict(data_df)
    #prediction value
    prediction_value = prediction[0]

    returnResult = {
        'prediction': cover_type[prediction_value],
        'prediction_value': int(prediction_value),
        # 'parcentage': str(round(np.max(ensemble_classifier_top3_model.predict_proba(data_df))*100, 2))+'%'
    }
    return returnResult

def organizeData(data: InputData):
    data_df = pd.DataFrame([dict(data)])

    for i in range(1,5):
        if(data_df['Wilderness_Area'][0] == i):
            data_df['Wilderness_Area'+str(i)] = 1
        else:
            data_df['Wilderness_Area'+str(i)] = 0
    for i in range(1,41):
        if(data_df['Soil_Type'][0] == i):
            data_df['Soil_Type'+str(i)] = 1
        else:
            data_df['Soil_Type'+str(i)] = 0

    data_df = data_df.drop(['Wilderness_Area', 'Soil_Type', 'Soil_Type15', 'Soil_Type7', 'Soil_Type8'], axis=1)

    data_df['soil_type38,39']=data_df['Soil_Type38']+data_df['Soil_Type39']
    data_df['soil_38_Wilde_area_1']=data_df['Soil_Type38']+data_df['Wilderness_Area1']
    data_df['soil_39_Wilde_area_1']=data_df['Soil_Type39']+data_df['Wilderness_Area1']

    return data_df
    