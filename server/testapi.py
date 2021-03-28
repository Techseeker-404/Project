#!/usr/bin/python3.8
import uvicorn
from fastapi import FastAPI, Form
#from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.responses import JSONResponse
import utils

app = FastAPI()

origins = [
    "*",
    "http://127.0.0.1:",         
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:8080",         
]
app.add_middleware (
    
    CORSMiddleware,
    allow_origins = origins, 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],

)

@app.get("/get_saved_api")
async def get_saved_api():
    response = JSONResponse (
            {

                'car_model_names':utils.get_names(),
                'Location':utils.get_locations(),
                'Owner_Type':utils.get_own_type(),
                'Fuel_Type':utils.get_fuel(),
                'Transmission':utils.get_tranmn(),
                    
            }
    )

    return response
"""
    Post method for predicting price.
"""
    
@app.post("/predict_car_price",status_code=200)
async def predict_price( 
                          car_name: str = Form(...), 
                          loctn: str = Form(...),
                          yr: int = Form(...),
                          km_driven: int = Form(...),
                          Fuel: str = Form(...),
                          Tnsm: str = Form(...),
                          owner: str = Form(...),
                          mileage: float = Form(...),
                          Engn: float = Form(...),
                          power: float = Form(...)
                       ):


    response = JSONResponse (

            {
                "estimated_Price": utils.predict_car_price (
                    car_name, loctn,
                    yr, km_driven,
                    Fuel, Tnsm,
                    owner, mileage,
                    Engn, power
                    )
            }
    )       
    

    return response



if __name__ == "__main__":
    utils.load_api_files()
    uvicorn.run (
            app,
            host='127.0.0.1',
            port=5000,
    )




