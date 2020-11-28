from flask import Flask,jsonify,request
import utils


app = Flask(__name__)
@app.route('/get_saved_api',methods=['GET'])
def get_saved_api():
    response = jsonify({
        'car_model_names':utils.get_names(),
        'Location':utils.get_locations(),
        'Owner_Type':utils.get_own_type(),
        'Fuel_Type':utils.get_fuel(),
        'Transmission':utils.get_tranmn(),

    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_car_price', methods=['GET','POST'])      #['GET','POST'])
def predict_price():
    car_name = request.form['car_name']
    loctn = request.form['loctn']
    yr = int(request.form['yr'])
    km_driven = int(request.form['km_driven'])
    Fuel = request.form['Fuel']
    Tnsm = request.form['Tnsm']
    owner = request.form['owner']
    mileage = float(request.form['mileage'])
    Engn = float(request.form['Engn'])
    power = float(request.form['power'])

    response = jsonify({
        'estimated_Price':utils.predict_car_price(car_name,loctn,yr,km_driven,Fuel,Tnsm,owner,mileage,Engn,power)
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    utils.load_api_files()
    app.run()