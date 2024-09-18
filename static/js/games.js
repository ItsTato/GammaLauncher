const BaseGame = document.getElementById("base-game-template");
BaseGame.className = "invisible";

const Body = document.getElementsByTagName("body")[0];

fetch("/api/games", {
	method: "GET"
}).then(res => {
	if (!res.ok) {
		console.error("..?");
	} else {
		return res.json();
	};
}).then(data => {
	data.forEach(game => {
		let gameElement = BaseGame.cloneNode(true);
		gameElement.id = "game-" + game.ID;
		gameElement.className = "game";
		gameElement.querySelector("#game-icon").src = "/images/" + game.ThumbnailID;
		gameElement.querySelector("#game-version").innerText = `v${game.Version.Major}.${game.Version.Minor}.${game.Version.Revision}`;
		gameElement.querySelector("#game-name").innerText = game.Name;
		gameElement.querySelector("#game-description-short").innerText = game.ShortDescription;
		gameElement.querySelector("#game-more").onclick = () => {
			document.location.href = document.location.href + "/" + game.ID
		};
		gameElement.setAttribute("style",`margin-top: ${120*(game.ID-1)}px;`);
		Body.appendChild(gameElement);
	});
}).catch(error => {
	console.error(error);
});
