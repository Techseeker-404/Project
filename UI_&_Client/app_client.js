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
