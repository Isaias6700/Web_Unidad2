import estudiantes
import materias
import json

def consultar(numero_control):
  conjunto_alumnos = estudiantes.estudiantes()
  conjunto_materias = materias.materias()
  dic = {}
  arr_materia = []
  dic_materia = {}
  promedio = 0

  for alumno in conjunto_alumnos:
    if numero_control in alumno:
      nombre = alumno[1]
      dic['Nombre'] = nombre
      for materia in conjunto_materias:
        if numero_control in materia:
          dic_materia["Nombre"] = materia[1]
          dic_materia["Promedio"] =int(materia[2])
          promedio += int(materia[2])
          arr_materia.append(dic_materia)
          dic_materia = {}
      dic["Materias"] = arr_materia
      dic["Promedio"] = promedio/len(arr_materia)
  return dic

if __name__ == '__main__':
  numero_control = input('N. Control: ')
  res = consultar(int(numero_control))
  json_file = open("/home/jair8choa/wos/archivos/res.json", 'w')
  json.dump(res, json_file)
  pass