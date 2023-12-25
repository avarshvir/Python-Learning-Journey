class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("This is a custom exception.")
except MyCustomError as e:
    print(f"Custom Exception: {e}")
