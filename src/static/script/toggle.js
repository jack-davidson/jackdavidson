function toggle(content_id)
{
	var content = document.getElementById(content_id);
	if (content.style.display === "none") {
		content.style.display = "block";
	} else {
		content.style.display = "none";
	}
}
