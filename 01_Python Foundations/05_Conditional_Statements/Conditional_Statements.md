# 1 . What are Conditionals

Conditionals allow a program to  make decisions.


# 2. if Statement

```python
x = 10
if x > 10:
    print("Greater Than 10")
```


# 3. if-else Statement

```python
a = int(input())
if a%2 == 0:
    print("Even")
else:
    print("Odd")
```


# 4. if-elif-else Ladder

```python
marks = int(input())
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```


# 5. Nested if

```python
x = int(input())
if x > 0:
    if x%2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative Number")
```


# 6. Logical Operators in Conditions

```python
age = int(input())
if age >= 18 and age <= 60:
    print("You Are Elegible")
else:
    print("Age Criteria Doesn't Matches")
```


# 7. Short Method

```python
n = int(input())
result = "Even" if n%2 == 0 else "Odd"
print(result)
```


# 8. Important Notes

- Indentation is mandatory
- Condition must return True or False
- Use == for comparison, not =


# 9. Common Mistakes

- Using = instead of ==
- Forgetting indentation
- Incorrect condition order in elif ladder


# 10. Quick Revison

- if
- if-else
- if- elif ladder
- Nested if
- Logical operators