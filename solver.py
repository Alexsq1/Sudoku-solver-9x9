def nonZero(matriz):

    count = 0
    for row in matriz:
        for i in row:
            if i != 0:
                count += 1
    return count

def solver(matriz):
    b = solverR(matriz, nonZero(matriz), False)
    if b:
        return matriz
    else:
        raise Exception("Imposible resolver")

def solverR(matriz, etapa, solved):


    if etapa == 81:
        return check(matriz)

    '''
    l1 = makeRow(matriz, i)
    l2 = makeColumn(matriz, j)
    l3 = makeCuad(matriz, i, j)
    ltot = l1 + l2 + l3
    ltot.sort()
    ltot = [*set(ltot)]
    ltot.remove(0)
    '''


    i, j, ltot = next2(matriz)

    for num in range(1, 10):

        if solved:
            break

        if ltot.count(num) == 0:

            matriz[i][j] = num
            solved = solved or solverR(matriz, etapa + 1, solved)

    if not solved:
        matriz[i][j] = 0

    return solved



def next(matriz):

    i, j = 0, 0
    while matriz[i][j] != 0:
        j += 1
        if j == 9:
            j = 0
            i += 1
    return i, j


def next2(matriz):

    valMin = 9
    l_tot_final = []
    mx, my = 0, 0
    for i in range(0, 9):
        for j in range(0, 9):

            if valMin == 0:
                break

            if matriz[i][j] == 0:
                l1 = makeRow(matriz, i)
                l2 = makeColumn(matriz, j)
                l3 = makeCuad(matriz, i, j)
                ltot = l1 + l2 + l3
                ltot = clean(ltot)

                remaining = 9 - len(ltot)
                if remaining < valMin:
                    mx = i
                    my = j
                    valMin = remaining
                    l_tot_final = ltot

    return mx, my, l_tot_final


def clean(ltot):
    ltot.sort()
    ltot = [*set(ltot)]
    ltot.remove(0)
    return ltot

def check(matriz):

    b = True

    #Filas
    for l in matriz:
        if not allDifferent(l) or not b:
            b = False
            break

    #Columnas
    l_buffer = []
    for i in range(0, 9):
        if not b:
            break

        l_buffer.clear()
        l_buffer = makeColumn(matriz, i)

        if not allDifferent(l_buffer) or not b:
            b = False
            break


    # Cuadrículas:

    opciones = ([0, 1, 2], [3, 4, 5], [6, 7, 8])

    for rows in range(0, len(opciones), 3):
        if not b:
            break
        for columns in range(0, len(opciones), 3):
            if not b:
                break

            l_buffer.clear()
            l_buffer = makeCuad(matriz, rows, columns)

            if not allDifferent(l_buffer) or not b:
                b = False
                break


    return b


def allDifferent(list):

    b = True
    for i in range(1, len(list)):
        if list.count(i) != 1:
            b = False
            break

    return b

#Te dan la matriz, devolver una lista con los elementos
#de la fila/columna/cuadrícula
def makeRow(matriz, index):

    return matriz[index]

def makeColumn(matriz, index):

    l_buffer = []
    for rows in matriz:
        l_buffer.append(rows[index])

    return l_buffer

def makeCuad(matriz, row, column):


    l_buffer = []
    opciones = ([0, 1, 2], [3, 4, 5], [6, 7, 8])

    opx, opy = 0, 0

    while row not in opciones[opx]:
        opx += 1
    while column not in opciones[opy]:
        opy += 1

    for i in opciones[opx]:

        for j in opciones[opy]:

            l_buffer.append(matriz[i][j])

    return l_buffer