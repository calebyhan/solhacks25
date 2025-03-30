

//for the resources sidebar
function toggleSubMenu(categoryId) { 
     // Get the submenu based on the provided category ID
     var submenu = document.getElementById(categoryId);
    
     // Toggle the submenu display between 'none' (hidden) and 'block' (visible)
     if (submenu.style.display === "none" || submenu.style.display === "") {
        const allSubmenus = document.querySelectorAll('.submenu');
            allSubmenus.forEach(sub => {
                if (sub !== submenu) {
                    sub.style.display = 'none';  // Hide other submenus
                }
            });
        
         submenu.style.display = "block";  // Show the submenu
     } else {
         submenu.style.display = "none";   // Hide the submenu
    }
    
}

//GPT is god