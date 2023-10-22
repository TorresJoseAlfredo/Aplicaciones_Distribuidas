import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9090'

def obtener_temperatura(pais):
    url = f'{url_base}/spotify/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'El album más escuchado en {pais} es: {data["spotify"]}'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Ejemplos de uso

# Solicitar al usuario el nombre del país
#paises = input('Por favor, ingrese el nombre del país: ')
paises = ["Argentina", "Brazil", "Chile", "Colombia", "Mexico"]
for pais in paises:
    resultado = obtener_temperatura(pais)
    print(resultado)
    
    
 