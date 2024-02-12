print(' 5. Revertir la Mitad de una Cola.\n')

from collections import deque

def Revertir_mitad(queue):    
    if not queue: #Verificar si la cola está vacía.
        return
   
    stack = [] #Crear una pila para almacenar temporalmente.  
    longitud = len(queue) #Obtiene la longitud de la cola.
    mitad = longitud // 2 #Calcula la mitad de la longitud de la cola.
   
    for _ in range(mitad):
        stack.append(queue.popleft()) #Pasa la primera mitad de la cola a la pila.   
    while stack:
        queue.append(stack.pop()) #Pasa la pila de nuevo a la cola para invertir la mitad de los elementos.  
    for _ in range(mitad):
        queue.append(queue.popleft()) #Pasa la segunda mitad de la cola a la pila esto sin invertir.

#Ejemplo de funcion:
cola = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(" Cola original: ", cola) #Muestra la cola original.

Revertir_mitad(cola) #Revierte la cola ingresada.
print("\n Cola invertirtiendo la mitad:", cola) #Muestra el resultado de la mitadad de la cola invertida.

