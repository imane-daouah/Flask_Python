document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".skill-progress span").forEach(function (span) {
        let targetWidth = parseInt(span.getAttribute("data-width")); // Récupère la valeur numérique de "data-width"
        let currentWidth = 0; // Démarre à 0%
        let animationSpeed = 10; // Temps entre chaque mise à jour (ms)
        let increment = targetWidth / 50; // Ajuste la progression (plus fluide et rapide)

        let interval = setInterval(function () {
            if (currentWidth >= targetWidth) {
                span.style.width = targetWidth + "%"; // Fixe exactement la largeur cible
                clearInterval(interval); // Stoppe l'animation
            } else {
                currentWidth += increment; // Augmente progressivement
                span.style.width = currentWidth + "%"; // Applique la largeur
            }
        }, animationSpeed);
    });
});
