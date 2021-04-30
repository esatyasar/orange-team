#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = int(input("Please Enter your Number ? "))
prime = " "
for i in range(2,number):
    if number<=1 :
        print("you number is invalid")
    else :
        if number%i == 0 :
            prime = "True"
            break
        else:
            continue
if prime == "True" :
    print(f"{number} is not a prime number")
else:
    print(f"{number} is  a prime number")
        

