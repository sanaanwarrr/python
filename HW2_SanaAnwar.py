# PART 1A
a = 3
b = 4
c = 5

# PART 1B
if a < b:
    print("OKB")

# PART 1C
if c < b:
    print("OKC")

# PART 1D
if a + b == c:
    print("OKD")

# PART 1E
if a**2 + b**2 == c**2:
    print("OKE")

#PART 2
if a**2 + b**2 == c**2:
    print("OKF")
else:
    print("NOT OK")

# PART 3
grades = ['A', 'F', 'C', 'F', 'A', 'B', 'A', 'C', 'A', 'B']
frequency = [grades.count('A'), grades.count('B'), grades.count('C'), grades.count('D'), grades.count('F')]
print(frequency)

# PART 4
dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

herding_dogs = dog_breeds[:2]
tiny_dogs = [dog_breeds[-1]]
print('Persian' in dog_breeds)

print(herding_dogs)
print(tiny_dogs)
