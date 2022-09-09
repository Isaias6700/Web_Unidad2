from io import open

file = open('/home/jair8choa/wos/conjuntos/Kardex.txt', errors="ignore")


def materias():
  conj = set()

  for line in file:
    arr = line.split('|')
    tupla = (int(arr[0]), arr[1], arr[2][:-1])
    conj.add(tupla)
  return conj

if __name__ == "__main__":
  materias()