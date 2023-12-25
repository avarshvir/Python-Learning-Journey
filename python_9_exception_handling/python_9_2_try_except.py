try:
  print(x)
except ZeroDivisionError:
  print("Something else went wrong")
except NameError:
  print("Variable x is not defined")

