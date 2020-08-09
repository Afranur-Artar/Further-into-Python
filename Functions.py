#!/usr/bin/env python
# coding: utf-8

# # Soru 1:
# A prime number is an integer greater than one that is only divisible by one and itself. Write a function that determines whether or not its parameter is prime, returns True if it is and False otherwise. Write a main program that reads an integer from the user and displays a message indicating whether or not it is prime. Ensure that the main program does not run if the file containing your solution is imported into another program.

# In[ ]:


def asal():
    number=int(input("Enter an integer: "))
    
    if number < 2:
        return
    elif number == 2: 
        return
    else:
        
        for i in range(3,number):
            bolundu = False
            for j in range(2,i):
                if i % j == 0:
                    bolundu=True
                    break
            if bolundu == False:
                print (i)
asal()


# # Soru 2:
# Please write a function that passes each element of a list only once to a new list. We usually do this with the set() command, but let us not use this command this time.
# 
# Example:
# 
#  unique_list([1,2,2,3,3,4,4]) = [1,2,3,4] <br><br>

# In[ ]:


def unique(list1):
    unique_list=[]
    
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    for i in unique_list:
        print(i)
    


# # Soru 3:
# There are many built-in modules in Python. By importing one of the modules on time, write a function that takes the date of birth as a parameter and returns the age.

# In[ ]:


from datetime import datetime, date

print("Your date of birth (dd mm yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

print(age)


# # Soru 4:
# Get a number from the user and calculate the factorial of it by using a function.

# In[4]:


def factori():
    number=int(input("Enter an integer: "))
    fact=1
    i=1
    for i in range(2,number+1):
        fact=fact*i
    print("Your number's factorial is: {}".format(fact))
    return fact

factori()


# # Soru 5:
# Write a function named perfect() that determines if the parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
# 
# An integer number is said to be a perfect number if its factors (including 1, but not the number itself) sum to the number.
# 
#  E.g.: 6 is a perfect number because 6 = 1 + 2 + 3.<br><br>

# In[1]:


def Perfect(Number):
    Sum = 0
    perfect_number=[]
    
    for i in range(1, Number):
        for j in range(1,i):
            if(Number % i == 0):
                Sum = Sum + i
            if (Number == Perfect(Number)):
                perfect_number.append()
    return perfect_number 
    print("Perfect numbers:  ",perfect_number)
    
# Öğrenilecek !!!


# In[2]:


Perfect(100)


# # Soru 6:
# Write a Python function that prints out the first n rows of Pascal's triangle.

# In[3]:


def pascal(yukseklik, satirlar=[]):
    satirlar.append([1])
    satir=[1]
    for i in range(yukseklik):
        sonraki = 0
        siradaki_satir = []
        for k in satir:
            siradaki_satir.append(sonraki + k)
            sonraki = k
        siradaki_satir.append(1)
        
        satir = siradaki_satir
        satirlar.append(satir)
    
    return satirlar
 
sayi = int(input("Pascal üçgeninin kaç satırını hesaplamak istiyorsunuz: "))
 
for x in pascal(sayi):
    print(x)


# In[ ]:




