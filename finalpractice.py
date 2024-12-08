# PROBLEM 1
a = ['i', 'never', 'study']
b = ['i', 'study', 'often']
c = a[0] + a[2] + b[1:]
print(c)

# output = TypeError

# a[0] = 'i' (string)
# a[2] = 'often' (string)
# b[1:] = ['study', 'often'] (list)
# you cannot add strings and lists together, thus making it a TypeError

# PROBLEM 2
def funJ(num):
    print(num, end=' ')
    num += 2
    return num
def funI(num):
    num += 2
    num = funJ(num)
    print(num, end=' ')
    return num
def funH(num):
    num += 3
    print(num, end=' ')
    num = funI(num)
    return num

num = 1
print(funH(num))

# output = 4 6 8 8 

# FUNCTION H: plug in 1 for num, 1 + 3 = 4, print 4, plug into FUNCTION I
# FUNCTION I: plug in 4 for num, 4 + 2 = 6, plug into FUNCTION J
# FUNCTION J: plug in 6 for num, print 6, 6 + 2 = 8, return FUNCTION J
# PLUG BACK INTO FUNCTION I: plug in 8 for num, print 8, return FUNCTION I
# PLUG BACK INTO FUNCTION H: plug in 8 for num, return FUNCTION H
# PRINT FUNCTION H = 8

# PROBLEM 3: the term for bundling variables and member functions, also called methods, together in a class is called: encapsulation.

# PROBLEM 4: the relation between a class and an object is: an object is an instance of a class.

# PROBLEM 5:
tpl = ('g','o','o','d','b','y','e')
lst = []
vowels = 'aeiou'
for el in tpl:
    if el not in vowels:
        lst.append(el)
print(list[2:3]*4)

# output = ['b','b','b','b']

# LOOP: appends all consonants into the list. lst = ['g','b','y']
# LIST: slices at index 2 not including 3 ['b']
# PRINT: multiplies the list ['b'] by 4 <-- strings and lists can be multiplied, will repeat the element

# PROBLEM 6:
bools = [True or False, True, False, True and False]
output = 0
for i in range(len(bools)):
    if bools[i]:
        output += 1
    else:
        output *= 2
print(output)

# output = 8

# TRUE OR FALSE = TRUE, 0 + 1 = 1
# TRUE = TRUE, 1 + 1 = 2
# FALSE = FALSE, 2 * 2 = 4
# TRUE AND FALSE = FALSE, 4 * 2 = 8

# PROBLEM 7: what is the name of the exception raised when a program stateemnt attempts to evaluate an unassigned identifier? : NameError

# PROBLEM 8:

# 1: def readAge(fileName)
# 2:    infile = open(filename)
# 3:    strAge = infile.readline()
# 4:    age = int(strAge) + 1
# 5:    return 'Next year you will be { }'.format(age)

# which lines could possibly throw an exception?
# LINE 2: there may not be an existing file with that name
# LINE 4: strAge may not contain an integer, thus you cannot do addition

# PROBLEM 9:

def myFunction(d):
    if 2 in d:
        return d[2]
    else:
        return 2 in d
d = {1:'for the money', 2:'for the show'}
print(myFunction(d))

# output = for the show

# DICTIONARY: if 2 is a member of the keys in the dictionary, then print out its definition

# PROBLEM 10:
def myFunction(d):
    lst = []
    for thing in d:
        if 'y' in d(thing):
            lst.append(thing)
    return let
d = {'tree':'oak','fish':'guppy', 'dog':'boxer', 'cat':'tabby'}
print(myFunction(d))

# output = ['fish','cat']

# KEYS are being appended, not the values
# TREE: no y in oak, key not appended
# FISH: y in guppy, key appended
# DOG: no y in dog, key not appended
# CAT: y in tabby, key appended

# PROBLEM 11: ???????????????????

# PROBLEM 12:
# expected output {95:3. 96:1, 100:3, 85: 1, 90:1}

counters = {}
for items in theList:
    if items not in counters:
        counters[item] = 1
    else:
        counters[item] += 1
return counters
grades = [95,96,100,85,90,95,100,100]
print(frequency(grades))

# IF: if you dont see the item, add it to the dictionary.
# ELSE: if the item is there, add to its count

# PROBLEM 13:
def cities(cityList):
    lst = []
    i = 0
    while True:
        city = cityList[i]
        i += 1
        if city == 'baltimore':
            break
        lst.append(city)
    return lst

lst = ['new york', 'philadelphia', 'newark'] 
print(cities(lst))

# output = ['new york', 'philadelphia', 'newark']

# indexes are plugged into the list, appending the items into the list until baltimore. 

# PROBLEM 14:
num = "4.5"
print(int(num))

# output = ValueError
# cannot convert a float to an integer, value is not in the right form

# PROBLEM 15: 
class Point:
    '''represent a point in a euclidean plane'''
    def __init__(self, x_coor, y_coor): 
        self.x = x_coor
        self.y = y_coor
    def coordinates(self):
        '''return a tuple of the x,y coordinates '''
        return (self.x, self.y)
    def move_to(self, x_coor, y_coor):
        '''assign new coordinates to a point'''
        self.x = x_coor
        self.y = y_coor

# PROBLEM 16:
def readAge(filename):
    strAge = None
    while True:
        try:
            if strAge == None:
                infile = open(filename)
                strAge = infile.readline()
            age = int(strAge)
            print('next year you will be', age + 1)
            break
        except ValueError:
            print('value cannot be coverted to integer.')
            strAge = input("enter a proper age: ")
        except FileNotFoundError:
            print('input file is missing:', "'" + filename + "'")
            filename = input('enter a new filename: ')

# PROBLEM 17:
