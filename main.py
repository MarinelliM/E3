from Temperatura import Registro
import csv
from Menu import menu

def test():
    m = Registro(8, 7.1, 9.9)
    m.getvalores()

def mostrarmatriz(lis):
    for i in range(3):
        for j in range(2):
            print(lis[i][j])

if __name__ == '__main__':
    test()
    lista = []
    for i in range(30):
        lista.append([])
        for j in range(24):
            lista[i].append(None)
    
    with open('ej3.csv', 'r', encoding='utf8') as archivo:
        reader = csv.reader(archivo, delimiter=',')
        next(reader)
        for fila in reader:
            dia=int(fila[0])-1
            hora=int(fila[1])-1
            temperatura=float(fila[2])
            humedad=float(fila[3])
            presion=float(fila[4])
            registro=Registro(temperatura,humedad,presion)
            lista[dia][hora] = registro
            print(lista)
    menu(lista)
