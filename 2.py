import utils
def start():
    leftArray, rightArray = utils.getArray()
    total = 0
    for number in leftArray:
      countInRight = rightArray.count(number)
      total += number * countInRight
    print("total: ", total)
if __name__ == "__main__":
    start()