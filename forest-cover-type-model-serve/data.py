import pickle
from pydantic import BaseModel
from pydantic_settings import BaseSettings
import pandas as pd

class AppConfig(BaseSettings):
    app_name: str = "Forest Cover Type Prediction"
    version: str = "0.1"

class InputData(BaseModel):
    Elevation: int
    Aspect: int
    Slope: int
    Horizontal_Distance_To_Hydrology: int
    Vertical_Distance_To_Hydrology: int
    Horizontal_Distance_To_Roadways: int
    Hillshade_9am: int
    Hillshade_Noon: int
    Hillshade_3pm: int
    Horizontal_Distance_To_Fire_Points: int
    Wilderness_Area: int
    Soil_Type: int

# Create the object for cover_type
cover_type = {
    0: 'Spruce/Fir',
    1: 'Lodgepole Pine',
    2: 'Ponderosa Pine',
    3: 'Cottonwood/Willow',
    4: 'Aspen',
    5: 'Douglas-fir',
    6: 'Krummholz'
}

# Load the model from the file
with open('./models/knn_model.pkl', 'rb') as file:
    knn_model = pickle.load(file)

with open('./models/decision_tree_model.pkl', 'rb') as file:
    decision_tree_model = pickle.load(file)

with open('./models/ensemble_classifier_top3_model.pkl', 'rb') as file:
    ensemble_classifier_top3_model = pickle.load(file)
    

