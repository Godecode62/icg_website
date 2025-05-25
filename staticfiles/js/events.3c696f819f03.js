document.addEventListener('DOMContentLoaded', function() {
    // Preview d'image
    const fileInput = document.querySelector('.hse-file-upload input[type="file"]');
    const previewImg = document.getElementById('hse-preview');
    
    if(fileInput && previewImg) {
        fileInput.addEventListener('change', function(e) {
            if(this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewImg.src = e.target.result;
                };
                reader.readAsDataURL(this.files[0]);
            }
        });
    }

    // Compteur de caractères
    const textarea = document.getElementById('id_event_description');
    const charCount = document.getElementById('hse-char-count');
    
    if(textarea && charCount) {
        textarea.addEventListener('input', function() {
            const count = this.value.length;
            charCount.textContent = count;
            
            if(count > 700) {
                charCount.style.color = 'var(--hse-orange)';
            } else {
                charCount.style.color = 'var(--hse-text)';
            }
        });
    }

    // Animation des champs
    document.querySelectorAll('.hse-form-group input, .hse-form-group textarea').forEach(input => {
        input.addEventListener('focus', function() {
            this.style.borderColor = 'var(--hse-orange)';
        });
        
        input.addEventListener('blur', function() {
            if(!this.value) {
                this.style.borderColor = 'var(--hse-border)';
            }
        });
    });
});