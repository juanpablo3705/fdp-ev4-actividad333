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

validar_lista_numeros
lista = lista_int_ingreso

pares = []
impares = []

for cada_int in lista_int_ingreso:
        

