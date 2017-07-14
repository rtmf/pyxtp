$(document).ready(function() {
	// Header Scroll
	$(window).on('scroll', function() {
		var scroll = $(window).scrollTop();

		if (scroll >= 50) {
			$('#header').addClass('fixed');
		} else {
			$('#header').removeClass('fixed');
		}
	});

	// Page Scroll
	var sections = $('section')
		nav = $('nav[role="navigation"]');

	$(window).on('scroll', function () {
	  	var cur_pos = $(this).scrollTop();
	  	sections.each(function() {
	    	var top = $(this).offset().top - 76
	        	bottom = top + $(this).outerHeight();
	    	//if (cur_pos >= top && cur_pos <= bottom) {
	      		//nav.find('a').removeClass('active');
	      		//nav.find('a[href="#'+$(this).attr('id')+'"]').addClass('active');
	    	//}
	  	});
	});
    
    //filtro in base alla id -> classe
    var $btnfilter = $('.filterbtn').click(function() {
      if (this.id == 'all') {
        $('.products-list > li').fadeIn(450);
      } else {
        var $el = $('.' + this.id).fadeIn(450);
        $('.products-list > li').not($el).hide();
      }
      $btnfilter.removeClass('active');
      $(this).addClass('active');
    })
    //filtro in base alla id -> classe END
    
	
	
	//smooth scrolling per link #buy
	$('a[href^="#contact"]').on('click',function (e) {
	    e.preventDefault();

	    var target = this.hash;
	    var $target = $(target);

	    $('html, body').stop().animate({
	        'scrollTop': $target.offset().top
	    }, 900, 'swing', function () {
	        window.location.hash = target;
	    });
	});
	

	$('.banner').click(function(){
		$('li.menu-tendina').removeClass('active');
		$('.menu-tendina a').removeClass('open-sub');
	})

	// Mobile Navigation
	$('.nav-toggle').on('click', function() {
		$(this).toggleClass('close-nav'); 
		nav.toggleClass('open');
		if(!$('.nav-toggle').hasClass('close-nav')){ //passo da mobile a desktop e chiudo X, chiudo .tendina
			$('li.menu-tendina').removeClass('active');
			$('.menu-tendina a').removeClass('open-sub');
		}
		$('body').toggleClass('overflow-hidden');
		return false;
	});	


	//drop-dow menu
	var visibile = $('a.nav-toggle').css('display');
    if (visibile=='none'){                          //main if
		$('.menu-tendina').mouseover(function () {
			$(this).find('.tendina').addClass('mostra');
			$(this).find('a').addClass('open-sub'); /*muovo freccia anche con mouse over*/
		});

		$('.menu-tendina').mouseleave(function () {
			$(this).find('.tendina').removeClass('mostra');
			$(this).find('a').removeClass('open-sub');
		});
    }else{
	 
		$('.primary-nav li a').click(function(e){
			e.stopPropagation(); //rende funzionante il clic bloccando .banner.click
			if($(this).parent().hasClass('menu-tendina')){ //if fuori

				if(!$(this).parent().hasClass('active')) { //if dentro
					$('li.menu-tendina').removeClass('active');
					$('.menu-tendina a').removeClass('open-sub');
					$(this).parent().addClass('active');
					$(this).addClass('open-sub');
					//se passo dalla modalità mobile a desktop e chiudo X NO CONTROLLO QUI
					//non funziona
					//$('.close-nav').on('click', function() {
					//	$('li.menu-tendina').removeClass('active');
					//    $('.menu-tendina a').removeClass('open-sub');
					//}
					
					//da provare click esterno
					//$(document).click(function(){
                    //$("#dropdown").hide();
                    //});
					e.preventDefault();
				} else {
					return true;} //fine if dentro

			} 
			else{
				$('li.menu-tendina').removeClass('active');
				$('.menu-tendina a').removeClass('open-sub');} //fine if fuori
			
		}); //fine click event

	
    } //fine main else if

});

