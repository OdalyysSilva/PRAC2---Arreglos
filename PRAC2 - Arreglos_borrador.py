"""Alumno por materia"""
import time
import numpy as np

materias = 6 #Definir el tamaño de la matriz
alum = 500
matriz = np.random.randint(0, 101, size=(materias, alum)) #Se le anaden datos aleatorios entre 0 y 100

def buscar_alumno(matriz, materia, alum):
    return matriz[materia-1][alum-1], (materia-1, alum-1)
#Para buscar el valor de la materia y un alumno en particular, se pone -1 porque el indice comienza en cero

inicio = time.perf_counter()
resul, indices = buscar_alumno(matriz, 5, 321)
fin = time.perf_counter()

print("-- Forma 1: --")
print(f"Alumno buscado: {resul}, posición: {indices}")
print(f"Tiempo de ejecución de la búsqueda: {fin - inicio} seg")
