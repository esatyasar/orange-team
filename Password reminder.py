#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = "Rifat"

password = "A.Wx"

user_name = input("Please enter your name: ").strip().title()

if user_name == name :

    print(f"Hello, {name}! The password is : {password}")

else:

    print(f"Hello, {user_name}! See you later.")

