#!/usr/bin/env python
# coding: utf-8

# # Errors:
# 3 farklı hata yapısı vardır: compile time errors, run time errors, logical errors. Compile time errors ise syntax ve semantic errors lardan oluşmaktadır. Logical errors larda hata mesajı yoktur, anlaşılması zor olabilir.
# 
# # Exceptions:
# try except komutuy kullanılır.

# # Soru 1:
# Let us define a division operation inside a function (using def) but to get an error, define the denominator as 0. So, type properly except statement.

# In[1]:


def division(number1,number2):
    try:
        return (number1/number2)
    
    except Exception as e:
        print ("'{}' error occurred! ".format(e)) 
        


# # Soru 2:
# It is possible to get multiple errors after the execution of one try block. So, please define an error-exception issue with NameError.

# In[6]:


try:
    print(x)
except NameError:
    print("Variable x is not defined")


# # Soru 3:
# Please define a function and with this function, generate a ValueError exception simply by entering a string instead of numerical value.

# In[7]:


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    
    except ValueError:
        print('Wrong data type') 

