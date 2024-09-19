var createButton = document.getElementById("image-create");

document.getElementById("image-form").addEventListener("submit", (e) => {
	e.preventDefault();
});

createButton.addEventListener("click", (e) => {
	const formData = new FormData(document.getElementById("image-form"));
	fetch(document.location.href, {
		method: "POST",
		body: formData
	}).then(res => {
		if (!res.ok) {
			console.error("Error!");
		}
		console.log("Created!");
		document.location.href = "/images";
	});
});
