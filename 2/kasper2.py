# Description:
# Alla värden måste antingen höjas eller sänkas
# Måste höjas eller sänkas med minst 1 men högst 3
# Om alla höjs eller sänks med minst 1 med högst 3 = safe
# Om inte = unsafe
# Exempelvis 1 2 3 2 4 = unsafe då de både höjs och sänks med 1 och 2
# 1 2 3 4 = safe då de alla höjs med 1
# 6 5 2 1 = safe då alla sänks med minst 1 och högst 3
def day1():
    safe = 0
    unsafe = 0
    with open('2/input.txt', 'r') as file:
        day1Text = file.read()
    for day1Line in day1Text.split('\n'):
        day1ListLine = day1Line.split(' ')
        increaseBool = False
        decreaseBool = False
        isUnsafe = False
        for i in range(len(day1ListLine)-1):
            if int(day1ListLine[i]) == int(day1ListLine[i+1]):
                # print(f"same value {day1ListLine[i]} {day1ListLine[i+1]}")
                # print(int(day1ListLine[i+1]) == int(day1ListLine[i]))
                isUnsafe = True
            elif int(day1ListLine[i]) < int(day1ListLine[i+1]):
                increaseBool = True
                if (int(day1ListLine[i+1]) - int(day1ListLine[i])) > 3:
                    isUnsafe = True
            elif int(day1ListLine[i]) > int(day1ListLine[i+1]):
                decreaseBool = True
                if (int(day1ListLine[i]) - int(day1ListLine[i+1])) > 3:
                    isUnsafe = True
        if isUnsafe == True:
            unsafe += 1
        elif increaseBool == True and decreaseBool == True:
            unsafe += 1
        else:
            safe += 1
        # print(day1Line)
        # print(f"Safe: {safe} Unsafe: {unsafe}")
        
if __name__ == "__main__":
    from utils import takeTime 
    takeTime(day1, 1000)
    