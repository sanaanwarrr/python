# PROBLEM 1
def safeOpen(filename):
    try:
        return open(filename, 'r')
    except FileNotFoundError:
        return None

# PROBLEM 2
def safeFloat(x):
    try:
        return float(x)
    except (ValueError, TypeError):
        return 0.0

# PROBLEM 3
def averageSpeed():
    attempts = 0
    file = None

    while attempts < 2:
        filename = input("enter file name: ")
        file = safeOpen(filename)
        if file:
            break
        else:
            attempts += 1
            if attempts < 2:
                print("file not found. please try again.")
            else:
                print("file not found. yet another human error. goodbye.")
                return

    valid_speeds = []
    for line in file:
        readings = line.split()
        for reading in readings:
            speed = safeFloat(reading) 
            if speed > 2: 
                valid_speeds.append(speed)

    file.close()

    if valid_speeds:
        average = sum(valid_speeds) / len(valid_speeds)
        print(f"average speed is {average:.2f} miles per hour.")
    else:
        print("no valid speeds found in the file.")