// Carousel for video
var owl = $('.video-carousel');
owl.owlCarousel({
    loop: false,
    margin: 16,
    nav: true,
    dots: false,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    navContainer: '#videoslider .custom-nav',
    responsive: {
        0: {
            items: 1.5
        },
        500: {
            items: 2
        },
        800: {
            items: 3
        },
        1000: {
            items: 4
        },
        1400: {
            items: 6
        }
    },
    afterAction: function() {
        if (this.itemsAmount > this.visibleItems.length) {
            $('.next').show();
            $('.prev').show();

            $('.next').removeClass('disabled');
            $('.prev').removeClass('disabled');
            if (this.currentItem == 0) {
                $('.prev').addClass('disabled');
            }
            if (this.currentItem == this.maximumItem) {
                $('.next').addClass('disabled');
            }

        } else {
            $('.next').hide();
            $('.prev').hide();
        }
    }
});
// gallery
// Carousel for Popular tractor
var owl = $('.gallery-carousel');
owl.owlCarousel({
    loop: false,
    margin: 16,
    nav: true,
    dots: false,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    navContainer: '.gallery-carousel .custom-nav',
    responsive: {
        0: {
            items: 1.5
        },
        500: {
            items: 2
        },
        800: {
            items: 3
        },
        1000: {
            items: 4
        },
        1400: {
            items: 6
        }
    },
    afterAction: function() {
        if (this.itemsAmount > this.visibleItems.length) {
            $('.next').show();
            $('.prev').show();

            $('.next').removeClass('disabled');
            $('.prev').removeClass('disabled');
            if (this.currentItem == 0) {
                $('.prev').addClass('disabled');
            }
            if (this.currentItem == this.maximumItem) {
                $('.next').addClass('disabled');
            }

        } else {
            $('.next').hide();
            $('.prev').hide();
        }
    }
});
$(".gallery-carousel").owlCarousel({
    loop: false,
    margin: 16,
    autoplay: 3000,
    dots: false,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1.5
        },
        1000: {
            items: 3
        }
    }
});