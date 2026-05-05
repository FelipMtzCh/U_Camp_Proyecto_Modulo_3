# U_Camp_Proyecto_Modulo_3

## Descripción

Este proyecto consiste en la simulación de una **Máquina de Galton**, donde varias canicas pasan por distintos niveles de obstáculos que las desvían hacia la izquierda o la derecha.
Al final, las canicas caen en diferentes contenedores. La probabilidad de caer en cada uno depende de qué tan cerca esté del centro.

---

## Librerías utilizadas

- **NumPy**  
  Se utiliza la función `randint` para simular si la canica se mueve a la izquierda (0) o a la derecha (1).

- **Matplotlib**  
  Se utiliza para crear un histograma que representa la cantidad de canicas en cada contenedor.

---

## Funcionamiento del programa

1. Se definen las variables para:
   - Cantidad de canicas  
   - Número de niveles  
   - Lista para almacenar resultados  

2. Se crea la función `simularCanicas`:
   - Recorre cada canica  
   - En cada nivel decide izquierda (0) o derecha (1)  
   - Suma los resultados para obtener la posición final  
   - Guarda cada resultado en una lista  

3. Se crea la función `crearHistograma`:
   - Recibe la lista de resultados  
   - Genera un histograma usando `matplotlib`  
   - Usa `bins` para definir los contenedores  
   - Personaliza colores con `color` y `edgecolor`  
   - Se agregan títulos y nombres a los ejes  
   - Se muestra la gráfica  

---

## Resultado

El programa genera un histograma donde:
- El centro tiene más canicas  
- Los extremos tienen menos  
- Se forma una distribución tipo campana  

