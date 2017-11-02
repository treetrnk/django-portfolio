$(document).ready(function() {

	$('.waypoint').css({opacity: 0});

	$('.waypoint').each( function() {
		animateVisible($(this));
	});

	var titletop = $('#title-a').offset().top;
	var experiencetop = $('#experience-a').offset().top;
	var experiencebottom = $('#experience').offset().bottom;
	var portfoliotop = $('#portfolio-a').offset().top;

	$(window).on('scroll', function() {

		$('.waypoint').each( function() {
			animateVisible($(this));
		});

		if ($(window).scrollTop() >= experiencetop-75) {

			$('#logo-img tspan').addClass('logo-purple');
			$('#logo-img path').addClass('logo-purple');
			$('header nav a').addClass('text-purple');
			$('header').addClass('bg-white');


		} else {
			$('#logo-img tspan').removeClass('logo-purple');
			$('#logo-img path').removeClass('logo-purple');
			$('header nav a').removeClass('text-purple');
			$('header').removeClass('bg-white');
		}
	});

});

function animateVisible(element) {
	console.log(element.attr('id') + ' ' + element.visible());
	if (element.visible()) {
		element.show();
		element.css({opacity: 100});
		element.addClass('animated');
		element.addClass(element.data('animation'));
		element.removeClass('waypoint');
	}
}
