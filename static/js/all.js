var homeButton = document.getElementById("home-button");
var gamesButton = document.getElementById("games-button");
var locationsButton = document.getElementById("locations-button");
var imagesButton = document.getElementById("images-button");

homeButton.addEventListener("click", (e) => {
	document.location.href = "/";
});
gamesButton.addEventListener("click", (e) => {
	document.location.href = "/games";
});
locationsButton.addEventListener("click", (e) => {
	document.location.href = "/locations";
});
imagesButton.addEventListener("click",(e) => {
	document.location.href = "/images";
});
