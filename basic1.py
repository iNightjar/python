# simple basic codes and tricks
'''
print ("hello man")
print("it's good to see you\n")
a = 3
b = 2
print(a and b) # boleon addition
print(a**b)  # A raised to power B
print(a//b) # floor division
print(not a)
print(not b)
list  = [1,2,3,4,5]
print(list)
stuff_new = [2,4,"bacon", False , 5, "e"]
stuff_new = [2,4,"bacon", False , 5, "e",[3, "Great", "cyber"]]
print(stuff_new)
print(len(stuff_new))
stuff_new [0]  = 7
print(stuff_new)
stuff_new.append(3)
print(stuff_new)
stuff_new.pop()
print(stuff_new)
print(stuff_new[:4]) # from the beginning to num:4
print(stuff_new[2:]) # from num:2 to the end
print(stuff_new[-1]) # elements from the end of list
print(stuff_new[-4:-1])
stuff_new[2]  = "changed"
print(stuff_new)
for x in stuff_new:
    print(x)
if  "change" in stuff_new:
    print("found")
else:
    print("Not found")
stuff_new.append("blue")
print(stuff_new)
stuff_new.pop()
print(stuff_new)
'''
'''
# dictionary
person_one = {"Name" : "John", "Age" : "35", "sex" : "male", "passion" : "cybersecurity", "married" : "True"}
person_two = dict()
print(type(person_two))
print(person_one)
person_one["married"] = False
print(person_one)
print(person_one["Age"])
print(person_one.values())
print(person_one)
'''
'''
a = 25
b = 20
c = 40
if a<b or b>c:
    print("A is smaller than B or B is Greater then C")
else:
    print("No condition was executed")
'''
'''
list = ["i" , "am", "learning", "Python","for","cybersecurity"]
for element in list:
    print(element)
for i in range(10):
    print(i)
for i in range(0,10,2):
    print(i)
'''
'''
list = ["i" , "am", "learning", "Python","for","cybersecurity"]
j = 0
while j<len(list):
    print(list[j])
    j = j + 1
'''
'''
import  os
def systeminfo():
    return  os.system("systeminfo > systeminfo.txt")
file = open("systeminfo.txt","r+")
for i in file.readlines():
    print(i)
file.close()
'''
'''
class BasicMath:
    def summing(self, a, b):
        return a + b
    def multy(self, a, b):
        return a * b
    def raiseit(self, a, b):
        return a**b
first_calc = BasicMath()
print(first_calc.multy(8, 3))
second_calc = BasicMath()
print(second_calc.raiseit(4,5))
'''
'''''
with open("data.txt", "r") as f:
    for line in f:
        print(line)
    f.close()
'''''
'''
list = ["pass123","youcantguessme","bravo" ,"awesome"]
with open("data.txt", "a") as f:
    for password in list:
        f.write(password)
        print(password)
    f.close()
with open("data.txt", "r+")as f:
    for i in f.readlines():
        print(i)
    f.close()
'''