def getArray(fileName="numbers.txt"):
    leftArray = []
    rightArray = []
    with open(fileName) as f:
        for line in f:
            numbers = []
            numbers = line.split("   ")
            leftArray.append(int(numbers[0]))
            rightArray.append(int(numbers[1]))
    return leftArray, rightArray