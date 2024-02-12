print(' 1. Implementación de una Pila\n')

# Implementación de una Pila
class Pila:
    def __init__(self):
        self.items = []  #Aqui creamos una lista para almacenar los elementos una pila.

    def esta_vacia(self):
        return len(self.items) == 0  #Devuelve True si la pila está vacía, False en caso contrario.

    def push(self, elemento):
        self.items.append(elemento)  #Agrega un elemento a la parte superior de la pila.

    def pop(self):
        if not self.esta_vacia():  #Verifica si la pila no está vacía.
            return self.items.pop()  #Elimina y regresa el elemento en la parte superior de la pila.

#Implementación de una Cola
class Cola:
    def __init__(self):
        self.items = []  #Creamos una lista para guardar los elementos de la cola.
    def esta_vacia(self):
        return len(self.items) == 0  #Regresa True si la cola está vacía, False en caso contrario.
    def enqueue(self, elemento):
        self.items.insert(0, elemento)  #Agrega un elemento al principio de la cola.
    def dequeue(self):
        if not self.esta_vacia():  #Verifica si la cola no está vacía.
            return self.items.pop()  #Elimina y devuelve el elemento al final de la cola.

# Función para invertir una lista utilizando una Pila
def invertir_lista_con_pila(lista):
    pila = Pila()  #Se crea una instancia de la clase pila.
    for elemento in lista:
        pila.push(elemento)     #Se aregrega cada elemento de la lista a la pila.
    lista_invertida = []
    while not pila.esta_vacia():    #Mientras la pila no esté vacía.
        lista_invertida.append(pila.pop())  #Se saca los elementos de la pila y los añadimos a la lista invertida
    return lista_invertida

#Aqui el programa para invertir una lista.
if __name__ == "__main__":
    lista_original = [10, 20, 30, 40, 50]
    print(" Lista original:", lista_original)
    lista_invertida = invertir_lista_con_pila(lista_original)
    print(" Lista invertida:", lista_invertida)
