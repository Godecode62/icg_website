let slideIndex = 1;
let autoSlideTimeout;

// Initialiser le diaporama
document.addEventListener('DOMContentLoaded', function() {
    showSlides(slideIndex);
    startAutoSlide();
});

// Fonctions de contrôle
function plusSlides(n) {
    clearTimeout(autoSlideTimeout);
    showSlides(slideIndex += n);
    startAutoSlide();
}

function currentSlide(n) {
    clearTimeout(autoSlideTimeout);
    showSlides(slideIndex = n);
    startAutoSlide();
}

function showSlides(n) {
    let slides = document.getElementsByClassName("carousel-slide");
    let dots = document.getElementsByClassName("dot");

    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }

    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
    }
    for (let i = 0; i < dots.length; i++) {
        dots[i].classList.remove("active");
    }

    slides[slideIndex - 1].classList.add("active");
    dots[slideIndex - 1].classList.add("active");
}

// Fonction pour le diaporama automatique
function startAutoSlide() {
    autoSlideTimeout = setTimeout(function() {
        plusSlides(1);
    }, 7000);
}