text = "fawzii"
# print(text.lower().islower()) # true
# print(text.lower().isupper()) # false
# print(len(text)) # size = 6
# print (text[0]) # f
# print(text.index("w"))  # 1
# print(text.replace("ii","y")) # fawzy
# *************************
from math import *

num = 2
# print(abs(-10))    # 10
# print(pow(num ,3)) # 8
# print(sqrt(16))     # 4
# print(max(num ,3)) # 3
# print(min(num ,3)) # num
# print(round(3.4))  # 3
# print(round(3.6))  # 4
# print(floor(3.4))  # 3
# print(ceil(3.4))   # 4
# *****************************
# name =input("enter the name : ")
# age = input("enter the age : ")
# print ("hello :  "+name +"\n" +"my age is : " +age)
# num1 = input("enter the num1 : ")
# num2 = input("enter the num2 : ")
# result =int(num1) + int(num2)
# print (result)
# ***********************

#  ******* list  *******

programming = ["c#", "c++", "python", "java"]
# print(programming[0]) #  c#
# print(programming[-1]) # java
# print(programming[1 : 3]) # c++ , python
# programming[0]="php"
# print(programming[0]) # php
# programming.append("fawzy") add elemant in last list
# print(programming)  #["c#","c++","python","java","fawzy"]
# programming.insert(2,"fawzy")
# print(programming)  #['c#', 'c++', 'fawzy', 'python', 'java']
# programming.remove("python")
# print(programming)  #['c#', 'c++', 'java']
# programming.clear()   # delete the all list
# print(programming)   #[]
# programming.pop() # delete the last elements
# print(programming) #  ['c#', 'c++', 'python']
# ind =programming.index("c++") # the number of place
# print(ind)  # 1
# programming.count("java")    #calculate the number of elements in list
# print(programming)    # 1
# programming.sort()
# print(programming)  #['c#', 'c++', 'java', 'python']
# new_list=programming.copy()
# programming.append("fawzy")
# print (new_list) #not change if the programming is changed  ['c#', 'c++', 'python', 'java']
# print( programming) #['c#', 'c++', 'python', 'java', 'fawzy']
# *************

# ******* tuple ********

tup = (25, 65, 89, 92)  # i cant change it
# tup[0]=66 # error
# print(tup[1]) #  65
# list_of_tuple=[(5,6),(6,41),(52,6)]
# print(list_of_tuple)      # i cant change it
# ****************
# *** function *****

#def printt(name ,age) :
  #print("hello " + name + "\nage is " + str(age))
# name =input("enter the name : ")
# age = input("enter the age : ")
#printt(name,age)
# *****
#def mmn (num):
# return num*num
#print(mmn(4)) #16
# **********

# **** if*****
""""
is_hungry=0
wants_to_eat =0
if is_hungry and wants_to_eat :
  print("go eat")
elif is_hungry and  not wants_to_eat :
  print("eat yalla")
else :
  print("im rich")
  """
# ***********
# build cal
"""
num1 =float (input("enter the num1 : "))
op=input("enter the operator  : ")
num2 = float(input("enter the num2 : "))
if op=="+":
  print(num1 + num2)
elif op=="-":
  print(num1 - num2)
elif op=="*":
  print(num1 * num2)
elif op=="/":
  print(num1 / num2)
elif op=="%":
  print(num1 % num2)
else :
  print("GO OUTSIDE")
        """
# **************
# **dictionary***
"""
dict={1 : "fawzii",
      2 : "shaker",
      "you" :[2,"son"] }
print(dict[1]) #fawzii
print(dict.get(2,"sorry")) #shaker
print(dict.get(3,"sorry")) #sorry  ,print sorry if the key(3) notfound
        """
# **************

# *** lop***

# **while****

'''
i=0
while i<=10 :

  i+=1
  if i==6 :
    continue
  if i==8 :
    break

  print(i)
else:
  print("stop")
      '''


# ******for****


#for x in "elfaraamawy" :
 # print(x)

"""
programming = ["c#", "c++", "python", "java"]
#print(len(programming)) # 4,the lenth of list

#for x in programming :
   #print(x)

for x in range(len(programming)) :
   print(programming[x])

for x in programming :
  if x=="python":
    print(x,"this true")
    break
  else 
  :
      print("thanks")
      
"""
#for x in range(2,5):     # 2  3 4
 #print(x)
# ***********
"""
def power(x,y):
  res=1
  for index in range(y) :
     res=res*x
  return res

num1 =float (input("enter the num1 : "))
num2 = float(input("enter the num2 : "))
print(power(10,2)) #100
"""

# ***2d list***
"""
list=[[1,2,3,],
     [4,5,6],
     [7,8,9]]
for row in list :
  for column in row :
    print(column,"\n")
    """


#*****try ,except*******
''''
try:
  #res=10/0
  num1 =int (input("enter the num1 : "))
  print(num1)
except ZeroDivisionError as err:  
  print(arr)
except ValueError as err2 :
  print(arr2)
print("finally")
'''
# **********
''''
programming = ["c#", "c++", "python", "java"]
for x in range(len(programming)):

  print(programming[x])
'''