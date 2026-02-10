# 1. Print natural number up to n.

""" n = int(input("enter a number : "))
for i in range(1,n+1,1):
    print(i)"""

# 2. Reverse for loop. Print n to 1.

"""n = int(input("enter a number : "))
for i in range(n,0,-1):
    print(i)"""

# 3. Take a number as input and print its table.

"""n = int(input("enter a number : "))
for i in range(n,(n*10)+1,n):
    print(i)"""

# 4. Sum up to n terms.

"""n = int(input("enter a number : "))
sum = 0
for i in range(1,n):
    sum +=i  
print(sum)"""

# 5. Factorial of a number.

"""n = int(input("enter a number : "))
factorial = 1
if(n == 0):
    print("1")
else:
    for i in range(1,n+1):
        factorial *= i
    print(factorial)"""

# 6. Print the sum of all even & odd numbers in a range
# separately.

"""n = int(input("enter a number : "))
sumeven = 0
sumodd = 0
for i in range(1,n+1):
    if(i%2 == 0):
        sumeven += i
    else:
        sumodd += i
print("sum of even is : ",sumeven)
print("sum of odd is : ",sumodd)"""

# 7. Write a program that uses:
# one single-line comment
# one multi-line comment
# prints your name and age

# This is my single line comment

"""This is my multi line 
comment"""

"""name = input("enter your name : ")
age = int(input("enter your age : "))
print(f"Name : {name}\nAge : {age}")"""

# 8. Swap two numbers using a third variable.

"""x = int(input("enter first number : "))
y = int(input("enter second number : "))

print(f"X = {x}\nY = {y}")
temp = x
x = y 
y = temp 
print(f"Swap:\nX = {x}\nY = {y}")"""

# 9. find the sum of tow number.
""""a= 2
b= 3
print("Sum : "a+b)"""\

# Addition of two numbers using function.
def sum(a,b):
    return a+b
x = int(input("enter first no. : "))
y = int(input("enter second no. : "))
sum = sum(x,y)
print(f"Sum : {sum}")