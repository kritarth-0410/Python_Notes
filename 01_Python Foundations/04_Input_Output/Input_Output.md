# 1. Output in Python

Output is printed using `print()`.

```python
print("Hello") # Hello
print(10) # 10
print(5 + 3) # 8
```


# 2. Multiple Values in print()

```python
name = "Kritarth"
age = 18

print(name, age) # Kritarth 18
```
By default, values are separated by space.


# 3. Custom Separator

```python
print("Python", "Java", "C++", sep="-") # Python-Java-C++
```


# 4. Custom End Parameter

```python
print("Kritarth", end = " ")
print("Bhargava")
```
Output:
    Kritarth Bhargava


# 5. Taking Input

`input()` takes user input as string.

```python
name = input()
```


# 6. Taking Integer Input 

```python
age  = int(input("Enter age"))
```


# 7. Taking Float Input

```python
price = float(input("Enter price"))
```


# 8. Taking Multiple Inputs in One Line

```python
a, b = map(int, input().split())
print(a, b)
```


# 9. Taking List Input

```python
1 2 3 4 5
nums = list(map(int, input().split()))
print(nums)
```


# 10. Formatted Strings (f-strings)

```python
name = "Kritarth"
age = 18
print(f"my name is {name} and my age is {age}")
```


# 11. Common Mistakes

- Forgetting int() conversion
- Forgetting .split() for multiple inputs
- Writing map(int, input()) without .split()


# 12. Quick Revision

- input() returns string
- map() + split() for multiple inputs
- Use f-strings for formatting