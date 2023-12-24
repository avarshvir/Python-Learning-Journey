import os

#remove demo_file3.txt
#os.remove('demo_file3.txt')

#Check if file exists, then delete it:

if os.path.exists("demo_file3.txt"):
  os.remove("demo_file3.txt")
else:
  print("The file does not exist")

#To delete an entire folder, use the os.rmdir() method
os.rmdir('demo')