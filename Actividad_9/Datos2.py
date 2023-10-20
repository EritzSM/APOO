from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        suma_temperatura = 0
        suma_humedad = 0
        suma_presion = 0
        suma_velocidad_viento = 0
        direccion_viento_grados = []

        direccion_grados = {
            'N': 0, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5,
            'E': 90, 'ESE': 112.5, 'SE': 135, 'SSE': 157.5,
            'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5,
            'W': 270, 'WNW': 292.5, 'NW': 315, 'NNW': 337.5
        }

        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                if linea.startswith("Temperatura:"):
                    suma_temperatura += float(linea.split(":")[1].strip())
                elif linea.startswith("Humedad:"):
                    suma_humedad += float(linea.split(":")[1].strip())
                elif linea.startswith("Presión:"):
                    suma_presion += float(linea.split(":")[1].strip())
                elif linea.startswith("Viento:"):
                    viento_info = linea.split(":")[1].strip().split(',')
                    suma_velocidad_viento += float(viento_info[0].strip())
                    direccion = viento_info[1].strip()
                    direccion_grados[direccion]
                    direccion_viento_grados.append(direccion_grados[direccion])

        cantidad_registros = len(direccion_viento_grados)
        temperatura_promedio = suma_temperatura / cantidad_registros
        humedad_promedio = suma_humedad / cantidad_registros
        presion_promedio = suma_presion / cantidad_registros
        velocidad_viento_promedio = suma_velocidad_viento / cantidad_registros

        direccion_viento_promedio_grados = sum(direccion_viento_grados) / cantidad_registros
        direccion_viento_promedio = ''
        for direccion, grados in direccion_grados.items():
            if (direccion_viento_promedio_grados >= grados - 11.25) and (direccion_viento_promedio_grados < grados + 11.25):
                direccion_viento_promedio = direccion
                break

        return (
            temperatura_promedio,
            humedad_promedio,
            presion_promedio,
            velocidad_viento_promedio,
            direccion_viento_promedio
        )

datos = DatosMeteorologicos("datos.txt")
temperatura_promedio, humedad_promedio, presion_promedio, velocidad_viento_promedio, direccion_viento_promedio = datos.procesar_datos()
print(f"Temperatura promedio: {temperatura_promedio}°C")
print(f"Humedad promedio: {humedad_promedio}%")
print(f"Presión promedio: {presion_promedio} hPa")
print(f"Velocidad promedio del viento: {velocidad_viento_promedio} m/s")
print(f"Dirección predominante del viento: {direccion_viento_promedio}")
