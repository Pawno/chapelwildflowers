

(function ($, document, window) {
	$(document).ready(function () {
		console.log("READY")

		// Cloning main navigation for mobile menu
		$(".mobile-navigation").append($(".main-navigation .menu").clone());

		// Mobile menu toggle 
		$(".menu-toggle").click(function () {
			$(".mobile-navigation").slideToggle();
		});

		$(".hero").flexslider({
			directionNav: false,
			controlNav: true
		});

		var map = $(".map");
		var latitude = map.data("latitude");
		var longitude = map.data("longitude");
		if (map.length) {

			map.gmap3({
				map: {
					options: {
						center: [latitude, longitude],
						zoom: 15,
						scrollwheel: false
					}
				},
				marker: {
					latLng: [latitude, longitude],
					options: {
						icon: "images/map-pin.png"
					}
				}
			});

		}

		// var waypoint = new Waypoint({
		var $section = $(".linkedSection");
		console.log("$section" + $section)
		$section.each(function () {
			console.log("links")
			console.log(this.toString())
			if (this.id == "slideshow") {
				$(this).waypoint(function () {
				$("#links").children().removeClass("current-menu-item");
				}, {
					offset: 0
				});
			} else {
				$(this).waypoint(function () {
					console.log("waypoint" + this.element.id)
					$("#" + this.element.id + "Link").toggleClass("current-menu-item").siblings().removeClass("current-menu-item");
				}, {
					offset: 0
				});
			}
		});


	});

	$(window).scroll(function () {

		// console.log("SCROLLLLLLLLLLING")
		if ($(this).scrollTop() > 1) {
			$('.siteHeader').addClass("sticky");
		} else {
			$('.siteHeader').removeClass("sticky");
		}

		// // Check if the element is visible
		// if ($('#map').is(':visible')) {
		// 	// Element is visible
		// 	console.log('Element is visible');
		// } else {
		// 	// Element is not visible
		// 	console.log('Element is not visible');
		// }
	});

	$(window).load(function () {

	});

})(jQuery, document, window);