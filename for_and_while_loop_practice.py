# -*- coding: utf-8 -*-
"""For and While Loop Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/104ZdaDhYUYF6Q7DU_E28gVtKz4CuSxdx
"""

'''''''''''''For Loop''''''''

fruits = ["apple","banana","mango","grapes"]
for fru in range(5):
        for fr in fruits:
            print(fr, end="  ")
        print()

i = 0
while i < 6:
  
  if i == 3:
    continue
  i += 1
  print(i)

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

n = 10
while n > 4:
        n -=1
        print(n)

n = 50
while n > 0:
    n -= 1
    if n == 25:
        continue
    print(n)