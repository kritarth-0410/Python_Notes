# 1. What is a List?

A list is a collection of multiple values stored in a single variable.

Example:

```python
nums = [1, 2, 3, 4]

Lists can store different data types.

data = [3, 3.12, "Kritarth"]
```


# 2. List Indexing

Each element has an index.

```python
data = [1,3, "python"]
print(list[1])   # 3
print(list[0])   # 1
```


# 3. Negative Indexing

Python allows negative indexing.

```python
nums = [1,2,5,3,4]
print(nums[-1])   # 4
print(nums[-5])   # 1
```


# 4. List Slicing

```python
l1 = [1,2,3,4,5,6,7,8,9]
print(l1[1:6])   # [2,3,4,5,6]
```


# 5. Insertng Element

Adds element at specific index provided.

```python
l1 = [1,3,4,5,6,7]
l1.insert(1, 2)
print(l1)   # [1,2,3,4,5,6,7]  Add 2 in index 1
```


# 6. Adding Element

Adds element at the end.

```python
l1 = [1,2,3,4,5,6,7]
l1.append(8)
print(l1)   # [1,2,3,4,5,6,7,8]
```


# 7. Removing Element

Removes specific value.

```python
l1 = ["kritarth", "ram", "ravan"]
l1.remove("ravan")  
print(l1)    #  ["kritarth", "ram"]
```


# 8. Pop()

Removes last element.

```python
nums = [1,2,3,4]
nums.pop()
print(nums)   # [1,2,3]
```


# 9. List Length 

```python
l1 = [1,2,3,4]
print(len(l1))   # 4
```


# 10. Looping Through list

```python
nums = [1,2,3,4]
for i in nums:
    print(i)
```


# 11. Checking Elements

```python
l1 = [10,20,30]
print(20 in l1)   # True
```


# 12. Sorting

```python
l1 = [1,2,5,4,8,9,0]
li.sort()
print(l1)    # [0,1,2,4,5,8,9]
```


# 13. Common Mistakes

- Index out of range
- Forgetting list uses []
- Confusing append() and insert()


# 14. Quick Revision

- List creation
- Indexing
- Slicing
- append()
- insert()
- remove()
- pop()
- len()
- sort()