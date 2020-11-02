const carouselDur = 2000;


var carouselScrollInterval;

startInterval();

function startInterval() {
    carouselScrollInterval = setInterval(updateCarousel, carouselDur);
}


$('.carousel').carousel({
    interval: 0
})

function updateCarousel() {
    $('.carousel').carousel('next');
}