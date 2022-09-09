'''
# Tema: Tuplas
# Fecha: 31 de agosto del 2022
# Autor: Leonardo Martínez González
'''
# 1. Definición. Es una colección de elementos inmutables.
#             Las tuplas son immutables y normalmente contienen una secuencia heterogénea
#             de elementos que son accedidos al desempaquetar o indizar.

# 2. Crear tuplas
tupla1 = tuple()
tupla2 = ()
tupla3 = (2, 'Pancho', True, 43.5)

# 3. Accesar a elementos de la tupla, igual que en las listas
print(tupla3[1])
for elem in tupla3:
    print(elem)

# 4. Operaciones.
# 4.A. Son inmutables
# tupla3[1] = 'uvu'

# 4.B. Las tuplas pueden ser anidadas
grupo_a = ('Jose', 'Mariana', 'Juan')
grupo_b = ('Antonio', 'Pedro', 'Manuel')
grupo_c = (grupo_a, grupo_b)
print(grupo_c)
numeros = ((3,5), (4,2), (7,6))
print(numeros)

# 4.C. Las listas se pueden convertir en tuplas  haciendo uso de la función tuple()
lista = ['A', 'B', 'C', 'D']
tupla_letras = tuple(lista)
print(tupla_letras)

# 4.D. Se puede asignar el valor de una tupla con n elementos a n variables
alumno = (420100, 'Isaias Sanchez Herrera')
contro,nombre = alumno
print('Control: ', contro, 'Nombre: ',nombre)

# 5. Métodos de tuplas
# count(), regresa el numero de elementos
print(grupo_a.count('Jose'))

# index() Regresa el índice donde se ha encontrado, tambien puede pasarle un segundo


'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
con la siguiente forma:
(nombre, clave, destino)
Ejemplo:
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el estado al que pertencen.
Ejemplo:
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de pasajeros
- Agregar ciudades a la lista de ciudades
- Dada la CLAVE de un pasajero, ver a que ciudad viaja
- Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
- Dada la CLAVE de un pasajero, ver a que ESTADO viaja
- Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
- Salir del programa

NOTA: Haga uso de funciones
'''
