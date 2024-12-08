# question one - part a

def hasFinalLetter(strList,letters):
    result = []
    letters = set(letters.lower())
    for word in strList:
        if word[-1].lower() in letters:
            result.append(word)
    return result

# question one - part b (test cases)

strList1 = ["anna", "bella", "carmen", "david"]
letters1 = "abc"
result1 = hasFinalLetter(strList1, letters1)
print(result1) 

strList2 = ["ox","yay","zebra","jazz"]
letters2 = "xyz"
result2 = hasFinalLetter(strList2,letters2)
print(result2)

strList3 = ["dog","elephant","flamingo","gorilla"]
letters3 = "def"
result3 = hasFinalLetter(strList3,letters3)
print(result3)

# question two - part a

def isDivisible(maxInt, twoInts):
    result = []
    for num in range(1, maxInt):
        if num % twoInts[0] == 0 and num % twoInts[1] == 0:
            result.append(num)
    return result

# question two - part b (test cases)

maxInt1 = 20
twoInts1 =(2,3)
result1 = isDivisible(maxInt1, twoInts1)
print(result1)

maxInt2 = 50
twoInts2 = (4,6)
result2 = isDivisible(maxInt2, twoInts2)
print(result2)

maxInt3 = 10
twoInts3 = (3,7)
result3 = isDivisible(maxInt3, twoInts3)
print(result3)
