function responsive_menu() {
    var x = document.getElementById("responsive-menu-item-container");
    if (x.className === "responsive-menu-list") {
        x.className += " show-menu";
    } 
    else {
        x.className = "responsive-menu-list";
    }
}