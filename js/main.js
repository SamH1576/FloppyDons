var map, infoWindow;
      function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -34.397, lng: 150.644},
          zoom: 15
        });
        infoWindow = new google.maps.InfoWindow;

        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
                
            var marker = new google.maps.Marker({
                position: pos,
                map: map,
                label: "A"
                
            });

            map.setCenter(pos);
          }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
          });
        } else {
          // Browser doesn't support Geolocation
          handleLocationError(false, infoWindow, map.getCenter());
        }
      }

      function handleLocationError(browserHasGeolocation, infoWindow, pos) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
                              'Error: The Geolocation service failed.' :
                              'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
      }
    
    function showfreerooms(){


        
          var xhttp = new XMLHttpRequest();
          xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {               
                // Create a <script> tag and set the USGS URL as the source.
                //var script = document.createElement('script');
                //script.setAttribute("id", "script");
                // This example uses a local copy of the GeoJSON stored at
                // http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojsonp
//                script.src = 'result.js';
//                document.getElementsByTagName('head')[0].appendChild(script);
//                alert();
                $.getJSON("result.json", function(a) {
//                    console.log(a.rooms);
//                    console.log(a.rooms[0][0][1].lat);
                    var rooms = [];
                    for (var i = 0; i < 5; i++){  
                      rooms.push(a.rooms[i][0][0]);
                      var lat = a.rooms[i][0][1].lat;
                      var lng = a.rooms[i][0][1].lng; 
                      var latLng = new google.maps.LatLng(lat,lng);
                      var marker = new google.maps.Marker({
                          position: latLng,
                          map: map
                          });
                      //document.getElementById("closestrooms").innerHTML = a.rooms.[i][0][0];
                    }
                    shittylanguage(rooms);
                }
                

                // Loop through the results array and place a marker for each
//                // set of coordinates.
//                a.rooms = function(results) {
//                  for (var i = 0; i < results.length; i++) {
//                  //var coords = results.features[i].geometry.coordinates;
//                      
//                      var lat = results[i][0][1].lat;
//                      var lng = results[i][0][1].lng;
//                  var latLng = new google.maps.LatLng(lat,lng);
//                  var marker = new google.maps.Marker({
//                      position: latLng,
//                      map: map
//                  });
//                  }
//                }
                )};
//                this.rooms = function(results) {
//                    
//                }
          }
          xhttp.open("GET", "PHP_Python_Test.php", true);
          xhttp.send();
    }

function shittylanguage(rooms){
  for (var i = 0; i < 5; i++){ 
    var line = document.createElement("p");
    line.className = "line";
    line.innerHTML = rooms[i];
  document.getElementById("closestrooms").appendChild(line);
  }
}