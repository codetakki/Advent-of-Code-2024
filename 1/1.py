import utils

def start():
    leftArray, rightArray = utils.getArray('numbers.txt')
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
    print("Answ 1: ", total)
    total = 0
    for number in leftArray:
      countInRight = rightArray.count(number)
      total += number * countInRight
      
    print("Answ 2: ", total)
if __name__ == "__main__":
    start()
