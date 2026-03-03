# 1. Print numbers from 1 to 10.

for i in range(1,11):
    print(i)



# 2. Print even numbers from 1 to 20.

for i in range(1,21):
    if i%2 == 0:
        print(i)



# 3. Find sum of first N numbers

n = int(input())
total = 0
for i in range(1,n+1):
    total += i
print(total)



# 4. Count how many numbers are divisible by 3 in a list.

list = [1,2,3,4,5,6,7,8,9,10,12]
count = 0
for i in list:
    if i%3 == 0:
        count += 1
print(count)



# 5. Print multiplication table of a number.

n = int(input())
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")