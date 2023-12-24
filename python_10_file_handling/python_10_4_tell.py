# Open a file for reading
with open('example.txt', 'r') as file:
    content = file.read(15)  # Read the first 15 characters
    position = file.tell()   # Get the current position
    print(f"Content: {content}")
    print(f"Current position: {position}")
