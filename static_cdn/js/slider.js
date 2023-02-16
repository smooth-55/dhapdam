// carousel

$(".banner-carousel").owlCarousel({
    loop: true,
    margin: 16,
    autoplay: 3000,
    dots: true,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 1,
        },
        1000: {
            items: 1,
        },
    },
});


$(".map-carousel").owlCarousel({
    loop: true,
    margin: 16,
    autoplay: 3000,
    dots: true,
    nav: false,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 1,
        },
        1000: {
            items: 1,
        },
    },
});
$(".picture-carousel").owlCarousel({
    loop: true,
    margin: 16,
    autoplay: 3000,
    dots: true,
    nav: false,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 1,
        },
        1000: {
            items: 1,
        },
    },
});
$(".gallery-carousel").owlCarousel({
    loop: true,
    margin: 16,
    autoplay: 3000,
    dots: false,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 1.5,
        },
        1000: {
            items: 3,
        },
    },
});
$(".video-carousel").owlCarousel({
    loop: true,
    margin: 8,
    autoplay: 3000,
    dots: false,
    responsive: {
        0: {
            items: 1,
        },
        600: {
            items: 1,
        },
        1000: {
            items: 2,
        },
    },
});