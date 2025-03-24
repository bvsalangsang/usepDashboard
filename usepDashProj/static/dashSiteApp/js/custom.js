$(document).ready(function () {
	// Remove active class from all links when a new link is clicked
	$(".nav-item .nav-link").click(function () {
		$(".nav-item .nav-link").removeClass("active");
		$(this).addClass("active");
	});

	// Check the current URL and add 'active' class to the corresponding link
	var currentUrl = window.location.pathname;

	$(".nav-item .nav-link").each(function () {
		var linkUrl = $(this).attr("href");

		// Match the current URL with href to add active class
		if (linkUrl === currentUrl) {
			$(this).addClass("active");
		}
	});
});
