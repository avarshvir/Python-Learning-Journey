# Open a file for writing
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
    file.flush()  # Flush the internal buffer to ensure data is written immediately
