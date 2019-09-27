#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def add(x,y):
    return x + y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print ("Enter any operator:")
print ("Add")
print ("sub")
print ("mul")
print ("div")
cho_opr = input ("choice any operator 1,2,3,4")

firstvalue = float(input ("Enter the first value"))
secondvalue = float(input ("enter the second value"))

if cho_opr == "1":
    print (firstvalue, "+", secondvalue, "=", add(firstvalue,secondvalue))
elif cho_opr == "2":
    print (firstvalue,"-", secondvalue, "=", sub(firstvalue,secondvalue))
elif cho_opr == "3":
    print (firstvalue, "*", secondvalue, "=", mul(firstvalue,secondvalue))
elif cho_opr == "4":
    print (firstvalue, "/", secondvalue, "=",div(firstvalue,secondvalue ))
else:
    print ("invalid syntax")


# In[3]:


fruits = ["apple","banana","mango","grapes"]
for fru in range(5):
        for fr in fruits:
            print(fr, end="  ")
        print()
        


# In[4]:


i = 0
while i < 6:
  
  if i == 3:
    continue
  i += 1
  print(i)


# In[5]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# In[6]:


i = 0
while i < 6:
  
  if i == 3:
    continue
    print(i)
    i += 1
 


# In[23]:


n = 10
while n > 4:
        n -=1
        print(n)
        


# In[8]:


n = 50
while n > 0:
    n -= 1
    if n == 25:
        continue
    print(n)


# In[7]:


for star in range(0,50):
    for star2 in range(0,star+1):
        print("*",end="")
    print()


# In[7]:


for star in range(0,50):
    for star2 in range(50,star,-1):
        print("*",end="")
    print()


# In[ ]:




