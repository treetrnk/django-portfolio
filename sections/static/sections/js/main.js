$(document).ready(function() {
	
	$('#experience .progress-bar').css({width: 0}, 1);
	$('#experience .progress-bar').hide();
	animateProgress();

	var titletop = $('#title-a').offset().top;
	var experiencetop = $('#experience-a').offset().top;
	var experiencebottom = $('#experience').offset().bottom;
	var portfoliotop = $('#portfolio-a').offset().top;

	$(window).on('scroll', function() {
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

		animateProgress();

	});

});

function animateProgress() {
	console.log('win top ' + $(window).scrollTop());
	console.log('win hi ' + $(window).height());
	console.log('exp top ' + $('#experience-a').offset().top);
	console.log('exp hi ' + $('#experience').height());
	if ($(window).scrollTop() + $(window).height() >= $('#experience-a').offset().top + $('#experience').height() + 75) {
		if (!$('#experience').hasClass('animated')) {
			var timer = 0;
			var rate = 250;

			$('.progress-bar').each(function() {
				var $this = $(this);
				var newWidth = $(this).data('perc') + '%';

				setTimeout(function() {
					$('#experience .progress-bar').fadeIn('slow');
					$this.animate({width: newWidth}, 1000, 'linear');
				}, timer);
				
				timer = timer + rate;
			});

			$('#experience').addClass('animated');
		}
	}
}
