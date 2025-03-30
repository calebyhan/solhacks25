

//for the resources sidebar
function toggleSubMenu(categoryId) {
    console.log("Toggling submenu for: " + categoryId); 
     // Get the submenu based on the provided category ID
     var submenu = document.getElementById(categoryId);
    
     // Toggle the submenu display between 'none' (hidden) and 'block' (visible)
     if (submenu.style.display === "none" || submenu.style.display === "") {
         submenu.style.display = "block";  // Show the submenu
     } else {
         submenu.style.display = "none";   // Hide the submenu
     }
}

//GPT is god