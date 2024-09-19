const BaseImage = document.getElementById("base-image-template");
BaseImage.className = "invisible";

const Body = document.getElementsByTagName("body")[0];

function getImageHeightFromUrl(url,callback) {
	const img = new Image();
	img.onload = function() {
		const naturalHeight = this.naturalHeight;
		const containerWidth = 512; // 512px
		const aspectRatio = this.naturalWidth / naturalHeight
		const height = containerWidth / aspectRatio
		callback(height);
	};
	img.src = url;
};

fetch("/api/images", {
	method: "GET"
}).then(res => {
	if (!res.ok) {
		console.error("..?");
	} else {
		return res.json();
	};
}).then(data => {
	var prevMargin = 0;
	data.forEach(image => {
		let imageElement = BaseImage.cloneNode(true);
		imageElement.id = "image-" + image.ID;
		imageElement.className = "image";
		var imageHolder = imageElement.querySelector("#image-holder");
		getImageHeightFromUrl("/images/" + image.ID, (height) => {
			imageHolder.src = "/images/" + image.ID;
			imageElement.setAttribute("style", `margin-top: ${prevMargin}px;`);
			prevMargin += height + 12;
		});
		Body.appendChild(imageElement);
	});
}).catch(error => {
	console.error(error);
});