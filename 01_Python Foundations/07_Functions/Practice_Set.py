# 1. Write a function that returns the square of a number.

def square(a):
    return a ** 2

result = square(6)
print(result)



# 2. Write a function that returns the sum of two numbers.

def add(a,b):
    return a + b

x = add(3,7)
print(x)



# 3. Write a function that returns the largest number in a list.

def largest(l1):
    largest = l1[0]
    for i in l1:
        if largest < i:
            largest = i
    return largest

l1 = [1,4,2,7,6,5]

print(largest(l1))



# 4. Write a function that returns how many even numbers are in a list.

def even(nums):
    count = 0
    for i in nums:
        if i%2 == 0:
            count += 1
    return count

nums = [1,2,3,45,6,7,8,9]
print(even(nums))



# 5. Write a function that return sum of numbers in list.

def add(nums):
    total = 0
    for i in nums:
        total += i
    return total 
nums = [1,2,3,4,5]
print(add(nums))



# 6. Write a function that returns the smallest number in a list.

def smallest(l1):
    smallest = l1[0]
    for i in l1:
        if smallest > i:
            smallest = i
    return smallest

l1 = [8, 3, 10, 2, 6]
print(smallest(l1))



# 7.  Write a function that return only prime number.

def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(prime(5))
print(prime(9))


#  8. Write a function to reverse a text.

def reverse(text):
    rev = ""
    for i in text:
        rev = i + rev
    return rev

print(reverse("python"))