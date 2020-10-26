const SM_BREAK_POINT = 576;

const pageHeader = document.querySelector('#page-header');
const humBarButton = document.querySelector('.humb-bars');
const collapsableNavbarMenu = document.querySelector('#navbarMenu');
const fadingBackground = document.querySelector('.overlay-bg');

const userNavigation = document.querySelector('#user');
const userNavList = document.querySelector('ul#usernav-list');
// Custom elements
const userMenuBarOnSmallDevice = document.createElement('div');
userMenuBarOnSmallDevice.classList.add('menubar-sm');
const userMenuBarSwitch = document.createElement('a');
userMenuBarSwitch.id = 'menubar-switch';
userMenuBarSwitch.innerText = 'Back'
userMenuBarOnSmallDevice.appendChild(userMenuBarSwitch);

const pageHeaderOriginalHeight = pageHeader.offsetHeight;
var pageHeaderResized = false;

initialSetup();


function initialSetup() {
    resizeCollapsedNavbarMenu();
    setCollapsableNavbarMenuWidth();
    setupUserMenuBar();
    

    humBarButton.addEventListener('click', function() {
        collapsableNavbarMenu.style.transition = '0.1s linear';
        if (humBarButton.classList.contains('active')) {
            humBarButton.classList.remove('active');
            collapsableNavbarMenu.classList.remove('display');
            fadingBackground.classList.remove('display');

            resetResponsiveForSmallScreen()
        } else {
            humBarButton.classList.add('active');
            collapsableNavbarMenu.classList.add('display');
            fadingBackground.classList.add('display');
        }
    })

    userMenuBarSwitch.addEventListener('click', function() {
        userMenuBarOnSmallDevice.classList.remove('display');
    })

    userNavigation.querySelector('a.menubar-switch')
        .addEventListener('click', function() {
            if (isScreenSmallerThanBreakPoint()) {
                userMenuBarOnSmallDevice.classList.add('display');
            }
    })

    onresize = function () {
        setCollapsableNavbarMenuWidth();
        collapsableNavbarMenu.style.transition = '0s linear';
        if (pageHeaderResized) {
            collapsableNavbarMenu.style.height = `${pageHeaderOriginalHeight}px`;
            pageHeaderResized = false;
        }

        resizeCollapsedNavbarMenu();
        setupUserMenuBar();
    }   
}



function resizeCollapsedNavbarMenu() {
    if (isScreenSmallerThanBreakPoint()) {
        collapsableNavbarMenu.style.height = 
            `${window.innerHeight - pageHeader.offsetHeight}px`;
        fadingBackground.style.height = collapsableNavbarMenu.style.height;
        pageHeaderResized = true;
    } else {
        resetResponsiveForSmallScreen();
    }
}


function setCollapsableNavbarMenuWidth() {
    collapsableNavbarMenu.style.width = `${pageHeader.offsetWidth - 40}px`;
}


function setupUserMenuBar() {
    console.log(userNavigation.offsetTop);
    if (isScreenSmallerThanBreakPoint()) {
        setupUserMenuBarOnSmallDevices();
    } else {
        setupUserMenuBarOnOtherDevices();
    }
}

function setupUserMenuBarOnSmallDevices() {
    userMenuBarOnSmallDevice.style.height = collapsableNavbarMenu.style.height;
    if (userNavigation.contains(userMenuBarOnSmallDevice)) return;
    userNavigation.appendChild(userMenuBarOnSmallDevice);
    userMenuBarOnSmallDevice.appendChild(userNavList);
}

function setupUserMenuBarOnOtherDevices() {
    if (!userNavigation.contains(userMenuBarOnSmallDevice)) return;
    userNavigation.appendChild(userNavList);
    userNavigation.removeChild(userMenuBarOnSmallDevice);
}

function isScreenSmallerThanBreakPoint() {
    return window.innerWidth <= SM_BREAK_POINT;
}

function resetResponsiveForSmallScreen() {
    userMenuBarOnSmallDevice.classList.remove('display');
}