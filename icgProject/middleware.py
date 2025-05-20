from django.http import HttpResponsePermanentRedirect

class RedirectToWWW:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        host = request.get_host().split(':')[0]  # Enlève le port (ex: "example.com:8000" → "example.com")
        
        # Liste des domaines à rediriger vers www.icguinea.com
        domains_to_redirect = ["icguinea.com", "icg-6bg2.onrender.com"]
        
        # Si le domaine est dans la liste OU si c'est HTTP (même pour www.icguinea.com)
        if (host in domains_to_redirect) or (not request.is_secure()):
            new_url = "https://www.icguinea.com" + request.get_full_path()
            return HttpResponsePermanentRedirect(new_url)
        
        return self.get_response(request)