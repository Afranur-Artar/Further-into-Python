#!/usr/bin/env python
# coding: utf-8

# Yöntemleri (methods) ve değişkenleri (variables) olan yeniden kullanılabilir bir kod yığını

# # Soru 1:
# In a retail application, many customers visit the retail outlet to purchase various items. The manager of the retail outlet now wants to keep track of all its items' and customers’ data. To achieve this purpose, please:
# 
# * Define two classes named as item (with item_name and price attributes) and customer (with customer_id, phone_number attributes and purchase method).
# * purchase method should calculate the total price with the given item name amount.
# * Create an item.
# * Create a customer with an arbitrary ID and number.
# * Make customers buy an item with an arbitrary amount and then print the total price.

# In[ ]:


class item():
    def __init__(self, item_name, price):
        self.item_name=item_name
        self.price=price
        
        return (self.item_name,self.price)     
    
        
    


# In[ ]:


class customer(item):
    def __init__(self, customer_id, phone_number, purchase):
        self.customer_id=customer_id
        self.phone_number=phone_number
        item.__init__(self, item_name,price)
        self.purchase=item.__init__(self, item_name,price)
        
        return(self.customer_id,self.phone_number,self.purchase)
        


# In[ ]:


x=item('Tshirt',60)
y=customer(1234,5057678936)

