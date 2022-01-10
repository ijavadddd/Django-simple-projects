function responsive_menu() {
    var x = document.getElementById("responsive-menu-item-container");
    if (x.className === "responsive-menu-list") {
        x.className += " show-menu";
    } 
    else {
        x.className = "responsive-menu-list";
    }
}
function open_login_form() {
    var x = document.getElementById("login-register-container");
    if (x.className === "login-register-container") {
        x.className += " show-form";
    } 
    else {
        x.className = "login-register-container";
    }
}
function close_login_form() {
    var x = document.getElementById("login-register-container");
    if (x.className === "login-register-container") {
        x.className += "show-form";
    } 
    else {
        x.className = "login-register-container";
    }
}