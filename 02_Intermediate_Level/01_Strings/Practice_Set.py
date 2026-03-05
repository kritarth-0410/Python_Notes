# 1. Take a string input and print its length.

name = input("Enter Your Name:")
print(len(name))   



# 2. Print the first and last character of a string.

str = "Python"
print(str[0])
print(str[-1])



# 3. Convert a string to uppercase.

name = "Samsung"
print(name.upper())



# 4. Count how many characters are in the string.

text = "Kritarth"
print(len(text))



# 5. Check if word "python" exists in the string.

sent = "Hi,  I am a python programmer"
print("python" in sent)



# 6. Check how many Vowels in given word. 

text = input()
count = 0
for i in text:
    if i in "aeiouAEIOU":
        count += 1
print(count)



# 7. Reverse the string.

text = "python"
for i in range(len(text)-1,-1,-1):
    print(text[i],end = "")