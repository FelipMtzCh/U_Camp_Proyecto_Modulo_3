import numpy as np
import matplotlib.pyplot as plt

# Número total de canicas a simular
num_canicas = 3000
# Número de niveles
niveles = 12

canicas = []

def simularCanicas():
    """
    Simula el comportamiento de una máquina de Galton.

    Cada canica pasa por varios niveles (12 en este caso),
    y en cada nivel decide aleatoriamente ir a la izquierda (0)
    o a la derecha (1).

    Retorna:
        list: Lista con la posición final de cada canica.
    """

    # Lista donde se guardarán las posiciones finales
    posiciones = []

    # Simular cada canica
    for i in range(num_canicas):
        # Contador de cuántas veces la canica fue a la derecha
        posicion_final = 0
        # Cada nivel representa una decisión (izquierda o derecha)
        for n in range(niveles):
            # Genera 0 (izquierda) o 1 (derecha) de forma aleatoria
            lado = np.random.randint(0, 2)
            # Se suma 1 solo si va a la derecha
            posicion_final = posicion_final + lado

        # Se guarda la posición final de la canica
        posiciones.append(posicion_final)

    # Se devuelve la lista completa de resultados
    return posiciones

def crearHistograma(*canicas):
    """
    Crea un histograma a partir de las posiciones finales
    de las canicas.

    Parámetro:
        canicas (list): Lista con las posiciones finales.
    """

    # Genera el histograma
    # bins=niveles, para dividir los datos en 12 grupos
    plt.hist(canicas, bins=niveles, color='#bb8fce', edgecolor='#4a235a')

    # Título del gráfico
    plt.title("Simulación de la Máquina de Galton")
    # Etiqueta del eje X (valores finales posibles)
    plt.xlabel("Distribución de canicas")
    # Etiqueta del eje Y (cantidad de canicas en cada posición)
    plt.ylabel("Cantidad de canicas")
    # Muestra el gráfico en pantalla
    plt.show()

# Mensaje inicial
print("Simulación de Máquina de Galton")
# Ejecuta la simulación
canicas = simularCanicas()
# Genera el histograma con los resultados
crearHistograma(canicas)
