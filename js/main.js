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
                map: map                
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
                $.getJSON("result.json", function(a) {
                    var rooms = [];
                    var letters = [];
                    letters = ["A", "B", "C", "D", "E", "F"];
                    for (var i = 0; i < 5; i++){  
                      rooms.push(a.rooms[i][0][0]);
                        console.log(a.rooms[i]);
                      var lat = a.rooms[i][0][1].lat;
                      var lng = a.rooms[i][0][1].lng; 
                      var latLng = new google.maps.LatLng(lat,lng);
                      var marker = new google.maps.Marker({
                          position: latLng,
                          map: map,
                          label: letters[i]
                          });
                    var contentString = '<p> ' + a.rooms[i][0][0] + '<p>';
                                        
                    }
                    shittylanguage(rooms);
                }
                )};
          }
          xhttp.open("GET", "PHP_Python_Test.php", true);
          xhttp.send();
    }

function shittylanguage(rooms){

    var letters = [];
    letters = ["A", "B", "C", "D", "E", "F"];
    
  for (var i = 0; i < 5; i++){ 
    var line = document.createElement("p");
    line.className = "line";
    line.innerHTML = letters[i] + ": " + rooms[i];
  document.getElementById("closestrooms").appendChild(line);
  }
}