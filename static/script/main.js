/* Add a link location to an element in a DRY fashion.  */
function addHref(id, href)
{
	var element = document.getElementById(id);

	element.style.cursor = "pointer";
	element.onclick = function()
	{
		window.location.href = href;
	};
}

/* unhide|hide element(content_id) when element(id) is clicked.  */
function addPopOut(id, content_id)
{
	var content = document.getElementById(content_id);
	var element = document.getElementById(id)

	/* for some reason, if I set display: none as a class and
	 * apply it to html element, I have to double click. For now,
	 * the best thing to do is add display: none as inline css.
	 */

	element.style.cursor = "pointer";

	element.onclick = function()
	{
		if (content.style.display === "none") {
			content.style.display = "block";
		} else {
			content.style.display = "none";
		}
	};
}

/* Do these things when DOM is fully loaded.  */
window.onload = function()
{
	/* Pop out menu by toggling hide/unhide of element.  */
	addPopOut("about", "about_content");
	addPopOut("contact", "contact_content");
	addPopOut("portfolio", "portfolio_content");

	/* Add link location to an element.  */
	addHref("git", "https://gitlab.com/J0ND03");
	addHref("resume", "resume.html");
}
