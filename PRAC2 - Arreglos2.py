import time #Para poder medir el tiempo de ejecución 
import numpy as np #Libreria numpy para manejar mejor la creación de las matrices 

materias = 6  #Definir el tamaño de la matriz
alum = 500
matriz = np.random.randint(0, 101, size=(materias, alum)) #Se le anaden datos aleatorios entre 0 y 100

def buscar_alumno(matriz, materia, alum):
    return matriz[materia-1][alum-1], (materia-1, alum-1)
#Para buscar el valor de la materia y un alumno en particular, se pone -1 porque el indice comienza en cero

inicio = time.time() 
for _ in range(100000): #Indica que no se necesita el valor de la variable 
    calif, indices = buscar_alumno(matriz, 6, 322)
fin = time.time() 

print("-- Forma 2: --")
print(f"Alumno: 322")
print(f"Materia: 6")
print(f"Calificación: {calif}")
print(f"Posición en la matriz: {indices}")
print(f"Tiempo de ejecución de la búsqueda: {fin-inicio:.6f} seg")