# funcion para validar ingresos y crear lista de int:
def validar_lista_numeros():

    while True:
        entrada = input("Ingrese una lista de números separados por espacios: ")
        elementos = entrada.split()
        numeros = []
        try:
            for elemento in elementos:
                numeros.append(int(elemento))
            return numeros
        except ValueError:
            print("Error. Debe ingresar solamente números enteros.")

# funcion para calcular pares e impares:
def separar_pares_impares(lista_numeros):
 
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares


# programa principal:

lista = validar_lista_numeros()

pares, impares = separar_pares_impares(lista)

print("Números pares:", pares)
print("Números impares:", impares)