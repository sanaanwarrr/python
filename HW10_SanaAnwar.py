class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = [] 

    def teach(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")

    def knows(self, trick):
        if trick in self.tricks:
            print(f"Yes, {self.name} knows {trick}")
            return True
        else:
            print(f"No, {self.name} doesn't know {trick}")
            return False

if __name__ == "__main__":
    sugar = Dog('Sugar', 'border collie')
    print(sugar.name) 
    print(sugar.breed) 

    print(sugar.tricks)  


    sugar.teach('frisbee') 


    print(sugar.knows('frisbee')) 
    print(sugar.knows('arithmetic')) 


    print(Dog.species)  
    print(sugar.species)  