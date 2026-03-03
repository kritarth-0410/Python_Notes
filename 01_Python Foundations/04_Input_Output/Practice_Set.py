#  1. Take two numbers in one line and print their product.

a, b = map(int, input().split())
print(a * b)



#  2. Take 5 space-separated numbers and print their sum.

nums = map(int, input().split())
print(nums)
total = 0
for i in nums:
    total+=i
print(total)



#  3. Take name and marks and print:
#   "Student <name> scored <marks> marks"

name = "Kritarth Bhargava"
marks = 99
print(f"Student {name} scored {marks} marks")