# Sana Anwar
# CS 100 H FALL 2023
# Homework 10 - User-Defined Classes

"""
Problem 1: Write a class definition line and a one line docstring for the class Dog. Write an __init__ method for 
the class Dog that gives each dog its own name and breed. Test this on a successful creation of a Dog object.

Problem 2: Add a data attribute tricks of type list to each Dog instance and initialize it in __init__ to the empty list. 
The user does not have to supply a list of tricks when constructing a Dog instance. Make sure that you test this successfully.

Problem 3: Write a method teach as part of the class Dog. The method teach should add a passed 
string parameter to tricks and print a message that the dog knows the trick.

Problem 4: Write a method knows as part of the class Dog. The method knows should check whether a passed string 
parameter is in the dog’s list of tricks, print an appropriate message and return True or False.

Problem 5: Create a class attribute species of type str to be shared by all instances of the class Dog and set its value to 'canis familiaris'. 
The class attribute species should be defined within the class Dog but outside of any method.
"""

# Problem 1:
class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        # Problem 2:
        self.tricks = [] 

# Problem 3:
    def teach(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} knows {trick}")

# Problem 4:
    def knows(self, trick):
        if trick in self.tricks:
            print(f"Yes, {self.name} knows {trick}")
            return True
        else:
            print(f"No, {self.name} doesn't know {trick}")
            return False

# Problem 5:
if __name__ == "__main__":
    sugar = Dog('Sugar', 'border collie')
    print(sugar.name) 
    print(sugar.breed)  
    print(sugar.tricks)  

    sugar.teach('frisbee') 
    print(sugar.tricks)  

    print(sugar.knows('frisbee')) 
    print(sugar.knows('arithmetic'))  

    print(Dog.species) 
    print(sugar.species)  