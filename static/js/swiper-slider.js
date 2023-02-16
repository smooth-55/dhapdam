(function($) {
    "use strict";
var swiper = new Swiper(".newsSwiper", {
    autoplay: {
        delay: 3000,
    },
    loop: true,
    direction: "vertical",
    slidesPerView: 4,
    pagination: false,
    // pagination: {
    //     el: ".swiper-pagination",
    //     clickable: true,
    // },
});
var swiper = new Swiper(".stakeSwiper", {
    autoplay: {
        delay: 2000,
    },
    loop: true,
    direction: "vertical",
    slidesPerView: 3,
    pagination: false,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});
})(window.jQuery)