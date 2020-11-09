const carouselDur = 5000;


var carouselScrollInterval;

startInterval();
$('.carousel-component[data-component="controller"] input[type="radio"]#carousel-homepage-0').prop('checked', true);

function startInterval() {
    carouselScrollInterval = setInterval(updateCarousel, carouselDur);
}

$('.carousel').carousel({
    interval: 0
})

$('.carousel').on('slide.bs.carousel', function(data) {
    $(`.carousel-component[data-component="controller"] input[type="radio"]#carousel-homepage-${data.to}`).prop('checked', true);
})

function updateCarousel() {
    $('.carousel').carousel('next');

}

$('.carousel-component[data-component="controller"] input[type="radio"]').each(function(index) {
    $(this).on("click", function() {
        clearInterval(carouselScrollInterval);
        $('.carousel').carousel(index);
        startInterval();
    })
})