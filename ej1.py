# funcion para validar ingresos y crear lista de int. arroja la variable "numeros":
def validar_lista_numeros():

    while True:
        entrada = input("Ingrese una lista de números separados por espacios: ")
        elementos = entrada.split() # divide el ingreso de un str en elementos separados de una lista
        numeros = [] # creo la lista donde voy a depositar dichos elementos
        try:
            for elemento in elementos: # uso ciclo for para transformar cada elemento de la lista que viene en str a int
                numeros.append(int(elemento)) # en el append especifico que quiero añadir como int
            return numeros # termina la funcion y entrega la lista completa en int hacia la variable (lista) "numeros"
        except ValueError:
            print("Error. Debe ingresar solamente números enteros.")

# funcion para calcular pares e impares. arroja las variables "pares", "impares":
def separar_pares_impares(lista_numeros):
 
    pares = []
    impares = []
    for numero in lista_numeros: # añadir cada elemento de la lista uno por uno a su categoria
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares # termina la funcion y entrega dos listas: pares e impares


# programa principal:

lista = validar_lista_numeros() # llamo a la funcion para llenar la variable "lista"

pares, impares = separar_pares_impares(lista) # llamo a la funcion para llenar las variables "pares" e "impares"

print("Números pares:", pares)
print("Números impares:", impares)