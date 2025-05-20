from django.http import HttpResponsePermanentRedirect

class RedirectToWWW:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        host = request.get_host()
        
        if host in ["icguinea.com", 'icg-6bg2.onrender.com']:
            #On redirige vers le bon domaine
            return HttpResponsePermanentRedirect("https://www.icguinea.com"+ request.get_full_path())
        
        return self.get_response(request)