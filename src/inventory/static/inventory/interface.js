(() => {
	const form = document.getElementById("search-form");
	const search = document.getElementById("search");
	const query = document.getElementById("query");
	const result = document.getElementById("result");
	const form_submit = async (event) => {
		event.stopPropagation();
		event.preventDefault();

		const params = new URLSearchParams();
		params.append("name", query.value);

		result.dispatchEvent(
			new CustomEvent("result-update", {
				detail: await fetch("/api/inventory?".concat(params.toString()), {
					headers: {
						Accepts: "application/json",
					},
				}).then((response) => {
					return response.json();
				}),
			}),
		);
	};

	search.addEventListener("click", form_submit);
	form.addEventListener("submit", form_submit);

	result.addEventListener(
		"result-update",
		(event) => {
			if (event.detail.length === 0) {
				result.innerHTML =
					document.getElementById("template-empty").textContent;
			} else {
				result.innerHTML = _.template(
					document.getElementById("template-table").textContent,
				)({ data: event.detail });
			}
		},
		false,
	);
})()