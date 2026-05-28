#first functiom === print("")
print("hello world")
print(23+349020)
print("my name is sarthak","my age is 19")


#variable : is a name given to a memory location in a program 
name = "sarthak dewangan"
print(name)
age = 19
print(age)
#here for eg we define a variable name=sarthak dewangan similarly we can define any variable and direcetly print it by writing the name of variable 
print("my name is :",name)


x = 2
y = 5 
add = x+y 
print(add)

#print(type())this will print a type of variable we are using 
print(type(name))
old = False 
print(type(old))
a = None
print(type(a))


#operators (types of operators):-

#1.arithmetic operator
a=5 
b=2 

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)#remainder
print(a ** b)#a^b  

#2.Relational operator(to compare the values)
a=20
b=50
print(a == b)#False
print(a != b)#!= mean not equal to 
print(a >= b)
print(a <= b)
 
#3.Assignment operators 
num = 10
#num = num + 10 
num += 10 #basically this gives us sum  
print(num)

#4.logical operators 
print(not False)#not False = True
print(not True)#not true = false

val1 = True
val2 = False
print(val1 and val2)#and use * operator 
print(val1 or val2)#or use + operator like a logic gates 

#type conversion (automatic conversion)
a=2
b=2.4
sum = a + b # a+b= 4.4
print(sum)

#if I will use a="2"(string) b=2.4(float) then it will give error . so for this we will use casting conversion which is manuall conversion
#type casting
a=1
b="2"
c=int(b)
sum = a + c
print(sum)

#input in python (to scan the input from the user)
name = input("Enter your name :")
print("welcome :",name)
first = int(input("Enter first number :"))
second = int(input("Enter second number :"))
print("Sum =", first + second)

