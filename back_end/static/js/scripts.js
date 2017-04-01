
function select_change() {
var z = document.getElementById("form_action").selectedIndex;
var z1 = document.getElementsByTagName("option")[z].value;
alert("Form action changed to " + z1);
}

function myfunction() {

// Calling Validation function.
//select option value from select tag and storing it in a variable.
var x = document.getElementById("form_action").selectedIndex;

var action = document.getElementsByTagName("option")[x].value;

document.getElementById("form_id").action = action;

document.getElementById("form_id").submit();

}
