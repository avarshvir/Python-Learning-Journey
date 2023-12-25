try:
    a = 10/0
    print(a)
except ZeroDivisionError:
    print("Division by zero")
except NameError:
    print("Name Error")
else:
    print("Divide Successfuly")
finally:
    print("Always Executed")

try:
    # Code that might raise an exception
    result = int("abc")
except (ValueError, TypeError):
    # Handle multiple exceptions
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    # Handle another exception
    print("Cannot divide by zero.")
