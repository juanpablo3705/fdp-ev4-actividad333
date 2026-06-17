def validar_lista_numeros():

    while True:
        try:
            ingreso = input("Ingrese números separados por un espacio: ")
            lista_str_ingreso = ingreso.split()
            lista_int_ingreso = []
            for cada_ingreso in lista_str_ingreso:
                lista_int_ingreso.append(int(cada_ingreso))
            return lista_int_ingreso
        except ValueError:
            print("Error, sólo puede ingresar números separados por un espacio.")

lista = validar_lista_numeros() # capturar el valor de la variable lista_int_ingreso en la variable lista

pares = []
impares = []

for cada_int in lista:
    if (cada_int % 2 == 0):
        pares.append(cada_int)
    else:
        impares.append(cada_int)
# no debo llamar a la funcion validar_lista_numeros() de nuevo, porque las variables ya existen
print(f"Números pares: {pares}.")
print(f"Números impares: {impares}.")