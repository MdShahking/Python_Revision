# print("Entered to Practice set")

from http.cookies import BaseCookie


a= 3
b= 2.5 
c="sonu"
print(a)
print(b)
print(c)
# *****************Data Types *******************
print(type(a))
print(type(b))
print(type(c))
# ***********Arithmetic Operators****************
print("The value of a+b:" , a + b )
print("The value of a-b:" , a - b )
print("The value of a*b:" , a * b )
print("The value of a/b:" , a / b )
# ************* Comparison operators *****************
e = a > b
print(e)
# **************Logical operators**********
bool1= True
bool2= False
print("the value of bool1 and bool2 is : " , bool1 and bool2)
print("the value of bool1 or bool2 is : " , bool1 or bool2)
print("the value of not bool2 is : " , not bool2)
# **************Type casting*************
f="786"
print(type(f))
f=int(f)
print(type(f))
print(f+14)
#*************** Input Function ***************
# g = input("Enter your name: " )
# g1= int(input("Enter your age: " ))
# print(type(g1))
# print(g)
# print(g1)
# ************ Average of Two Numbers Entered By the User **********
# h1=int(input("Enter the first number: "))
# h2=float(input("Enter the second number: "))
# Avg_H=(h1 + h2)/2
# print("Average of two nubers is : " , Avg_H)
# ************ Square of number Entered By the user**********
# I=int(input("Enter the number to get the square root : "))
# Isquare= I * I
# print("Square of the number is :  " , Isquare)
# ************ strings slicing ***************
# word = "my name is king shahnawaz.\n he is the most kind and mercifull king of all times"
# print(word [0 : 15 : 3])
# print(len(word))
# print(word.endswith("r"))
# print(word.count("a"))
# print(word.capitalize())
# print(word.replace("shahnawaz" , "sonu"))
# *****************Practice questions on strings**********************
# g=input("Enter your name : " )
# print("Good AfterNoon " , g )
name = ("Enter the name of the c  andidate")
# date1 = input("Enter today's date")
# print("dear", name )
# print("You are selected for the role \n thnak you\n" , date1)
# print(name.find("  "))
# print(name.replace("  "," "))
# **************Lists and Tuples ***************
# myLists = [2,34,23,35.4,97,74] 
# print(myLists)
# myLists.append(69)
# myLists.reverse()
# myLists.sort()
# print(myLists.sort())
# print(myLists[2])
# print(myLists)
# *************Dictionary****************
myDict = {"Book" : "Rich dad poor dad", 
"school" : "dav" ,
"girlfriend" : "soni", 
"fruit" : "apple" , }
# print(myDict["fruit"])
print(myDict.items())



