$(document).ready(function () {
    navbarController();
    $("#contact-btn").click(function () {
        window.location.href = 'mailto:melissawoodvine@hotmail.com?Subject=Alta Tutoring Inquiry';
        console.log("Got clicked!")
    });
});

// navbar controller

var OFFSET = 0;
function navbarController() {
    var triggerPosition = $('.nav-trigger').position().top + OFFSET;
    $(window).on("scroll", function () {
            var scrollPosition = scrollY || pageYOffset;
            if (scrollPosition > triggerPosition) {
                console.log("triggered!")
                $('header').addClass('nav-fixed');
                var navHeight = $(".nav-container").css('height');
                $('.nav-ghost').height(navHeight);
                $('.nav-ghost').show();
            } else {
                $('header').removeClass('nav-fixed');
            }


        }
    )
    ;
}