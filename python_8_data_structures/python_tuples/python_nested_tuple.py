nested_tuple = (
    (1, 2, 3),
    (4, 5, 6)
)
print(nested_tuple)
#using loop
for row in nested_tuple:
    for item in row:
        print(item, end=" ")
    print()

# Accessing an element in the nested tuple
element = nested_tuple[1][2]  # Accessing the element in the second row, third column
print(element)  # Output: 6
