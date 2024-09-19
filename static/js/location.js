var deleteButton = document.getElementById("location-delete");

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
