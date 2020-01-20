(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 72)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 75
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-scrolled");
    } else {
      $("#mainNav").removeClass("navbar-scrolled");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

  // Magnific popup calls
  $('#portfolio').magnificPopup({
    delegate: 'a',
    type: 'image',
    tLoading: 'Loading image #%curr%...',
    mainClass: 'mfp-img-mobile',
    gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0, 1]
    },
    image: {
      tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
    }

  });


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// display the food picture at the top of the result and detail pages
var $urlResult = $('.result').attr('id');
if ($urlResult !== undefined) {
    $('header.masthead').css('background', 'linear-gradient(to bottom, rgba(92, 77, 66, 20) 0%, rgba(92, 77, 66, 0.5) 100%), url("'+ $urlResult +'") no-repeat');
    $('header.masthead').css('background-size', '1600px');
    }

var $urlDetail = $('.detail').attr('id');
if ($urlDetail !== undefined) {
    $('header.masthead').css('background', 'linear-gradient(to bottom, rgba(92, 77, 66, 20) 0%, rgba(92, 77, 66, 0.5) 100%), url("'+ $urlDetail +'") no-repeat');
    $('header.masthead').css('background-size', '1600px');
    }


// get id of element clicked in the result page for save the food
$('.save').on('click', function() {
    $.ajax({
      data : {id: this.id},
      type : 'POST',
      url : '/food/result/'
    });
    $('#' + this.id).hide();
 });

// get id of element clicked in the favorites page for delete the food
$('.delete').on('click', function() {
    $.ajax({
      data : {id: this.id},
      type : 'POST',
      url : '/food/favorites/'
    });
    $('#delete' + this.id).hide();
 });


})(jQuery); // End of use strict



