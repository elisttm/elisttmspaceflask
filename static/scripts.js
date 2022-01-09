// toggles part of header on small width screens
function toggleHead() {
	var x = document.getElementById("topnavContent");
	if (x.className === "topnav") {
		x.className += " responsive";
	} else {
		x.className = "topnav";
}}

