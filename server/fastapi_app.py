#!/usr/bin/python3.8
import uvicorn
from fastapi import FastAPI, Form
#from starlette.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware 
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import utils
#utils.load_api_files()

app = FastAPI()

app.add_middleware (
    
    CORSMiddleware,
    allow_origins     = ["*"], 
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"],

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
    
class Price(BaseModel):    
    car_name: str  = Form(...)
    loctn: str     = Form(...)
    yr: int        = Form(...)
    km_driven: int = Form(...)
    Fuel: str      = Form(...)
    Tnsm: str      = Form(...)
    owner: str     = Form(...)
    mileage: float = Form(...)
    Engn: float    = Form(...)
    power: float   = Form(...)


@app.post("/predict_car_price",status_code=200)
async def predict_price(price: Price): 
    response = JSONResponse (

            {
                "estimated_Price": await utils.predict_car_price (
                    price.car_name, price.loctn,
                    price.yr, price.km_driven,
                    price.Fuel, price.Tnsm,
                    price.owner, price.mileage,
                    price.Engn, price.power
                    )
            }
    )       
    

    return response



if __name__ == "__main__":
    utils.load_api_files()
    uvicorn.run (
            app,
            host = '127.0.0.1',
            port = 7000,
    )


