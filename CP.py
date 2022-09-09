'''
Tema: Diccionarios, archivos y formato JSON
Fecha: 02 de septiembre del 2022
Autor: Isaac Rocha Torres
'''

'''
Ejercicio: Crear un diccionario con los códigos postales y su localidad del estado de San Luis Potosi,
           para ello descargue la tabla de códigos postales de la siguiente dirección: 
           https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx

           el formato del diccionario  tendra la forma:
           {109159: {'CP': '78000', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, 
           109160: {'CP': '78037', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, . . . }

           Genere una lista con los VALORES del diccionario anterior.
           Guarde en un archivo con formato JSON los resultados

           Consideraciones:
           1. El método split regresa un arreglo al separar una cadena en subcadenas.
           2. El municipio se encuentra en la posición 4.
           3. El estado se llama: "San Luis Potosí"
'''
import json

arch = open("CPdescarga.txt")
renglones = arch.readlines()
lista = {}

for ren in renglones[2:]:
    codigos = {}
    cod = ren.split(sep='|')
    if cod[4] == 'San Luis Potosí':
        codigos["Codigo Postal"] = cod[6]
        codigos["Municipio"] = cod[3]
        codigos["Estado"] = cod[4]
        lista[cod[0]] = codigos
print(lista)

with open("listap.json", "w") as file:
    json.dump(lista, file, indent=4)
