def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

calculateGmean(10,20)

# default argumetn 
def grret(name="mr/ms"):
    print(f"hello {name}")
    
grret("Aayush")
grret()

# varibel length arguments :  pass n number of agrument 
def average(*numbers):
    type(numbers) # take number as a tuple 
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is ", sum / len(numbers)) 

average(10,20,30,40)

# variable length as dictionary
def name(**name):
    print(type(name))
    print("hello", name["fname"], name["mname"], name["lname"]) 
    
name(mname = "Gulabsnh", fname = "Aayush", lname = "Parmar")

# Return keyword
def average(*numbers):
    type(numbers) # take number as a tuple 
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum
print(average(22,25,23))