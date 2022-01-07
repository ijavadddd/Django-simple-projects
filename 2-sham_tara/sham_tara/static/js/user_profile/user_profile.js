function responsive_user_profile_menu(){
    var menu = document.getElementById("vertical-menu-container");
    if (menu.className === "sidebar-menu-container") {
        menu.className += " show-menu";
    } 
    else {
        menu.className = "sidebar-menu-container";
    }
}