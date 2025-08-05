from waitress import serve
from backend.wsgi import application  # Reemplaza 'backend' por el nombre correcto si es otro

serve(application, host="127.0.0.1", port=8081)



