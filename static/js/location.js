var revealButton = document.getElementById("location-reveal");
var deleteButton = document.getElementById("location-delete");

revealButton.addEventListener("click", (e) => {
	fetch(document.location.href, {
		method: "POST"
	}).then(res => {
		if (res.status == 404) {
			console.error("INVALID ID ERROR! HOW?");
		}
		console.log("Revealed!");
	});
});

deleteButton.addEventListener("click", (e) => {
	fetch(document.location.href, {
		method: "DELETE"
	}).then(res => {
		if (res.status == 404) {
			console.error("INVALID ID ERROR! HOW?");
		}
		console.log("Deleted!");
		document.location.href = "/";
	});
});
