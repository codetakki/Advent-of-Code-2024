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

def takeTime(function, times=100):
    import datetime
    start_time = datetime.datetime.now()
    for(i) in range(times):
        function()
    end_time = datetime.datetime.now()
    print("time:", end_time - start_time)