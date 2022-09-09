#Listas
#26/08/22
#Isaias Sanchez Herrera

#Listas
# nombre_lista =  []
# otra_lista = list()


#1. Imprimir una lista
# lista1 = [3,6,3,2,4,5]
# for i in lista1:
#     print(i)


#2. Imprimir lista de nombres
# lista1 = ['xd','unu','usu']
# for i in lista1:
#     print(i)

#3.
 #lista1 = [223,'were',43,'rewf']
# for i in lista1:
#     print(i)

#4.
# print(lista1[0])
# print(lista1[2])
# print(lista1[-1])
# print(lista1[-5])

#Agregar elementos a una lista
# lista = []
# for i in lista:
#  print(i)
# lista.append(100)
# lista.append(500)
# for i in lista:
#  print(i)

lista = []
cont =1
while cont < 11:
 lista.append(input("Numero "))
 cont = cont +1

lista.sort()
print(lista)