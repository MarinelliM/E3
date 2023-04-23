def menu(lista):
    print('1 - Mostrar el maximo y menor valor')
    print('2 - Temperatura promedio mensual por hora')
    print('3 - Obtener los valores de las tres variables para cada hora del día dado')
    print('0 - Salir')
    op = int(input('Ingrese opcion:'))
    while op!=0:
        if op == 1:
            op1(lista)
        elif op ==2:
            op2(lista)
        elif op == 3:
            a = int(input('Ingrese el dia a buscar:'))
            op3(lista,a)
        else:
            print('opcion incorrecta')
            op = int(input('Ingrese opcion:'))
        print('1 - Mostrar el maximo y menor valor')
        print('2 - Temperatura promedio mensual por hora')
        print('3 - Obtener los valores de las tres variables para cada hora del día dado')
        print('0 - Salir')
        op = int(input('Ingrese opcion:'))
    print('Fin del programa')

def op1(lis):
    opciones=['Temperatura','Humedad','Presion']
    for i in range(3):
        max=func1(lis,opciones[i])
        min=func2(lis,opciones[i])
        print('Para el dia {} el mayor registro de la variable {} es de {}, y para el dia {} el menor valor es de {}' .format(max[0]+1,opciones[i],max[1],min[0]+1,min[1]))

def func1(lisa,op):
    ma=-100000
    if op == 'Temperatura':
        for i in range(30):
            for j in range(24):
                if lisa[i][j].getemp() > ma:
                    ma = lisa[i][j].getemp()
                    dia = i
                    hora = j
    elif op == 'Humedad':
        for i in range(30):
            for j in range(24):
                if lisa[i][j].gethum() > ma:
                    ma = lisa[i][j].gethum()
                    dia = i
                    hora = j
    elif op == 'Presion':
        for i in range(30):
            for j in range(24):
                if lisa[i][j].getpres() > ma:
                    ma = lisa[i][j].getpres()
                    dia = i
                    hora = j
    return dia,hora
def func2(lisa,op):
    mi=10000000000
    if op == 'Temperatura':
        for i in range(30):
            for j in range(24):
                if lisa[i][j].getemp() < mi:
                    mi = lisa[i][j].getemp()
                    dia = i
                    hora = j
    elif op == 'Humedad':
        for i in range(30):
            for j in range(24):
                if lisa[i][j].gethum() < mi:
                    mi = lisa[i][j].gethum()
                    dia = i
                    hora = j
    elif op == 'Presion':
        for i in range(30):
            for j in range(24):
                if lisa[i][j].getpres() < mi:
                    mi = lisa[i][j].getpres()
                    dia = i
                    hora = j
    return dia,hora

def op2(lisa):
    for i in range(24):
        m = 0
        for j in range(30):
            m += lisa[j][i].getemp()
        m = m/30
        print('El valor promedio mensual de la temperatura en la hora {} es de {:.2f}'.format(i+1,m))

def op3(lisa,b):
    for i in range(24):
        print('En la hora {} del dia {} el valor de la temperatura es de {} el de la humedad es de {} y de la presion de {}'.format(i+1,b,lisa[b-1][i].getemp(),lisa[b-1][i].gethum(),lisa[b-1][i].getpres()))

