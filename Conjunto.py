##CONJUNTOS
#Obtener los set de ususario , llamaremos A y B
#Debemos hacer funcion de union, interseccion, diferencia y diferencia simetrica.

print("********** Bienvenidos a los conjuntos ********** ")
print("Introduce los elementos, separados por espacios   ")
print("Ej: 1 8 3 ")

conjunto_a = set(input("Conjunto A: ").split())
conjunto_b = set(input("Conjunto B: ").split())

#print(conjunto_a)
#print(conjunto_b)

def ver_instrucciones():
    print("\n ********** Menu ********** \n")
    print("Operaciones que puedes realizar")
    print("1. Union.")
    print("2. Interseccion.")
    print("3. Diferencia.")
    print('4. Diferencia Simetrica.')
    print("5. Ver instrucciones")
    print("6. Salir")

def union_conjuntos( conjunto_a, conjunto_b ):
    print( "\nLa union de A y B es {}\n".format(conjunto_a.union(conjunto_b)) )

def intersecion_conjuntos( conjunto_a, conjunto_b ):
    print( "\nLa interseccion de A y B es {}\n".format( conjunto_a.intersection( conjunto_b ) ) )

def diferencia_conjuntos( conjunto_a, conjunto_b ):
    print("¿Qué diferencia desea realizar?")
    print("1. A - B")
    print("2. B - A")

    try:
        opcion = int( input("Eliga opcion: "))
    except ValueError:
        print("Opción no valida, solo debes introducir 1 ó 2.")
        diferencia_conjuntos(conjunto_a, conjunto_b)
    else:
        if opcion == 1:
            print("\nLa intersección de A - B es {}\n".format(conjunto_a.difference(conjunto_b)))
        elif opcion == 2:
            print("\nLa interseccion de B - A es {}\n".format(conjunto_b.difference(conjunto_a)))
        else:
            print("\n *********** Opcion no valida! Intenta de nuevo ***********\n")
            diferencia_conjuntos( conjunto_a, conjunto_b )

def diferencia_simetrica_conjuntos( conjunto_a, conjunto_b ):
    print( "\nLa interseccion de A y B es {}\n".format( conjunto_a.symmetric_difference( conjunto_b ) ) )


while True:
    print("\n ********** Menu ********** \n")
    print("Operaciones que puedes realizar")
    print("1. Union.")
    print("2. Interseccion.")
    print("3. Diferencia.")
    print('4. Diferencia Simetrica.')
    print("5. Ver instrucciones")
    print("6. Salir")
    try:
        operacion = int(input("Eliga opcion: "))
    except ValueError:
        print("\n ********** Opcion no Validad, Solo numeros del 1 al 6 ********** \n")
    else:
        if operacion == 1:
            print("\n ********** Union ********** ")
            union_conjuntos( conjunto_a, conjunto_b )
        elif operacion == 2:
            print("\n ********** Interseccion ********** ")
            intersecion_conjuntos(conjunto_a, conjunto_b)
        elif operacion == 3:
            print("\n *********** Diferencia **********")
            diferencia_conjuntos( conjunto_a, conjunto_b )
        elif operacion == 4:
            print("\n ********** Diferencia Simetrica *********")
            diferencia_simetrica_conjuntos(conjunto_a, conjunto_b)
        elif operacion == 5:
            print("\n ********** Ver instrucciones *********** ")
            ver_instrucciones()
        elif operacion == 6:
            print("\n*********** Hasta Pronto ***********\n")
            break
        else:
            print("Opcion No valida intenta de Nuevo.")