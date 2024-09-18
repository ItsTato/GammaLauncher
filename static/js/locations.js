const BaseLocation = document.getElementById("base-location-template");
BaseLocation.className = "invisible";

const Body = document.getElementsByTagName("body")[0];

fetch("/api/locations", {
	method: "GET"
}).then(res => {
	if (!res.ok) {
		console.error("..?");
	} else {
		return res.json();
	};
}).then(data => {
	data.forEach(location => {
		let locationElement = BaseLocation.cloneNode(true);
		locationElement.id = "location-" + location.ID;
		locationElement.className = "location";
		locationElement.querySelector("#location-name").innerText = location.Name;
		locationElement.querySelector("#location-path").innerText = location.Path;
		locationElement.querySelector("#location-more").onclick = () => {
			document.location.href = document.location.href + "/" + location.ID;
		};
		locationElement.querySelector("#location-reveal").onclick = () => {
			fetch(document.location.href + "/" + location.ID + "/reveal", {
				method: "POST"
			}).then(res => {
				if (res.status == 404) {
					console.error("INVALID ID ERROR! HOW?");
				}
				console.log("Reavled!");
			});
		}
		locationElement.setAttribute("style", `margin-top: ${120 * (location.ID - 1)}px;`);
		Body.appendChild(locationElement);
	});
}).catch(error => {
	console.error(error);
});