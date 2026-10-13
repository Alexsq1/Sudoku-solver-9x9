import solver
import input

#programa solucionador de sudoku por backtracking

#usar búsqueda en profundidad de árbol, empezando por menos opciones

#método comprobar, siguiente opción, menor núm opciones

#se codifica con una matriz, número no puesto -> 0

fichero = "enunciado.txt"
matriz = []
input.leer(fichero, matriz)


print("\nResolviendo...\n")
solver.solver(matriz)


print("La matriz final es: \n")
input.pprint(matriz)
print("¿Está resuelto? ", solver.check(matriz))

#print(input.pprint(matriz))
