class Studnet:
    
    def setName(self, name):
        self.name =  name
        
    def getName(self):
        print(self.name)
        return self.name
    
obj = Studnet()
obj.setName("Aayush")
obj.getName()