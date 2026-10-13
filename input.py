def leer(nom_fich, matriz):

    f = open(nom_fich, "r")

    line = '1'
    while line != '':
        line = f.readline()
        list_buffer = []

        for car in line:
            if car != ' ' and car != '\n':
                list_buffer.append(int(car))

        if len(list_buffer) > 0:
            matriz.append(list_buffer)


    f.close()

def pprint(matriz):

    for list in matriz:
        print(list)
