"""
character_age = "23"
print("there was a man called: " + character_name )
print("he was "+ character_age + " years old. ")
print("he liked the name: " + character_name)
print("but didn't like being " +character_age )
"""
"""
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
"""
"""""
phrase = "Girafe Acadimy"
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper().isupper())
print(phrase.isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("i"))
print(phrase.index("Acadimy"))
print(phrase.replace("Girafe","Elephent"))
"""""
"""""
print(2)
print(2.332)
print(-1)
print(3+4*5)
print(10 % 3)
print(str(5) + " my favorite number")
num = -5.2
print(abs(num))
print(pow(num,2))
print(max(num,5.3))
print(min(num,5,3))
print(round(3.7))
from math import *
print(floor(num))
print(ceil(num))
number = 25
print(sqrt(number))
"""""
''''
name = input("enter your name: ")
age = input("enter your age: ")
print("Hello " + name + " you are " + age + " old")
'''''
""""
#very basic calculator
num1 = input("enter first number: ")
num2 = input("enter  second number: ")
result = float(num1) + float(num2)
print(result)
"""
"""""
# mad libs
color = input("enter color: ")
plural = input("enter plural noun: ")
celebrity = input("enter celebrity: ")
print("roses are: " + color)
print(plural + " are blue")
print("i love: " + celebrity)
"""
"""""
# lists = arrays
friends = ["kevin","karen","jim","oscar","toby"]
friends[1] = "mike"
print(friends)
print(friends[0])
print(friends[2])
print(friends[-1])
print(friends[0:])
print(friends[1:3])
"""""
"""""
# list functions
lucky_numbers = [4,8, 42,23,16,15]
friends = ["kevin","karen","jim","oscar", "jim" ,"toby"]
friends.extend(lucky_numbers)
friends.append("creed")
friends.insert(1,"kelly")
friends.pop()
print(friends.index("kevin"))
print(friends.count("jim"))
lucky_numbers.sort()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
"""""
"""""
# tubles  is immutable{unchangable}
coordinates = (3,4)
coordinates[1] = 10
print(coordinates)
"""""
"""""
#functions
def say_hi ():
    name = input("enter name: ")
    print("i love python")
    print("Hello " + name + ", i'm the devolper")
def say_hi1(name, age):
    print("Hello "+ name+ "!" + " Your age is "+ str(age))
def cube(num):
    return num*num*num
# calling the fucntion
say_hi()
say_hi1("steve", 35)
print(cube(3))
"""""
"""""
# if statements
is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else :
    print("you are not a male or not tall")
"""""
"""""
# funtion to print the biggest of 3 numbers
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return  num2
    else:
        return num3
print(max_num(183,223,323))
"""""
"""""
#building a simple calculator
num1 = float(input("enter first number: "))
op = input("enter operator: ")
num2 = float(input("enter second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1 *num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operator")
"""""
"""""
# dicitionaries
monthconvertions = {
    "1" : "january",
    "2" : "febuary",
    "3" : "march",
    "4" : "april",
    "5" : "may",
    "6" : "june",
    "7": "july",
    "8": "august",
    "9": "septemper",
    "10": "october",
    "11": "november",
    "12": "december",
}
print(monthconvertions["8"])
print(monthconvertions.get("13","Not a valid key"))
"""""
"""
#  while loop
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop I\n")

# while loop example two
j = 20
while j>= 0:
    print(j)
    j -= 1
print("Done with loop J")
"""
""""
# basic guessing game
secret_word = "giraffe"
guess = ""
i = 0
flag = False
while guess != secret_word:
        print("Hint, The word is a tall animal")
        guess = input("Enter guess please: ")
        i += 1
        if i>=3:
            flag = True
            break
if flag:
    print("Out of guesses, You lose!")
else:
    print("You win!")
"""
"""
# for loop
friends = ["jim", "keren","kevin"]
for j in friends:
    for i in j:
        print(i)
for i in range(21):
    print(i)
    print(i+1)
"""
""""
# exponent function
#print(2**3)
def raise_to_power(basenumber, powernumber):
    result = 1
    for index in range(powernumber):
        result = result * basenumber
    return result
print(raise_to_power(3,4))
"""
"""""
# nested loops and 2D lists
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
for row in number_grid:
    for column in row:
        print(column)
"""""
'''
# building a translator
#giraffe language :: vowles are (g) , ex: cat is cgt
def translation(phrase):
    result = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            result += "g"
        else:
            result += letter
    return result
print(translation(input("enter phrase")))
'''
'''
# try except
try:
    #value = 10 / 0
    number = int(input("enter number: "))
    print(number)
except :
    print("Invalid input")
'''
'''
# read from files
employee_file = open("employee.txt", "r+")
for emplyee in employee_file.readlines():
    print(emplyee)
#print(employee_file.readlines())        # all the content is put in an array
employee_file.close()
'''
'''
# appending to the file
employee_file = open("employee.txt", "w") # a for append
employee_file.write("\nkelly - customer_services")
employee_file.close()
'''
'''
# importing files
import useful_tools
print(useful_tools.roll_dice(10))
'''
'''
#classses and objects
from student import student
student1 = student("jim","busness", 3.1, False)
student2 = student("pam", "art", 2.5, True)
print(student1.name)
print(student2.name)
'''