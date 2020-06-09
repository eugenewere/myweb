/* Template Name: Cristino - Responsive Personal Template
   Author: Shreethemes
   Version: 1.0.0
   Created: August 2019
   File Description: Main JS file of the template
*/

/************************/
/*       INDEX          */
/*=======================
 *  01.  Menu           *
 *  02.  Scrollspy      *
 *  03.  Loader         *
 *  04.  Back to top    *
 =======================*/

! function($) {
    "use strict";
    //*********************/ 
    //         Menu       */
    //*********************/ 
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        if (scroll >= 50) {
            $(".sticky").addClass("nav-sticky");
        } else {
            $(".sticky").removeClass("nav-sticky");
        }
    });

    $('.navbar-nav a, .mouse-down').on('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 0
        }, 2500, 'easeInOutExpo');
        event.preventDefault();
    });


    //*********************/ 
    //      Scrollspy     */
    //*********************/ 
    $(".navbar-nav").scrollspy({ offset: 70 });


    //*********************/ 
    //       Loader       */
    //*********************/ 
    $(window).on('load', function() {
        $('#status').fadeOut();
        $('#preloader').delay(350).fadeOut('slow');
        $('body').delay(350).css({
            'overflow': 'visible'
        });
    });


    //*********************/ 
    //    BACK TO TOP     */
    //*********************/ 
    $(window).scroll(function(){
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn();
        } else {
            $('.back-to-top').fadeOut();
        }
    }); 

    $(".back-to-top").on("click", function() {
        $("html, body").animate({ scrollTop: 0 }, 3000);
        return false;
    });
}(jQuery);




// =========================================================================

// {#CKEDITOR.replace( 'comment' );#}
//              ClassicEditor
//                 .create( document.querySelector( '#comments' ) )
//                 .then( editor => {
//                         console.log( editor );
//                 } )
//                 .catch( error => {
//                         console.error( error );
//                 } );


            $(document).ready(function() {

               $("#owl-example").owlCarousel({
                   items:1,

                   autoplay: 2000,
                   autoplayHoverPause: true,
                   animateOut: 'fadeOut',
                   animateIn: 'fadeIn',
                   // {#navigation:true,#}
                   navText: ["<span class='ion-md-arrow-back'></span>", "<span class='ion-chevron-right'></span>"],
                   navigation : true,
                    navigationText : ["prev","next"],
                    rewindNav : true,
                    scrollPerPage : true,

               });

            });


                var $animation_elements = $('.overlay-animated');
                var $window = $(window);

                function check_if_in_view() {
                  var window_height = $window.height();
                  // {#console.log(window_height);#}
                  var window_top_position = $window.scrollTop();
                  // {#console.log(window_top_position);#}
                  var window_bottom_position = (window_top_position + window_height);
                  // {#console.log(window_bottom_position);#}

                  $.each($animation_elements, function() {
                    var $element = $(this);
                    var element_height = $element.outerHeight();
                    // {#console.log(element_height);#}
                    var element_top_position = $element.offset().top;
                    var element_bottom_position = (element_top_position + element_height);

                    //check to see if this current container is within viewport
                    if ((element_bottom_position >= window_top_position) &&
                        (element_top_position <= window_bottom_position)) {
                      $element.addClass('animate-it');
                    } else {
                      $element.removeClass('animate-it');
                    }
                  });
                }

                $window.on('scroll resize', check_if_in_view);
                $window.trigger('scroll');




                // socialholder
                var timeout;
                var social_holder = document.getElementById("social-holder");

                document.ontouchmove= function(){
                     social_holder.style.right=5+"px";
                  clearTimeout(timeout);
                  timeout = setTimeout(function(){
                      social_holder.style.right= -65+"px";

                  }, 3000);
                };
                document.onmousemove = function(){
                     social_holder.style.right=5+"px";
                  clearTimeout(timeout);
                  timeout = setTimeout(function(){
                      social_holder.style.right= -65+"px";

                  }, 3000);
                };
                // socialholder

