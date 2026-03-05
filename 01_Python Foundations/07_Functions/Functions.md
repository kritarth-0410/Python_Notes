# 1. What is a Function?

A function is a reusable block of code that performs a specific task.

Functions help in:
- reducing code repetition
- making programs modular
- improving readability

```python
def greet():
    print("Kritarth")
greet()      # Kritarth
```


# 2. Function Syntax

```python
def function_name():
    print("We welcomes you")

function_name()
```


# 3. Function with Parameters

Parameters allow us to pass values to functions.

```python
def greet(name):
    print("Hello", name)

greet("Kritarth")      # Hello Kritarth
```


# 4. Function with Return Value

A function can return a result using the return keyword.

```python
def sum_numbers(a,b):
    return a + b

result = sum_numbers(5,3)
print(result)
```


# 5. Multiple Parameters

Functions can take multiple parameters.

```python
def multiply(a, b):
    return a * b
```


# 6. Default Parameters

A parameter can have a default value.

```python
def greet(name = "Kritarth"):
    print("Hello", name)

greet()         # Hello Kritarth
greet("Ram")    # Hello Ram
```


# 7. Why Functions are Important

- Functions help to:
- organize code
- reuse logic
- simplify large programs


# 8. Common Mistakes

- forgetting parentheses while calling function
- incorrect indentation
- missing return statement


# 9. Quick Revision

- function definition using def
- parameters
- return value
- default parameters