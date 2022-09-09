import json
import random

import bcrypt
def devuelve_estudiantes():
    estudiantes = open("Estudiantes.prn","r")
    conjunto_estudiantes= set()
    estudiantes = estudiantes.readlines()
    for est in estudiantes[0:]:
        estudiante = est.split("\n")
        no_control = estudiante[0][0:8]
        nombre = estudiante[0][8:]
        tupla = (no_control, nombre)
        conjunto_estudiantes.add(tupla)
    return conjunto_estudiantes

materias = open("Kardex.txt","r")
conjunto_materias= set()
materias = materias.readlines()
for mat in materias[0:]:
    materia = mat.split("\n")
    datos = materia[0].split('|')
    no_control2 = datos[0]
    nombre_materia = datos[1]
    calificacion = int(datos[2])
    conjunto_materias.add((no_control2,nombre_materia,calificacion))
# print(conjunto_materias)

# formato = {}
# def consulta(nc):
#     promedio = 0
#     dicc_mat = {}
#     lis_mat = []
#
# #     for alumn in conjunto_estudiantes:
# #         if nc in alumn:
# #             nombre = alumn[1]
# #             formato['Nombre'] = nombre
# #             for mat in conjunto_materias:
# #                if nc in mat:
# #                    dicc_mat['Nombre'] = mat[1]
# #                    dicc_mat['Promedio'] = int(mat[2])
# #                    promedio += int(mat[2])
# #                    lis_mat.append(dicc_mat)
# #                    dicc_mat = {}
# #             formato['Materias'] = lis_mat
# #             formato['Promedio'] = promedio/len(lis_mat)
# #     return formato
# #
# # print('Bienvenido')
# # print('Ingresa el numero de control')
# # num_control = input()
# # print(consulta(num_control))
# #
# # with open("formato.json", "w") as file:
# #     json.dump(formato, file, indent=4)

# 4.- List de materias
# def regresa_materia_por_estudiantes(ctl):
#     promedios = regresa_materia_por_estudiantes()
#     lista_materias = []
#     for mate in promedios:
#         c,m,p = mat
#         if ctl == c:
#             lista_materias.append({'Nombre': m})
#     return json.dums(lista_materias)
#
# print(regresa_materia_por_estudiantes('18420485'))

# 5
def mayuscula(): #Genera una letra mayuscula desde la A ... Z
    return chr(random.randint(65,90))


def minuscula():
    return chr(random.randint(97,122))

def generar_numeros():
    return chr(random.randint(48,57))

def caracter_especial():
    lista_caracter = ['@', '#', '$','%','&','_','?','!']
    return lista_caracter[random.randint(0,7)]

def generar_contra():
    clave = ""
    for i in range(1,10):
        numero = random.randint(1,5)
        if numero == 1:
            clave = clave + mayuscula()
        elif numero == 2:
            clave = clave + minuscula()
        elif numero == 3:
            clave = clave + caracter_especial()
        elif numero >= 4 and numero <= 5:
            clave = clave + generar_numeros()
    return clave

# print(generar_contra())

# Cifrar contraseña
def cifrar_contra(contrasena):
    sal = bcrypt.gensalt()
    contra_cifra = bcrypt.hashpw(contrasena.encode('utf-8'), sal)
    return contra_cifra

clave = generar_contra()
# print(clave,cifrar_contra(clave))
#
# print(bcrypt.checkpw("Zvm9#GYtS".encode('utf-8'),"$2b$12$s5vnd2GLyKTi/hUAoVQxb.YmTfxswee0mPtnj90BTz.5pScghhQdu".encode('utf-8')))

# Generar archivo de usuarios
# def generar_archivo_usuario():
#     estudiante = conjunto_estudiantes
#     usuarios = open('usuarios.txt','w')
#     cont = 1
#     for estu in estudiante:
#         c,n = estu
#         clave = generar_contra()
#         clave_cifrada = cifrar_contra(clave)
#         registro = c + " " + clave + " " + str(clave_cifrada, 'utf-8') + " \n"
#         usuarios.write(registro)
#         cont += 1
#         print(cont)
#     print("Archivo Generado")

# generar_archivo_usuario()

def autenticar_usuario (usuario, contrasena):

    archivo_usuario = open("usuarios.txt", "r")
    archivo_estudiantes = devuelve_estudiantes()
    lista_usuario = archivo_usuario.readlines()

    flag = False
    user = usuario
    password = contrasena
    msj = ""
    lista_login = {}
    log = {}

#evaluar si existe el usuario

    for est in lista_usuario[0:]:
        usuarios = est.split()
        c, p, e = usuarios
        if c == user:
            for ae in archivo_estudiantes:
                co,n = ae
                if p == password:
                 flag = True
                 msj = "Bienvenido al Sistema de Autenticación de usuarios"
                 log["Bandera: "] = flag
                 log["Usuario: "] = n
                 log["Mensaje: "] = msj
                 print(log)
                 break
                elif p != password:
                    flag = False
                    msj ="Contraseña incorrecta"
                    log["Bandera: "] = flag
                    log["Usuario: "] = n
                    log["Mensaje: "] = msj
                    print(log)
                    break
        else:
            flag = False
            msj = "No existe el Usuario"
            log["Bandera: "] = flag
            log["Usuario: "] = ""
            log["Mensaje: "] = msj
            print(log)
            break

    return json.dumps(log)


autenticar_usuario("18420470","48$8@2#Yg")
# print(devuelve_estudiantes())