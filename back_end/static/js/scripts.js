
function select_change() {
var z = document.getElementById("form_action").selectedIndex;
var z1 = document.getElementsByTagName("option")[z].value;
alert("Form action changed to " + z1);
}

function myfunction() {

// Calling Validation function.
//select option value from select tag and storing it in a variable.
addButtons();
var x = document.getElementById("form_action").selectedIndex;

var action = document.getElementsByTagName("option")[x].value;

document.getElementById("form_id").action = action;
document.getElementById("form_id").submit();

addButtons();
}

function addButtons() {
var para = document.createElement("P");
    var t = document.createTextNode("This is a paragraph.");
    para.appendChild(t);
    document.getElementById("myDIV").appendChild(para);

}
function changeColour(value)
{
    var color = document.body.style.backgroundColor;
    switch(value)
    {
        case 'd':
            color = "#3D3D3D";
            tree = "#000000";
        break;
        case 'l':
            color = "#AAAAAA";
            tree = "#AAAAAA";
        break;
    }
    document.body.style.backgroundColor = color;
    document.getElementsByClassName("tree")[0].style.backgroundColor= tree;
}