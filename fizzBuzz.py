import sys

FIZZ_NUMBER = 3
FIZZ_VALUE = 'Fizz'
BUZZ_NUMBER = 5
BUZZ_VALUE = 'Buzz'
FIZZBUZZ_VALUES = [FIZZ_VALUE, BUZZ_VALUE]
FIZZBUZZ_NUMBERS = [FIZZ_NUMBER, BUZZ_NUMBER]

def repeatUntil(finishFlag):
    index = 1
    conditionRepeat = True
    while conditionRepeat:
        print(index, main(index))
        index += 1
        conditionRepeat = (index <= finishFlag)

def main(number):
    if not (isNumber(number)):
        return ''

    return getResult(number)

def getResult(number):
    result = ''
    
    index = 0
    for value in FIZZBUZZ_VALUES:
        if(checkQuotient(number, FIZZBUZZ_NUMBERS[index])):
            result += value
        index += 1
    
    return result

def checkQuotient(number, quotient):
    if((int(number) % quotient) == 0):
        return True
    return False 

def isNumber(value):
    if(str(value).isnumeric()):
        return True
    
    return False

repeatUntil(100)