#!/usr/bin/env python
# coding: utf-8

# # Soru 1:
# Please form a multiplication table from user input.

# In[49]:


x=int(input("Please enter an integer: "))

i=1
while i<11:
    print("{} * {}= {}".format(x,i,x*i))
    i=i+1
    if i>=11:
        break


# # Soru 2:
# Simply by using list compherension, form a list by taking square of odds numbers and by calculating cube of even numbers from 1 to 20.

# In[50]:


odd=[]
even=[]

i=1
while i<21:
    if i%2==0:
        even.append(i**3)
    elif i%2!=0:
        odd.append(i**2)
    i=i+1
    if i>=21:
        break
print("Even numbers are: ",even)
print("Odd numbers are: ",odd)
        
        


# # Soru 3:
# Please type a code that inverts the initial user input.
# 
# Example : "automobile" --> "elibomotua"

# In[ ]:


word=input("Please enter a word: ")

for i in range(0,len(word)):
    
    # Nasıl çözülür!!


# In[ ]:





# # Soru 4:
# Using range(1, 201), make two lists. One is containing all even numbers and the other containing all odd numbers.

# In[2]:


even=[]
odd=[]

i=1
for i in range(1,201):
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
        
print("Even lists: ",even,"\n")
print("Odd lists: ",odd)


# # Soru 5:
# Define a function called count that has two arguments called sequence and item. Return the number of times the item occurs in the list.
# 
# Example:
# 
# count([1,2,1,1], 1)
# It should return 3. Because 1 appears 3 times in the list.

# In[ ]:


counts=[[1,2,1,1], 1] 

for i in range(0,len(count)):



# # Soru 6:
# Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits as a single-digit number.
# 
# Example:
# 
#  27684 --> 2 + 7 + 6 + 8 + 4 = 27 --> 2 + 7 = 9<br>

# In[41]:


numb=int(input("Enter a positive integer: "))
str_numbr=[]

sum_numbers=0
if numb<10:
    print("Sum of all that number's digits: {}".format(numb))
elif numb>10:
    numb=str(numb)
    print(type(numb))
    str_numbr.append(numb)
    for i in range(0,len(str_numbr)):
        str_numbr=int(str_numbr[i])
        print(type(str_numbr))
        sum_numbers=sum_numbers+str_numbr
        i=i+1
        str_numbr=[]
        numb=str(numb)
        str_numbr.append(numb)
print("Sum of all that number's digits are: ",sum_numbers)
                

# Nasıl çözülebilir?


# # Soru 7:
# Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.

# In[10]:


sayı1=int(input("Sayı1: "))
sayı2=int(input("Sayı2: "))
i=1
ebob=1

while (i<=sayı1 and i<=sayı2):
    if (not (sayı1%i) and not (sayı2%i)):
        ebob=i
    i+=1
print("Ebob: ",ebob)
            


# # Soru 8:
# Write a Python program that iterates integers from 1 to 50. For multiples of three print fizz instead of the number and for the multiples of five print buzz. For numbers which are multiples of both three and five print fizzbuzz.
# 
# 1 den 50 ye kadar sayılardan 3ün katları için fizz; 5 in katları için de buzz yazdır.

# In[ ]:


mult_three=[]
mult_five=[]
three_five=[]

for i in range(1,50):
    if i%3==0:
        mult_three.append("fizz")
print("Multiples of three: {}".format(mult_three),"\n")
    
for i in range(1,50):
    if i%5==0:
        mult_five.append("buzz")
print("Multiples of five: {}".format(mult_five),"\n")
    
for i in range(1,50):   
    if i%3==0 and i%5==0:
        three_five.append("fizzbuzz")
print("Multiples of both three and five: {}".format(three_five))
        
        


# # Soru 9:
# Please form a list out of Fibonacci numbers from 1 to 50. The first two Fibonacci numbers are 1. The next numbers are the sum of the previous two.

# In[ ]:


a=1
b=1
fibonacci=[a,b]

for i in range(1,50):
    a,b=b,a+b
    fibonacci.append(b)
print("Fibonacci numbers {} dir".format(fibonacci))

