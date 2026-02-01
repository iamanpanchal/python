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

