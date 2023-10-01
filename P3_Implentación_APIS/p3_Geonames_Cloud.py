import requests

def obtener_informacion_ubicacion(geonames_username, lugar):
    url1 = f"http://api.geonames.org/searchJSON?name={lugar}&maxRows=1&username={geonames_username}"

    try:
        response = requests.get(url1)
        data = response.json()
        if "geonames" in data and data["geonames"]:
            ubicacion = data["geonames"][0]
            print(f"Nombre: {ubicacion['name']}")
            print(f"País: {ubicacion['countryName']}")
            print(f"Población: {ubicacion['population']}")     
            obtener_datos_meteorologicos(api_key,ubicacion['name'])    
        else:
            print("Ubicación no encontrada.")
    except Exception as e:
        print(f"Error: {str(e)}")

def obtener_datos_meteorologicos(api_key, ciudad):
    url2 = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"

    try:
        response = requests.get(url2)
        data = response.json()
        if "main" in data and "weather" in data:
            temperatura = data["main"]["temp"] - 273.15  # Convertir de Kelvin a Celsius
            condiciones_climaticas = data["weather"][0]["description"]
            print(f"Temperatura: {temperatura:.2f}°C")
            print(f"Condiciones Climáticas: {condiciones_climaticas}")
        else:
            print("Datos meteorológicos no disponibles.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Coloca tu usuario de geonames
    geonames_username = "akricitooo"

    lugar = "Mexico"  # Cambia esto a la ubicación que desees consultar
    obtener_informacion_ubicacion(geonames_username, lugar)

    # Tu API key de openweathermap
    api_key = "e3ddb67d4bcab798bbd1c64866750f01"  # Tu API key