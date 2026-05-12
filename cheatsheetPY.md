# 🐍 Python Cheatsheet

## File Handling
``` python
# Open a file
file = open("example.txt", "r")

# Read content
content = file.read()

# Example output:
# content = "This is the content of example.txt"

# Write to a file
with open("output.txt", "w") as f:
    f.write("Hello, world!")

# Example output:
# output.txt content: Hello, world!

# Append to a file
with open("output.txt", "a") as f:
    f.write("
Another line")

# Example output:
# output.txt content:
# Hello, world!
# Another line
```
## Exception Handling
``` python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("Execution completed.")

# Example output:
# Cannot divide by zero!
# Execution completed.
```
## Working with JSON

JSON (JavaScript Object Notation) è un formato leggero per lo scambio dati. Python fornisce il modulo json per codificare e decodificare dati JSON.
``` python
import json

# Convert Python object to JSON
json_data = json.dumps({"name": "John", "age": 25})

# Example output:
# json_data = '{"name": "John", "age": 25}'

# Convert JSON to Python object
python_obj = json.loads(json_data)

# Example output:
# python_obj = {'name': 'John', 'age': 25}
```
## List Manipulations
``` python
numbers = [1, 2, 3, 4, 5]

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Example output:
# evens = [2, 4]

# Map
squared = list(map(lambda x: x**2, numbers))

# Example output:
# squared = [1, 4, 9, 16, 25]

# Reduce (requires functools)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)

# Example output:
# product = 120
```
## Dictionary Manipulations
``` python
my_dict = {'a': 1, 'b': 2, 'c': 3}  # Get value with default value = my_dict.get('d', 0)  # Example output: # value = 0  # Dictionary comprehension squared_dict = {key: value**2 for key, value in my_dict.items()}  # Example output: # squared_dict = {'a': 1, 'b': 4, 'c': 9}
```