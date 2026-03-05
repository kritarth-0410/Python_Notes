# 1. What is a String ?

A String is a sequence of characters. 

Examples:

```python
name = "Kritarth"
language = "python"

Strings are written inside quotes.

"Hello"
'Hello'

Both Are Valid. 
```


# 2. String Indexation

```python
str = "Kritarth"

K  r  i  t  a  r  t  h
0  1  2  3  4  5  6  7

print(str[0])   # K
print(str[3])   # t
```


# 3. Negative Indexing

```python
str = "Kritarth"

K   r   i   t   a   r   t   h
-8 -7  -6  -5  -4  -3  -2  -1

print(str[-6])   # i
```


# 4. String Slicing

Syntax:
    string[start:end]

```python
name = "Yatharth"
print(name[1:7])   # athart
print(name[0:5])   # Yatha
```


# 5. String Length

Use len() function.

```python
name = "Kritarth"
print(len(name))  # 8
```


# 6. String Methods

## 1. Uppercase

```python
name = "Kritarth"
print(name.upper())   # KRITARTH
```

## 2. Lowercase

```python
name = "AMazOn"
print(name.lower())  # amazon
```

## 3. Replace

```python
name = "Hello Kritarth"
print(name.replace("Hello", "Hi"))  # Hi Kritarth
```

## 4. Split

```python
fruit = "apple mango banana"
print(fruit.split())   # ['apple', 'mango', 'banana']
```


# 7. String Concatenation

Joining Strings. 

```python
name = "Kritarth"
surname = "Bhargava"
print(name + " " + surname)  # Kritarth Bhargava
```


# 8. String Membership

Check if substring Exists.

```python
str = "Hello How Are You"
print("are" in str)  # False (python is case sensitive)
```


# 9. Common Mistakes

- Index out of range
- Forgetting slicing end is excluded
- Trying to modify string directly (strings are immutable)


# 10. Quick Revision

- String indexing
- Negative indexing
- Slicing
- len(), upper(), lower(), replace(), split()
- string concatenation