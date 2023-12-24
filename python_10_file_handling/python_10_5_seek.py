# Open a file for reading
with open('example.txt', 'r') as file:
    content = file.read(15)  # Read the first 15 characters
    position_before = file.tell()  # Get the current position before seeking
    print(f"Content before seek: {content}")
    print(f"Position before seek: {position_before}")

    # Seek to the beginning of the file
    file.seek(0, 0)

    # Read again from the beginning
    content_after_seek = file.read(10)
    position_after_seek = file.tell()
    print(f"Content after seek: {content_after_seek}")
    print(f"Position after seek: {position_after_seek}")
