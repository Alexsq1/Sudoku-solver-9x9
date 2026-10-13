# Returns the number of non-empty squares of the matrix
def nonZero(matrix):
    count = 0
    for row in matrix:
        for i in row:
            if i != 0:
                count += 1
    return count

def solver(matrix):
    b = solverR(matrix, nonZero(matrix), False)
    if b:
        return matrix
    else:
        raise Exception("Imposible to solve")

# Auxiliar method for recursive searching. Takes the input, the number of numbers inserted and if it is solver. Modificates the input.
def solverR(matrix, step, solved):

    # All the squares are filled: check if the solution is correct
    if step == 81:
        return check(matrix)

    # Select the square (i,j) with the minimum options avaliable (ltot)
    i, j, ltot = next2(matrix)

    for num in range(1, 10):

        if solved:
            break

        if ltot.count(num) == 0:

            matrix[i][j] = num
            solved = solved or solverR(matrix, step + 1, solved)

    # Wrong number: undo
    if not solved:
        matrix[i][j] = 0

    return solved

# Selects the square with the minimum options available in the format (i, j, options)
def next2(matrix):

    l_tot_final = []

    # Current minimum square and options
    mx, my = 0, 0
    valMin = 9

    for i in range(0, 9):
        for j in range(0, 9):

            if valMin == 0:
                break

            if matrix[i][j] == 0:
                l1 = makeRow(matrix, i)
                l2 = makeColumn(matrix, j)
                l3 = makeCuad(matrix, i, j)
                ltot = l1 + l2 + l3
                ltot = clean(ltot)

                remaining = 9 - len(ltot)
                if remaining < valMin:
                    mx = i
                    my = j
                    valMin = remaining
                    l_tot_final = ltot

    return mx, my, l_tot_final

# Takes a list, remove duplicates and sorts it
def clean(ltot):
    ltot = [*set(ltot)]
    ltot.sort()
    ltot.remove(0)
    return ltot

# Checks if a sudoku is properly solved
def check(matrix):

    b = True

    #Rows
    for l in matrix:
        if not allDifferent(l) or not b:
            b = False
            break

    #Columns
    l_buffer = []
    for i in range(0, 9):
        if not b:
            break

        l_buffer.clear()
        l_buffer = makeColumn(matrix, i)

        if not allDifferent(l_buffer) or not b:
            b = False
            break

    #Squares:

    options = ([0, 1, 2], [3, 4, 5], [6, 7, 8])

    for rows in range(0, len(options), 3):
        if not b:
            break
        for columns in range(0, len(options), 3):
            if not b:
                break

            l_buffer.clear()
            l_buffer = makeCuad(matrix, rows, columns)

            if not allDifferent(l_buffer) or not b:
                b = False
                break
    return b

# Checks if all the elements in the list are different
def allDifferent(list):

    b = True
    for i in range(1, len(list)):
        if list.count(i) != 1:
            b = False
            break
    return b

# Takes the row of a matrix
def makeRow(matrix, index):

    return matrix[index]

# Takes the column of a matrix
def makeColumn(matrix, index):

    l_buffer = []
    for rows in matrix:
        l_buffer.append(rows[index])

    return l_buffer

# Takes the column of a box
def makeCuad(matrix, row, column):

    l_buffer = []
    options = ([0, 1, 2], [3, 4, 5], [6, 7, 8])

    opx, opy = 0, 0

    while row not in options[opx]:
        opx += 1
    while column not in options[opy]:
        opy += 1

    for i in options[opx]:

        for j in options[opy]:

            l_buffer.append(matrix[i][j])

    return l_buffer
