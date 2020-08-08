#!/usr/bin/env python
# coding: utf-8

# # Soru 1:
# Please get Celcius or Fahrenheit degrees from users and type a code to convert these heat units to each other.
# For conversion, please use this formula: C = (5/9) * (F - 32)
# 
#  Example : "40C" --> "104F"
#            "52F" --> "11.1C"

# In[10]:


F=float(input("Fahrenheit: "))
C=(5/9)*(F-32)
print("Celcius= {} ".format(C))


# # Soru 2:
# A company decided to give a bonus of 5% to the employees if his/her year of service is more than 5 years. Ask the user for their salary and year of service and print the net bonus amount.

# In[13]:


salary=float(input("Your salary: "))
service=int(input("Year of service: "))

if service>5:
    bonus=(salary)*(0.05)
    print("Your net bonus amount:",bonus)
else:
    print("No bonus!")
    


# # Soru 3:
# Take input of ages of 3 people by the user and determine the oldest and youngest among them.

# In[28]:


v1=int(input("Your age: "))
v2=int(input("Your age: "))
v3=int(input("Your age: "))

list_of_age=[v1,v2,v3]
 
print("The oldest and the youngest ages: ",max(list_of_age),min(list_of_age))


# # Soru 4:
# A student will not be allowed to attend to the exam if his / her attendance to classes is less than 75%. Take followings input from the user:
# 
# Number of classes held,
# Number of classes attended.
# 
# Then, print the percentage of classes attended and whether the student is allowed to attend in an exam or not.

# In[31]:


classes=int(input("Number of classes: "))
attended=int(input("Classes of attended: "))

print("Percentage of classes attended: {} ".format(attended/classes))

if (attended/classes)<0.75:
    print("You couldn't attend the exam!")
else:
    print("You can attend the exam")
    


# # Soru 5:
# In this exercise, you will create a program that reads a letter of the alphabet from the user. According to the answer:
# 
# * If the user enters a, e, i, o, u, then your program should display a message indicating that the entered letter is a vowel.
# 
# * If the user enters y, then your program should display a message indicating that y is sometimes a vowel and sometimes a consonant.
# 
# * Otherwise, your program should display a message indicating that the letter is a consonant.

# In[40]:


vowel=["a","e","i","o","u"]
cons_vo=["y"]

user_alph=input("Enter an alphabet: ")

for i in range(0,len(vowel)):
    if user_alph==vowel[i]:
        print("vowel")
    elif user_alph=="y":
        print("a vowel and a consonant")
    else:
        print("Consonant")
    break
        


# In[ ]:




