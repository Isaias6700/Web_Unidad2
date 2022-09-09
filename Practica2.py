# Listas
# 29/08/22
# Isaias Sanchez Herrera

#lista = ['Pancho', 'Pedro', 'Juan', 'Marisela', 'Pancha']

# for x in range(5):
#     print(lista[x])
#
# print("Longitud de la lista: " + str(len(lista)) + "\n")

# print(lista[0:2])             #Rebanadas de una lista
# print(lista[:2])
# print(lista[2:4])

# lista.insert(1,'Lalo')        #Inserta un elemento mediante el indice
# print(lista)
# lista.remove('Lalo')          #Remueve un elemento
# print(lista)

# print(lista)
# lista.pop()
# print(lista)

# lista = ['Pancho', 'Pedro', 'Juan', 'Marisela', 'Pancha']
# print(lista.index('Pedro'))         #Regresa el indice de un elemento
#
# lista.insert(4,'Pancha')
# print(lista)
# print(lista.count('Pancha'))      #Cuenta el numero de elementos iguales
#
# print(lista.reverse())              #Invierte los elementos de la lista
# print(lista)

# lista = [i for i in range(5)]
# # print(lista)

# import random
# lista = [random.randint(1,100) for i in range(10)]
# print(lista)


#Lista anidada
# prom = []
#lista = [18420485, 'Isaias Sanchez Herrera', 83], [18420458698, 'Pedro Felipe Diaz', 87], [18420125987, 'Mariano Lopez', 95]
# for x in lista:
#     prom.append(list[-1])
#
# print(prom)

lista = ['Isaias Sanchez', 'Isaac Rocha', 'Joauqin Ochoa', 'Juan Navarrete']
# def buscar(nom):
#     for x in lista:
#         if (nom == )


#Lista de estudiantes
#Menu principal: Insertar, Eliminar, actualizar, imprimir y Salir
print('Menu')
print('1: Insertar\n','2: Eliminar\n', '2: Actualizar\n', '3: Imprimir\n', '4: Salir')
op = input('Selecciona una opcion: ')

while op > 0 and op < 5:
    if op == 1:
        name = input('Dame un nombre ')
        name.upper(lista)
    elif op == 2:
        name = input('Nombre del alumno a eliminar')
        for x in lista:
            if (name == lista[x]):
                lista.remove(name)
