class Person:
    ## it is special method it is called constructor
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        
    def info(self): ## self is object for which we call method
        print(f"{self.name} is a {self.occupation}")
        

p1 = Person("Aniket", "Studnet")
p2 = Person("Aayush", "Student")

p1.info()
p2.info()