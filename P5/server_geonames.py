import http.server
import socketserver
import json
import random

# Datos ficticios de poblacion para países de América Latina
poblacion = {
    "Argentina": random.randint(1000000, 500000000) ,
    "Brazil": random.randint(1900000, 600000000),
    "Chile": random.randint(1000000, 200000000),
    "Colombia": random.randint(1000000, 200000000),
    "Mexico": random.randint(100000, 200000000),
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/poblacion/'):
            pais = self.path[11:]
            if pais in poblacion:
                data = {"poblacion": poblacion[pais]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090")
    httpd.serve_forever()