import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9090'

def obtener_temperatura(pais):
    url_spotify = f'{url_base}/spotify/{pais}'
    
    url_temp = f'{url_base}/temperature/{pais}'
    
    response = requests.get(url_spotify)
    if response.status_code == 200:
        data1 = response.json()
        
        response = requests.get(url_temp)
        if response.status_code == 200:
            data = response.json()
            return f'El album más escuchado en {pais} es: {data1["spotify"]}\nTemperatura en {pais}: {data["temperature"]:.2f}°C'      
        elif response.status_code == 404:
            return f'Temp País no encontrado: {pais}'
        else:
            return f'Error en la solicitud: Código {response.status_code}'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Ejemplos de uso

# Solicitar al usuario el nombre del país
paises = input('Por favor, ingrese el nombre del país: ')
#paises = ["Argentina", "Brazil", "Chile", "Colombia", "Mexico"]
#for pais in paises:
resultado = obtener_temperatura(paises)
print(resultado)
    
    
 