function responsive_menu(){
    var menu = document.getElementById("primary-mobile-menu-container");
    if (menu.className === "header-mobile-menu") {
        menu.className += " show-menu";
    } 
    else {
        menu.className = "header-mobile-menu";
    }
}