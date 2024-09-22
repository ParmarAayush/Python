try:
    num = int(input("Enter an integer number: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number Entered is not an integer.")
except IndexError:
    print("Index Error")
finally:
    print("I am always execute")  
