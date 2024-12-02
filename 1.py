import utils

def start():
    leftArray, rightArray = utils.getArray('testnumbers.txt')
    leftArray.sort()
    rightArray.sort()
    print(leftArray, rightArray)
    total = 0
    for i, number1 in enumerate(leftArray):
      number2 = rightArray[i]
      # print(number1)
      value = abs(number1 - number2)
      print(value)
      total += value
    print(total)
if __name__ == "__main__":
    start()
