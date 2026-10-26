def readInput(nom_fich, matrix):
    """
    Reads a file in a sudoku format
    """


    f = open(nom_fich, "r")

    line = '1'
    while line != '':
        line = f.readline()
        list_buffer = []

        for car in line:
            if car != ' ' and car != '\n':
                list_buffer.append(int(car))

        if len(list_buffer) > 0:
            matrix.append(list_buffer)


    f.close()

def pprint(matrix):
    """
    Prints a sudoku
    """
    for list in matrix:
        print(list)
