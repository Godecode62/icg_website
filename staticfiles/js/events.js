document.addEventListener('DOMContentLoaded', function() {
    // --- Application des classes CSS aux champs non gérés par Django Forms ---

    // Sélectionne les inputs text et textarea générés par Django et applique la classe 'hse-input'
    const inputsAndTextareas = document.querySelectorAll(
        '#id_event_name, #id_event_address, #id_event_description' // Retire #id_event_date d'ici
    );
    inputsAndTextareas.forEach(element => {
        element.classList.add('hse-input');
    });

    // Le champ id_event_date a déjà la classe 'hse-input' dans le HTML, donc pas besoin de le cibler ici.
    // Ses attributs type="date" et min="" sont aussi déjà dans le HTML.


    // --- Script pour l'aperçu de l'image ---
    const fileInput = document.getElementById('id_event_picture');
    const previewImg = document.getElementById('hse-preview');
    
    if(fileInput && previewImg) {
        // Applique la classe pour masquer l'input file réel si tu ne veux pas qu'il soit visible
        fileInput.classList.add('hse-input-file'); 

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
    const maxLength = 1500; 

    if(textarea && charCount) {
        charCount.textContent = textarea.value.length; // Initialiser au chargement

        textarea.addEventListener('input', function() {
            const count = this.value.length;
            charCount.textContent = count;
            
            if(count > maxLength) {
                charCount.style.color = 'red';
            } else {
                charCount.style.color = '#FF6D00'; // Couleur orange directe
            }
        });
    }

    // --- Animation des champs (focus/blur) ---
    // Cette partie est en grande partie gérée par le CSS via :focus.
    // On peut la laisser pour les champs qui ont la classe hse-input.
    document.querySelectorAll('.hse-input').forEach(input => {
        input.addEventListener('focus', function() {
            // Le CSS gère déjà border-color et box-shadow
        });
        
        input.addEventListener('blur', function() {
            if(!this.value) {
                this.style.borderColor = 'var(--hse-border)';
            }
        });
    });
});