#!/usr/bin/env python
# coding: utf-8

# # Soru 1:
# Please write a poem you wanted in a .txt file and save it to the disk.

# In[21]:


with open("poem.txt",'w') as f: 
    f.write("Baktım gökte bir kırmızı bir uçak\nBol çelik bol yıldız bol insan\n")

with open("poem.txt", "r") as f:
    lines=f.read()
    
print (lines)
    


# # Soru 2:
# Append a new poem into the file you have created.

# In[22]:


with open("poem.txt",'a') as f: 
    f.write("Bir gece Sevgi Duvarını aştık\nDüştüğüm yer öyle açık öyle seçik ki")

with open("poem.txt", "r") as f:
    lines=f.read()
    
print (lines)
    


# # Soru 3:
# Read and print all poems.

# In[23]:


with open("poem.txt", "r") as f:
    lines=f.read()
    
print (lines)

