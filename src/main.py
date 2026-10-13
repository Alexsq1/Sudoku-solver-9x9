import solver
import input

file = "input.txt"
matrix = []
input.readInput(file, matrix)

print("The input is: \n")
input.pprint(matrix)

print("\nSolving...\n")
solver.solver(matrix)

print("The solution is: \n")
input.pprint(matrix)
