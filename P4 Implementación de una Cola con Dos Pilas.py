print(' 4. Implementación de una Cola con Dos Pilas.\n')

class ColaConPilas:
    def __init__(self):
        self.pila_entrada = []  #Pila para la entrada de elementos.
        self.pila_salida = []   #Pila para la salida de elementos.

    def enqueue(self, elemento):
        self.pila_entrada.append(elemento)  #Agrega un elemento a la cola (simula "enqueue" en una cola).

    def dequeue(self): #Remueve y devuelve el elemento más antiguo de la cola (simula "dequeue" en una cola).
                
        if not self.pila_salida: #Si la pila de salida está vacía, transfiere los elementos desde la pila de entrada.
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        
        if not self.pila_salida: #Si ambas pilas están vacías la cola está vacía.
            return None
       
        return self.pila_salida.pop() #Devuelve el elemento más antiguo de la cola.

    def esta_vacia(self):
        return not (self.pila_entrada or self.pila_salida)  #Verifica si la cola está vacía.
    
#Ejemplo de funcion:
cola = ColaConPilas()

cola.enqueue(1) #Asignaciones de cola.
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)

print(cola.dequeue())  #Salida 1.
print(cola.dequeue())  #Salida 2.
print(cola.dequeue())  #Salida 3.
print(cola.dequeue())  #Salida 4.

print(cola.dequeue())  #Salida None si la cola está vacía.

