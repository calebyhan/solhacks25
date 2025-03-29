// Set Mapbox access token
mapboxgl.accessToken = "pk.eyJ1IjoiY2FsZWJoYW4iLCJhIjoiY20zYWZhemx6MTJvMDJqcHhuOHpzMzIxaCJ9.Ex5-2rGapj9t0afOM2s4Yw"; // Get the Mapbox access token dynamically from Flask

function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(success, error);
    }
  }

// Initialize the map
function success(position) {
    var longitude = position.coords.longitude;
    var latitude = position.coords.latitude;

    var map = new mapboxgl.Map({
        container: 'map', // ID of the map container
        center: [longitude, latitude], // Default coordinates (Longitude, Latitude)
        zoom: 12 // Default zoom level
    });

    var marker = new mapboxgl.Marker({ draggable: true })
    .setLngLat([longitude, latitude]) // Use the user's location
    .addTo(map);

    marker.on('dragend', function() {
    var lngLat = marker.getLngLat();
    document.getElementById("location").value = lngLat.lat + ", " + lngLat.lng;
    });

    map.on('click', function(e) {
    var lngLat = e.lngLat;
    marker.setLngLat(lngLat);
    document.getElementById("location").value = lngLat.lat + ", " + lngLat.lng;
    });
}

function error(err) {
    console.warn("ERROR(" + err.code + "): " + err.message);
}

getLocation();