x = 10

def notChangeGlobalValue():
    x = 5
    print(f"Try to cahnge but both are diff : {x}")
    
def changeGlobalValue():
    global x
    x = 9
    print(f"use global keyword and change global var: {x}")
    
print(f"print before change: {x}")
notChangeGlobalValue()
print(f"print before change: {x}")
changeGlobalValue()