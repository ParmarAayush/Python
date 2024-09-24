class Person:
    name = "Aayush"
    occupation = "Student"
    def info(self): ## self is object for which we call method
        print(f"{self.name} is a {self.occupation}")
        

p1 = Person()
p1.name = "Aniket"
p1.info()

p2 = Person()
p2.name = "Aayush"
p2.info()