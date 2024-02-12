print(' 2. Implementar una cola utilizando una lista en Python\n')

class FilaDeAtencion:
    def __init__(self):       
       self.cola = []  #Inicializa la fila como una cola vacía.

    def llegar_a_la_fila(self, cliente):        
        print(f" {cliente} ha llegado y se ha unido a la fila.")
        self.cola.append(cliente) #Un cliente llega y se añade a la cola.

    def atender_cliente(self): 
        if not self.esta_vacia():
            cliente_atendido = self.cola.pop(0) 
            print(f" ¡{cliente_atendido} ha sido atendido!") #Atiende al cliente en el frente de la cola. 
        else:
            print("La fila está vacía. No hay clientes para atender.") #Si la fila esta vacia muestra esto.

    def mostrar_fila(self):      
        if not self.esta_vacia():
            print("\n Estado de la fila actual: ", self.cola,"\n")  #Muestra la fila actual.
        else:
            print("\n Estado de la fila actual: Esta vacia. \n") #Si no hay nadie muestra este mensaje.

    def esta_vacia(self):       
        return len(self.cola) == 0 #Verifica si la fila está vacía.
 
#Programa que simule el proceso de atención en una fila:
fila_de_atencion = FilaDeAtencion()

fila_de_atencion.llegar_a_la_fila("Cliente 1") 
fila_de_atencion.llegar_a_la_fila("Cliente 2")
fila_de_atencion.llegar_a_la_fila("Cliente 3") 

fila_de_atencion.mostrar_fila() #Muestra los clientes que estan en fila.

fila_de_atencion.atender_cliente() 
fila_de_atencion.atender_cliente()
fila_de_atencion.atender_cliente() #Muestra el mensaje cuando atienden a los cliente.

fila_de_atencion.mostrar_fila() #Muestra los clientes que estan en fila pero como no hay tira el otro mensaje.



