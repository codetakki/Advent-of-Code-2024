import datetime

def start():
  okReports = []
  
  with open("2/input.txt") as f:
    for line in f:
      numbers = [int(x) for x in line.split(" ")]
      # print(numbers)
      if safeOrder(numbers):
        okReports.append(numbers)
        continue
      for i, number in enumerate(numbers):
        numbersMinusOne = numbers.copy()
        numbersMinusOne.pop(i)
        # print(numbersMinusOne)
        if(safeOrder(numbersMinusOne)):
          okReports.append(numbers)
          # print('removing ', i, "results in success")
          break
        
  # print("Safe Reports: ", len(okReports))


def safeOrder(numbers):
  increasing = False
  decreasing = False
  for i, number in enumerate(numbers):
    if i == len(numbers) -1:  
      continue
    nextNumber = numbers[i+1]
    if (number == nextNumber):
      return False
    if (abs(number - nextNumber) > 3):
      return False
    if (number < nextNumber):
      increasing = True
    if (number > nextNumber):
      decreasing = True
    
  if (increasing and decreasing):
    return False
  else:
    return True
  # print("number: ", number, "next: ", nextNumber)
      
if __name__ == "__main__":
  from utils import takeTime 
  takeTime(start, 1000)
