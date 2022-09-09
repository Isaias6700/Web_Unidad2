'''
Tema: conjuntos
Fecha: 05 de septiembre del 2022
Autor: Leonardo Martínez González
'''

# 1. Definición. en Python es utilizado para trabajar con conjuntos de elementos.
#    La principal característica de este tipo de datos es que es una colección cuyos elementos
#    no guardan ningún orden y que además son únicos.
#    los principales usos de esta clase se usan para conocer si un elemento pertenece o no
#    a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).

# 2. Creación. Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {},
#    o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable
#    (como una lista, una tupla, una cadena …).
# lista = {}
# c1 = {1,2,3,4}
# c2 = set(i for i in range (0,11,2))
# c3 =set()



#    Usando la función forezenset. es inmutable y su contenido no puede ser modificado
#    una vez que ha sido inicializado


#    Los elementos repetidos se eliminan


# 3. Para acceder a los elementos de un conjunto. Dado que los conjuntos son colecciones
#    desordenadas, en ellos no se guarda la posición en la que son insertados los elementos
#    como ocurre en los tipos list o tuple. Es por ello que no se puede acceder a los elementos
#    a través de un índice.



# 4. Añadir elementos: con el método add() ó con el método update()
#    Agregar el numero 8 al conjunto c


#    Agregar varios elementos al conjunto


# 5. Eliminar elementos del conjunto: discard(elemento), remove(elemento), pop() y clear()
#    discard(elemento) y remove(elemento) son muy parecidos, solo que remove lanza una excepcion KeyError
#    en caso de no existir el elemento



#     pop() devuelve un elemento aleatorio y lo elimina, si el conjunto esta vacio lanza una
#     excepcion KeyError.



#    El método clear() elimina todos los elementos del conjunto


#    Número de elementos en un conlunto con la función len()


#    Verificar si un elemento esta dentro de un conjunto



# ************************ Operaciones con conjuntos
# 1. Union  ( | )


# 2. Intersección ( & )


# 3. Diferencia ( - )


# 4. Diferencia simétrica ( ^ ). es el conjunto que contiene los elementos de A y B
#    que no son comunes.


# 5. Inclusión de conjuntos.  Se utiliza el operador <= para comprobar si un conjunto A
#    es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.


# 5. Conjuntos disjuntos. Dos conjuntos A y B son disjuntos si no tienen elementos en común,
#    es decir, la intersección de A y B es el conjunto vacío.


# 6. Igualdad de conjuntos. En Python dos conjuntos son iguales si y solo si todos los elementos
#    de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto
#    del otro.


'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"",
                "Promedio":
            },
            {
                "Nombre":"",
                "Promedio":
            },
            . . . 
        ],
        "Promedio general": 
   }


'''






