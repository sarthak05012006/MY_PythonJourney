#string= is a datatype that stores a sequence of charecter 
str1 = "This is new project.\nI am going to start python"
print(str1)
str2 = "hello"
str3 = "world"
print(str2+str3) 
print(len(str1))
str = "Sarthak"
ch = str[2]
print(ch)
print(str[1:3])
print(str.endswith("kl"))
print(str.replace("a","o"))
print(str.find("a"))
print(str.count("a"))
name = input("Enter your name : ")
print(name)
age = 95
if(age >= 18):
    if(age >=80):
        print("cannot drive")
    else : 
        print("can drive")
else : 
    print("cannot drive")