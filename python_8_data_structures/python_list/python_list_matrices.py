matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
#using loop
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# Accessing an element in the matrix
element = matrix[1][2]
print(element)  # Output: 6
