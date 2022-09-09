from io import open

file = open('/home/jair8choa/wos/conjuntos/Estudiantes.prn')

def estudiantes():
  conj = set()

  for line in file:
    conj.add(tuple((int(line[0:8]),line[8:-1])))  
  return conj

if __name__ == "__main__":
  estudiantes()