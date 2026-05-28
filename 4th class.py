#dictionary 
"""info = {
    "name" : "sarthak dewangan",
    "age" : 25,
    "t" : ("dict", "set"), 
}
print(type(info))
print(info)
print(info["age"])
info["surname"] = "dewangan"
print(info)
"""#nested dictionary 
"""student = {
    "name" : "sarthak ",
    "subjects" : {
        "phy" : 97,
        "chem" : 89,
        "maths" : 90, 
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.get("subjects"))
print(len(student))
student.update({"city" : "delhi"})
print(student)"""


#set : 
nums = {1,2,3,4,5}
sums = {1,2,2,2,2,3,3,3}
print(sums)
print(nums)
print(type(nums))

empty_set = set()
print(empty_set)
sums.add(9)
print(sums)
sums.remove(1)
print(sums)
print(sums.pop())
print(sums)
#sums.clear()
print(sums)
print(sums.union(nums))
print(sums.intersection(nums))