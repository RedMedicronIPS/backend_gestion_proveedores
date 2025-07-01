# middleware.py
class CustomXFrameOptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Permitir framing para endpoints de documentos
        if request.path.startswith('/media/') or request.path.startswith('/documents/'):
            response['X-Frame-Options'] = 'SAMEORIGIN'
        
        return response

# Añade a MIDDLEWARE en settings.py
#MIDDLEWARE = [
#    # ... otro middleware
#    'processes.middleware.CustomXFrameOptionsMiddleware',
#]