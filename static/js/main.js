const pageHeader = document.querySelector('#page-header');
const humBarButton = document.querySelector('.humb-bars');
const collapsableNavbarMenu = document.querySelector('#navbarMenu');
const fadingBackground = document.querySelector('.overlay-bg');

const pageHeaderOriginalHeight = pageHeader.offsetHeight;
var pageHeaderResized = false;

resizeCollapsedNavbarMenu();

humBarButton.addEventListener('click', function() {
    collapsableNavbarMenu.style.transition = '0.1s linear';
    if (humBarButton.classList.contains('active')) {
        humBarButton.classList.remove('active');
        collapsableNavbarMenu.classList.remove('display');
        fadingBackground.classList.remove('display');
    } else {
        humBarButton.classList.add('active');
        collapsableNavbarMenu.classList.add('display');
        fadingBackground.classList.add('display');
    }
})

onresize = function () {
    collapsableNavbarMenu.style.width = `${window.innerWidth - 40}px`;
    collapsableNavbarMenu.style.transition = '0s linear';
    if (pageHeaderResized) {
        collapsableNavbarMenu.style.height = `${pageHeaderOriginalHeight}px`;
        pageHeaderResized = false;
    }

    resizeCollapsedNavbarMenu();
}

function resizeCollapsedNavbarMenu() {
    if (window.innerWidth <= 576) {
        collapsableNavbarMenu.style.height = `${window.innerHeight - pageHeader.offsetHeight}px`;
        pageHeaderResized = true;
    }
}