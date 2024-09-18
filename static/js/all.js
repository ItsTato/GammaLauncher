var homeButton = document.getElementById("home-button");
var gamesButton = document.getElementById("games-button");

homeButton.addEventListener("click", (e) => {
	document.location.href = "/";
});
gamesButton.addEventListener("click", (e) => {
	document.location.href = "/games";
});
