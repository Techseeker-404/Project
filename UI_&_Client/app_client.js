
 //Get value of Transmission
function getTransmn(){
    var uiTrnsm = document.getElementById("uiTrnsm");
    for(var i in uiTrnsm){
        if(uiTrnsm[i].checked){
            return str(uiTrnsm[i].value);
        }
    }
    return -1; //Invalid Value
}
//Get value of ownertype.
function getOwnertype(){
    var uiOwnertype = document.getElementById("uiOwner");
    for (var i in uiOwnertype){
        if(uiOwnertype[i].checked){
            return str(uiOwnertype[i].value);
        }
    }
    return -1; //Invalid value
}

//Calculate estimate price of Used cars sending POST method functionality to Backend.
function onClickedEstimatePrice(){
    console.log("Estimate Price Button Clicked");
    var car_name = document.getElementById("uiCarname");
    var loctn = document.getElementById("uiLocations");
    var yr = document.getElementById("uiYear");
    var km_driven = document.getElementById("uiKmdriven");
    var Fuel = document.getElementById("uiFuel");
    var Tnsm = getTransmn();
    var owner = getOwnertype();
    var mileage = document.getElementById("uiMileage");
    var Engn = document.getElementById("uiEngine");
    var power = document.getElementById("uiPower");
    //variable for Estimated price.
    var estprice = document.getElementById("uiEstimatedPrice");
     
    var url = "http://127.0.0.1:5000/predict_car_price";

   // var url = "/api/predict_car_price"; // For online deployement api call.

   $.post(url, {
    car_name:car_name.value,
    loctn:loctn.value,
    yr:parseInt(yr.value),
    km_driven:parseInt(km_driven.value),
    Fuel:Fuel.value,
    Tnsm:Tnsm,
    owner:owner,
    mileage:parseFloat(mileage.value),
    Engn:parseFloat(Engn.value),
    power:parseFloat(power.value)
 
   },function(data,status) {
       console.log(data.estimated_Price);
       estprice.innerHTML = "<h2>" + data.estimated_Price.toString()  + " Lakhs</h2>";
       console.log(status);
   });
}

// Function to load Json datas into the Location and Fuel_Type Column
function onPageload(){
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_saved_api";
    // var url = "/api/get_saved_api"; //
    $.get(url,function(data, status){
        console.log("got saved api call files responses");
        if (data){
            var locations = data.Location;
            var Fuel_type = data.Fuel_Type;
            var uilocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations){
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
            var uifuel = document.getElementById("uiFuel");
            $('#uiFuel').empty();
            for(var i in Fuel_type){
                var opt1 = new Option(Fuel_type[i]);
                $('#uiFuel').append(opt1);
            }
        }           
    });

}

window.onload = onPageload;
