var locationButton = document.getElementById("location-choose");
var imageButton = document.getElementById("image-choose");
var gameButton = document.getElementById("game-choose");

locationButton.addEventListener("click", (e) => {
	document.location.href = "/new/location";
});
imageButton.addEventListener("click", (e) => {
	document.location.href = "/new/image";
});
gameButton.addEventListener("click", (e) => {
	document.location.href = "/new/game";
});