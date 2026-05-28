#functions...
"""def calSum(a,b):
    sum = a+b
    print(sum)

calSum(2,3)
#or 
def cal_sum(c,d):
    return c + d

sums = cal_sum(3,5)
print(sums)
"""
def Pri():
    print("hello")
    #return "hello"

output = Pri()
print(output) # it gives none because function was not returning any thing 
def Mul(a=1,b=2):
    print(a*b)
    return a*b
Mul()



cities = ["delhi","mumbai","calcutta","hydreabad","goa","raipur","risali"]
def count(list):
    print(len(list))
def printList(list):
    for item in list :
        print(item, end = " ")
count(cities)
printList(cities)
print(cities)

def rec(n):
    if (n==0):
        return 0 
    print(n)
    rec(n-1)
rec(6)