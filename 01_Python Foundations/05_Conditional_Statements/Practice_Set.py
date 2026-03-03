# 1. Take a number and print if it is positive, negative, or zero.

num = int(input())
if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")



# 2. Take two numbers and print the larger one.

a = int(input())
b = int(input())
if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Both Are Equal")



# 3. Take a year and check if it is a leap year.

year = int(input())
if (year%4 == 0 and year%100 != 0) or (year % 400 == 0):
    print("Leap Year", year)
else:
    print("Not Leap Year", year)



# 4. Take marks and print grade based on ranges.

marks = int(input())

if marks >= 90:
    print("Congrats! You got Grade A")
elif marks >= 75:
    print("Congrats! You got Grade B")
elif marks >= 50:
    print("Nice Try! You got Grade C")
else:
    print("Failed!!")