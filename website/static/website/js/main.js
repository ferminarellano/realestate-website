$(function(){
	
	// Instantiate MixItUp:
	$('#container-mix').mixItUp();
	$("#testimonial-carousel").owlCarousel({
		items: 3,
		 afterAction: function(el){
		   //remove class active
		   this
		   .$owlItems
		   .removeClass('active')
		  
		   //add class active
		   this
		   .$owlItems //owl internal $ object containing items
		   .eq(this.currentItem + 1)
		   .addClass('active')
		  
		},
        pagination : true,
        paginationNumbers: true
	});
	new WOW().init();
	
	//Smooth Scroll
	$('nav a[href*="#"]:not([href="#"])').click(function() {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
		  var target = $(this.hash);
		  target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
		  if (target.length) {
			$('html, body').animate({
			  scrollTop: target.offset().top
			}, 1000);
			return false;
		  }
		}
	  });
	
});
$(window).load(function() { // makes sure the whole site is loaded
  $('#status').fadeOut(); // will first fade out the loading animation
  $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
  $('body').delay(350).css({'overflow':'visible'});
})