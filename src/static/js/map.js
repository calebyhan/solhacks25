// Set Mapbox access token
mapboxgl.accessToken = "pk.eyJ1IjoiY2FsZWJoYW4iLCJhIjoiY20zYWZhemx6MTJvMDJqcHhuOHpzMzIxaCJ9.Ex5-2rGapj9t0afOM2s4Yw"; // Get the Mapbox access token dynamically from Flask

// Initialize the map
var map = new mapboxgl.Map({
    container: 'map', // ID of the map container
    center: [0, 0], // Default coordinates (Longitude, Latitude)
    zoom: 2 // Default zoom level
});

// Create a draggable marker
var marker = new mapboxgl.Marker({ draggable: true })
    .setLngLat([0, 0]) // Set default location (Longitude, Latitude)
    .addTo(map);

// When the marker is dragged, update the hidden location field with the coordinates
marker.on('dragend', function() {
    var lngLat = marker.getLngLat();
    document.getElementById("location").value = lngLat.lat + ", " + lngLat.lng;
});

// Optionally, add a click event listener to the map to place the marker where the user clicks
map.on('click', function(e) {
    var lngLat = e.lngLat;
    marker.setLngLat(lngLat);
    document.getElementById("location").value = lngLat.lat + ", " + lngLat.lng;
});
