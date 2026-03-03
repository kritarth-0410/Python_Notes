# 1. What are Loops?

- Loops are used to repeat a block of code multiple times.
- Instead of writing the same code again and again, we use loops.


# 2. while Loop

Runs while condition is True.

```python
n = 1
while n <= 5:
    print(n)
    n += 1  # 1 2 3 4 5 
```


# 3. for Loop

Used to iterate over a sequence (range, list, string).

```python 
for i in range(1,6):
    print(i)   # 1 2 3 4 5 
```


# 4. range() Function

range(start, stop, step)

Examples:

```python
range(5) # 0 1 2 3 4
range(1, 6) # 1 2 3 4 5
range(1, 10, 2) # 1 3 5 7 9
```


# 5. Loop with list

```python
num = [1,2,3,4,5]
for i in num:
    print(i)
```


# 6. Break Statement

Stops the loop completely.

```python
for i in range(1,10):
    if i == 5:
        break
    print(i)  # 1 2 3 4 
```


# 7. Continue Statement

```python
for i in range(1,6):
    if i == 3:
        continue
    print(i) # 1 2 4 5 (skips 3)
```


# 8. Nested Loop

Loop inside loop.

```python
for i in range(1,5):
    for j in range(1,3):
        print(i, j)
```


# 9. Important Patterns

## 1. Sum of numbers

```python
nums = [1,2,3,4,5]
total = 0
for i in nums:
    total += i
    print(total)
```

## 2. Count Condition

```python
l = [1,3,2,4,5,6]
count = 0 
for i in l:
    if i%2 == 0: 
        count += 1
    print(count)
```


# 10. Common Mistakes

- Forgetting to update variable in while loop (infinite loop)
- Wrong indentation
- Using range incorrectly
- Writing condition wrong (like 1%2 instead of i%2)