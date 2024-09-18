var homeButton = document.getElementById("launch-game");

fetch(document.location.href + "/status", {
	method: "GET"
}).then(res => {
	if (res.status == 404) {
		console.error("INVALID ID ERROR! HOW?");
	} else {
		return res.json();
	};
}).then(data => {
	if (data["Running"] == true) {
		homeButton.innerText = "Kill";
		homeButton.className = "game-launch-kill";
	};
}).catch(error => {
	console.error("Failed getting status!");
});

homeButton.addEventListener("click", (e) => {
	if (homeButton.className == "game-launch-kill") {
		homeButton.innerText = "Launch";
		homeButton.className = "game-launch";
		fetch(document.location.href + "/kill", {
			method: "POST"
		}).then(res => {
			if (res.status == 404) {
				console.error("INVALID ID ERROR! HOW?");
			}
			console.log("Game killed!");
		});
	} else {
		homeButton.innerText = "Kill";
		homeButton.className = "game-launch-kill";
		fetch(document.location.href + "/launch", {
			method: "POST"
		}).then(res => {
			if (res.status == 404) {
				console.error("INVALID ID ERROR! HOW?");
			}
			console.log("Game started(ing)? !");
		});
	};
});
