#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python Program to Find the Factorial of a Number?

# In[1]:


num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial cannot be computed for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)


# 2.Write a Python Program to Display the multiplication Table?

# In[2]:


num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 3.Write a Python Program to Print the Fibonacci sequence?

# In[3]:


n = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 4.Write a Python Program to Check Armstrong Number?

# In[8]:


num = int(input("Enter a number: "))
num_str = str(num)
n = len(num_str)
sum_of_cubes = sum(int(digit) ** n for digit in num_str)
if sum_of_cubes == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# 5.Write a Python Program to Find Armstrong Number in an Interval?

# In[9]:


lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
num = lower
while num <= upper:
    num_str = str(num)
    n = len(num_str)
    sum_of_cubes = 0
    for digit in num_str:
        sum_of_cubes += int(digit) ** n
    if sum_of_cubes == num:
        print(num)
    num += 1


# 6.Write a Python Program to Find the Sum of Natural Numbers?

# In[10]:


num = int(input("Enter a positive integer: "))
if num <= 0:
    print("Invalid input!")
else:
    sum = (num * (num + 1)) // 2
    print("The sum of first", num, "natural numbers is", sum)


# In[ ]:




