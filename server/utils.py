import json
import pickle as pck
import pandas as pd
import asyncio
import warnings
warnings.filterwarnings("ignore")

#initialising web app variables for Price prediction.
__data = None
__car_model_name = None
__location = None
__owner_type = None
__fuel = None
__transmission = None
__model = None

"""
 model section, this is the core functional code section where our primary objective of
 prediction happens.

"""   
async def predict_car_price(car_name,loctn,yr,km_driven,Fuel,
                      Tnsm,owner,mileage,Engn,power):
    try:                 
        new_df = pd.DataFrame({
                    "Name":car_name,
                    "Location":loctn,
                    "Year":yr,
                    "Kilometers_Driven":km_driven,
                    "Fuel_Type":Fuel,
                    "Transmission":Tnsm,
                    "Owner_Type":owner,
                    "Mileage":mileage,
                    "Engine":Engn,
                    "Power":power,

                },index=[0])
        #print("Predicted price of the car in lakhs.")
        #return new_df
        return round(__model.predict(new_df)[0],3).astype(str) 
    except TypeError:
        raise("Check out the values entered ,shouldn't leave any columns blank")

"""   
 function to load "API" calling dependencies for web app as this serve as model and detail serving 
 section of the app.

"""
def load_api_files():
    print("loading api dependecies...")
    global __data 
    global __car_model_name 
    global __location 
    global __owner_type
    global __fuel 
    global __transmission
    global __model 

    with open("./api_call_files/data.json",'r')as f:
        __data = json.load(f)
        #utilize dictionary get vlaue method for a specific key as json is eqv to python dict
        __car_model_name = __data.get("names")
        __location = __data.get("location")
        __owner_type = __data.get("owner")
        __fuel = __data.get("fuel")
        __transmission = __data.get("tnsmn")
     # lodaing saved machine learning model for prediction  
    if __model is None:
        with open("./api_call_files/xgbmodel.pickle",'rb')as f:
            __model = pck.load(f)

    print("api dependecies...loaded.")

def get_names():
    return __car_model_name
def get_locations():
    return __location
def get_own_type():
    return  __owner_type
def get_fuel():
    return __fuel
def get_tranmn():
    return __transmission

"""
    Main function to run predict function.
"""
async def main():
    print(await predict_car_price("Maruti alto","Thiruvananthapuram",2011,34007,"Petrol","Manual","Second",21,848.0,67))
    print(await predict_car_price("Ford Ecosport","Delhi",2014,45007,"Diesel","Manual","Second",17,1498.0,99))
    
## run ##
if __name__ == "__main__":
    load_api_files()
    #just check
    print(get_locations())
    asyncio.run(main())
