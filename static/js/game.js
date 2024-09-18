var launchButton = document.getElementById("launch-game");

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
		launchButton.innerText = "Kill";
		launchButton.className = "game-launch-kill";
	};
}).catch(error => {
	console.error("Failed getting status!");
});

launchButton.addEventListener("click", (e) => {
	if (launchButton.className == "game-launch-kill") {
		launchButton.innerText = "Launch";
		launchButton.className = "game-launch";
		fetch(document.location.href + "/kill", {
			method: "POST"
		}).then(res => {
			if (res.status == 404) {
				console.error("INVALID ID ERROR! HOW?");
			}
			console.log("Game killed!");
		});
	} else {
		launchButton.innerText = "Kill";
		launchButton.className = "game-launch-kill";
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
