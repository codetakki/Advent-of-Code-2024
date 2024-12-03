import re

from utils import takeTime

def start():
  text = open('3/test2.txt', 'r').read()
  cleanText = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text )
  total = 0
  for item in cleanText:
    numbers = re.findall(r"\d{1,3}", item )
    total += int(numbers[0]) * int(numbers[1])

takeTime(start, 10000)