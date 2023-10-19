import http.server
import socketserver
import requests

# Tu API Key de OpenWeatherMap
API_KEY =  "e3ddb67d4bcab798bbd1c64866750f01"
GEONAMES_USERNAME = "akricitooo"
# Función para obtener datos meteorológicos
def obtener_informacion_ubicacion(lugar):
    url = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=2&username={GEONAMES_USERNAME}"


    try:
        response = requests.get(url)
        data = response.json()
        if "geonames" in data: 
            ubicacion = data["geonames"][0]
            print(f"Nombre: {ubicacion['name']}")
            print(f"País: {ubicacion['countryName']}")
            print(f"Población: {ubicacion['population']}")
        else:
            print("Ubicación no encontrada.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/searchJSON/'):
            lugar = self.path[9:]
            resultado = obtener_informacion_ubicacion(lugar)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(resultado.encode())
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090 para openweathermap")
    httpd.serve_forever()
