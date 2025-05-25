document.addEventListener('DOMContentLoaded', function() {
    // --- Application des classes CSS et attributs via JavaScript ---

    // Sélectionne tous les inputs text, date et textarea générés par Django
    // et applique la classe 'hse-input'
    const inputsAndTextareas = document.querySelectorAll(
        '#id_event_name, #id_event_date, #id_event_address, #id_event_description'
    );
    inputsAndTextareas.forEach(element => {
        element.classList.add('hse-input');
    });

    // Pour l'input de date : s'assurer qu'il est de type "date" et définir l'attribut "min"
    const dateInput = document.getElementById('id_event_date');
    if (dateInput) {
        dateInput.setAttribute('type', 'date'); // Garantit que le navigateur affiche un sélecteur de date
        const today = new Date().toISOString().split('T')[0]; // Récupère la date du jour au format YYYY-MM-DD
        dateInput.setAttribute('min', today); // Empêche la sélection de dates passées
    }

    // Pour l'input de fichier : Django le rendra avec l'id_event_picture
    // Le CSS le cachera, et le label stylisé sera utilisé.
    const fileInput = document.getElementById('id_event_picture');
    if (fileInput) {
        // Applique une classe si tu as besoin de styles spécifiques pour l'input file lui-même (même s'il est masqué)
        fileInput.classList.add('hse-input-file'); 
        // Tu peux ajouter des attributs ici aussi si nécessaire, par exemple, un accept=""
        // fileInput.setAttribute('accept', 'image/png, image/jpeg, image/jpg');
    }

    // --- Script pour l'aperçu de l'image ---
    const previewImg = document.getElementById('hse-preview');
    if(fileInput && previewImg) {
        fileInput.addEventListener('change', function(e) {
            if(this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewImg.src = e.target.result;
                };
                reader.readAsDataURL(this.files[0]);
            } else {
                // Remet l'image par défaut si aucun fichier n'est sélectionné
                previewImg.src = "{% static 'images/hse-default.jpg' %}"; 
            }
        });
    }

    // --- Compteur de caractères pour la description ---
    const textarea = document.getElementById('id_event_description');
    const charCount = document.getElementById('hse-char-count');
    const maxLength = 1500; // Doit correspondre à la validation de ton modèle si tu en as une

    if(textarea && charCount) {
        // Met à jour le compteur au chargement initial
        charCount.textContent = textarea.value.length;
        if(textarea.value.length > maxLength) {
            charCount.style.color = 'red'; // Rouge si dépasse la limite
        } else {
            charCount.style.color = '#FF6D00'; // Orange vif si dans la limite
        }

        textarea.addEventListener('input', function() {
            const count = this.value.length;
            charCount.textContent = count;
            
            if(count > maxLength) {
                charCount.style.color = 'red';
            } else {
                charCount.style.color = '#FF6D00'; // Utilise la couleur orange directe
            }
        });
    }

    // --- Animation des champs (focus/blur) ---
    // Cette partie est en grande partie gérée par le CSS :focus
    // Mais on peut la garder pour des effets supplémentaires si nécessaire.
    document.querySelectorAll('.hse-input').forEach(input => {
        input.addEventListener('focus', function() {
            // Le CSS gère déjà border-color et box-shadow
            // Tu peux ajouter d'autres effets JS ici si besoin
        });
        
        input.addEventListener('blur', function() {
            if(!this.value) {
                this.style.borderColor = 'var(--hse-border)'; // Réinitialise si vide
            }
        });
    });
});