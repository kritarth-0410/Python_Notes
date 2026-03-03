# # 1. Take an integer input.
# # Print:
# # "Positive Even"
# # "Positive Odd"
# # "Negative"
# # "Zero"

n = int(input())
if n > 0:
    if n%2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif n == 0:
    print("Zero")
else:
    print("Negative")



# # 2. Take two integers in one line.
# # Print the greater number without using max(). 

l = list(map(int, input().split()))

largest = l[0]
for i in l:
    if largest < i:
        largest = i
        print("largest is", largest)



# # 3. Take integer N. Print sum of numbers from 1 to N using loop.

N = int(input())
sum = 0
for i in range(1,N+1):
    sum += i
print(sum)



# # 4. Take space-separated integers input. Print count of numbers divisible by 3.

nums = list(map(int, input().split()))
count = 0
for i in nums:
    if i%3 == 0:
        count += 1
print(count)



# # 5. Take integer N. Print patterns

N = int(input())

for i in range(1, N+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()