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

    document.getElementById("location").value = latitude + ", " + longitude;

    window.map = new mapboxgl.Map({
        container: 'map', // ID of the map container
        center: [longitude, latitude], // Default coordinates (Longitude, Latitude)
        zoom: 12 // Default zoom level
    });

    var marker = new mapboxgl.Marker({ draggable: true })
    .setLngLat([longitude, latitude]) // Use the user's location
    .addTo(window.map);

    marker.on('dragend', function() {
    var lngLat = marker.getLngLat();
    document.getElementById("location").value = lngLat.lat + ", " + lngLat.lng;
    });

    window.map.on('click', function(e) {
    var lngLat = e.lngLat;
    marker.setLngLat(lngLat);
    document.getElementById("location").value = lngLat.lat + ", " + lngLat.lng;
    });
}

function error(err) {
    console.warn("ERROR(" + err.code + "): " + err.message);
}

function nextStep(currentStep) {
    const currentDiv = document.getElementById(`step-${currentStep}`);
    const nextDiv = document.getElementById(`step-${currentStep + 1}`);
    
    // Validate the current step before proceeding
    if (currentStep === 1) {
        const dateInput = document.getElementById("reportdate");
        if (!dateInput.value) {
            alert("Please select a date.");
            return;
        }
    }
    
    if (currentStep === 2) {
        const locationInput = document.getElementById("location");
        if (!locationInput.value) {
            alert("Please select a location.");
            return;
        }
    }

    currentDiv.style.display = "none";  // Hide the current step
    nextDiv.style.display = "block";    // Show the next step

    if (currentStep === 1) {  // Ensure this only happens when going to the map step
        setTimeout(() => {
            window.map.resize();  // Update the map size after the transition
        }, 1);  // Delay slightly to allow the display transition
    }
}

getLocation();