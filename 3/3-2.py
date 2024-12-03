import re
def start():
  text = open('3/input.txt', 'r').read()
  dontText = re.sub(r"don't\(\)[\s\S]*?do\(\)", "", text)
  cleanText = re.findall(r"mul\(\d{1,3},\d{1,3}\)", dontText )
  total = 0
  for item in cleanText:
    numbers = re.findall(r"\d{1,3}", item )
    total += int(numbers[0]) * int(numbers[1])
  print(total)
start()