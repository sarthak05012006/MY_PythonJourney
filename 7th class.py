class student :
    clg_name = "UTD CSVTU" #clg_name is class attribute as commom for all
    def __init__(self,fullname,age):
        self.name = fullname #self.name and self.age are instance attributes
        self.age = age
    def welcome(self):
        print("hello")
    
    #Static Methods : methods that don't use the self paramaneter .... 
    @staticmethod #decorator
    def Print():
        print("Hellow world")

s1 = student("Karan",20)
s1.welcome()
s1.Print() 