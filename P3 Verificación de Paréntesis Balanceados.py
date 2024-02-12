print(' 3. Verificación de Paréntesis Balanceados\n')

def parentesis_balanceados(cadena):    
    pila = [] #Inicializamos una pila vacía para rastrear los paréntesis abiertos.
    
    for caracter in cadena:       
        if caracter == '(': #Si encontramos un paréntesis de apertura, lo agregamos a la pila.
            pila.append(caracter)        
        elif caracter == ')': #Si encontramos un paréntesis de cierre.
            if not pila or pila.pop() != '(': #Si alguna de las condiciones anteriores se cumple, la cadena no está balanceada.                
                return False  
    return not pila #Si la pila está vacía al final, entonces los paréntesis están balanceados.

#Ejemplo de funcion:
cadena = "(3,4,55,4,3,3)"
resultado = parentesis_balanceados(cadena)
print(' La cadena',cadena,'es:',resultado,'.') #Imprimimos el resultado




